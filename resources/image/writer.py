import logging
import math
from resources.image.bitwriter import BitWriter

from resources.image.color import Color


class Writer:
    signature = bytearray(b'BMd\x00')


    def __init__(self, stream):
        self._writer = stream
        self._palleteColorsArray = []
        self._paletteColors = 0
        self._transparency = 0

    def write(self, image):
        self._image = image
        self._width = image.size[0]
        self._height = image.size[1]

        self.ExtractPalette()

        if (self._bitsPerPixel == 3):
            self._bitsPerPixel = 4
        if (self._bitsPerPixel == 0):
            self._bitsPerPixel = 1

        if (self._bitsPerPixel > 4):
            raise Exception(
                f"The image has {self._bitsPerPixel} bit/pixel and can't be packed for using on the watches. Looks like dithering works incorrectly on the image."
            )

        self._rowLengthInBytes = math.ceil(self._width * self._bitsPerPixel / 8)

        self._writer.write(Writer.signature)

        self.writeHeader()
        self.writePallete()
        self.writeImage()

    def ExtractPalette(self):
        logging.info("Extracting palette...");

        for y in range(self._height):
            for x in range(self._width):
                coordinate = (x, y)
                color = self._image.getpixel(coordinate)
                print(color)
                if (color in self._palleteColorsArray):
                    continue

                if (color.a < 0x80 and self._transparency == 0):
                    logging.info(f"Palette item {len(self._palleteColorsArray)}: R {hex(color.r)}, G {hex(color.g)}, B {hex(color.b)}, Transaparent color")
                    self._palleteColorsArray.insert(0, color)
                    self._transparency = 1
                else:
                    logging.info(f"Palette item {len(self._palleteColorsArray)}: R {hex(color.r)}, G {hex(color.g)}, B {hex(color.b)}")
                    self._palleteColorsArray.append(color)

            startIndex = 1 if (self._transparency == 1) else 0

            for i in range(startIndex, len(self._palleteColorsArray) - 1):
                minColor = self._palleteColorsArray[i].ToArgb()
                minIndex = i;
                for j in range(i + 1, len(self._palleteColorsArray)):
                    color = self._palleteColorsArray[j].ToArgb()
                    if (color >= minColor):
                        continue

                    minColor = color
                    minIndex = j

                if (minIndex == i):
                    continue

                tmp = self._palleteColorsArray[i]
                self._palleteColorsArray[i] = self._palleteColorsArray[minIndex]
                self._palleteColorsArray[minIndex] = tmp
            
            self._paletteColors = len(self._palleteColorsArray)
            self._bitsPerPixel = math.ceil(math.log(self._paletteColors, 2))

    def writeHeader(self):
        logging.debug("Writing image header...")
        logging.debug(f"Width: {self._width}, Height: {self._height}, RowLength: {self._rowLengthInBytes}")
        logging.debug(f"BPP: {self._bitsPerPixel}, PalleteColors: {self._paletteColors}, Transparency: {self._transparency}")

        self._writer.write(self._width.to_bytes(2, byteorder='little'))
        self._writer.write(self._height.to_bytes(2, byteorder='little'))
        self._writer.write(self._rowLengthInBytes.to_bytes(2, byteorder='little'))
        self._writer.write(self._bitsPerPixel.to_bytes(2, byteorder='little'))
        self._writer.write(self._paletteColors.to_bytes(2, byteorder='little'))
        self._writer.write(self._transparency.to_bytes(1, byteorder='little'))

    def writePalette(self):
        logging.info("Writing palette...");
        for color in self._palleteColorsArray:
            self._writer.write(color.r.to_bytes(1, byteorder='little'))
            self._writer.write(color.g.to_bytes(1, byteorder='little'))
            self._writer.write(color.b.to_bytes(1, byteorder='little'))
            self._writer.write((0).to_bytes(1, byteorder='little')) # always 0 maybe padding
            
    def writeImage(self):
        logging.debug("Writing image...")

        paletteHash = {}
        i = 0
        for color in self._palleteColorsArray:
            paletteHash[color] = i
            i += 1

        pixels = self._image.convert('RGBA')

        for y in range(self._height):
            rowData = ''
            bitWriter = BitWriter(rowData)
            for x in range(self._width):
                coordinate = (x, y)
                color = self._image.getpixel(coordinate)
                if (color.a < 0x80 and self._transparency == 1):
                    bitWriter.WriteBits(0, self._bitsPerPixel)
                else:
                    paletteIndex = paletteHash[color]
                    bitWriter.WriteBits(paletteIndex, self._bitsPerPixel);

            bitWriter.Flush()
            self._writer.write(rowData)
            
