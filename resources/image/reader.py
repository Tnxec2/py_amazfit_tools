import logging
import io
from PIL import Image

import resources.image.bitreader
import resources.image.color


class Reader():
    def __init__(self, stream):
        self._reader = stream
        self._bip = True
        self._bmd = False
        self._palleteColorsArray = []

# TODO: read images BM0x1b zepp Dz9GUS6zjaJEJpsdNaKVdJieyELjKoSRf9VJOMi6

    def read(self):
        signature = self._reader.read(4)
        if signature[0] != ord('B') or signature[1] != ord('M'):
            print(signature)
            raise TypeError("Image signature doesn't match.")
        
        self.readHeader()

        if self._palleteColors > 256:
            raise TypeError("Too many palette colors.")

        if self._palleteColors > 0:
            self.readPallete()
        else:
            if self._bitsPerPixel != 8 and self._bitsPerPixel != 16 and self._bitsPerPixel != 24 and self._bitsPerPixel != 32:
                raise TypeError("Image format is not supported")
        return self.readImage()
    
    def readImage(self):
        if self._palleteColors > 0:
            return self.readPalleteImage()
        if self._bitsPerPixel == 8:
            return self.readImage8()
        if self._bitsPerPixel == 16:
            return self.readImage16()
        if self._bitsPerPixel == 24:
            return self.readImage24()
        if self._bitsPerPixel == 32:
            return self.readImage32()

    def readPalleteImage(self):
        logging.debug("Read pallete image...")
        image = Image.new('RGBA', (self._width, self._height))
        
        for y in range(self._height):
            rowBytes = self._reader.read(self._rowLengthInBytes)
            bitReader = resources.image.bitreader.BitReader(rowBytes)
            for x in range(self._width):
                pixelColorIndex = bitReader.ReadBits(self._bitsPerPixel)
                if (pixelColorIndex < len(self._palleteColorsArray)):
                    color = self._palleteColorsArray[pixelColorIndex]
                else:
                    logging.warning(f"x: {x}, y: {y}, pixelColorIndex {pixelColorIndex} out of pallete range {len(self._palleteColorsArray)}")
                    color = self._palleteColorsArray[len(self._palleteColorsArray)-1]
                image.putpixel((x, y), color)

        return image

    def readImage8(self):
        logging.debug("Read 8 Bit image...")
        image = Image.new('RGBA', (self._width, self._height))
        
        for y in range(self._height):
            rowBytes = self._reader.read(self._rowLengthInBytes)
            for x in range(self._width):
                b = rowBytes[x]
                color = resources.image.color.Color.fromArgb(255, b, b, b)
                image.putpixel((x,y), color)
        return image

    def readImage16(self):
        logging.debug("Read 16 Bit image...")
        image = Image.new('RGBA', (self._width, self._height))

        for y in range(self._height):
            rowBytes = self._reader.read(self._rowLengthInBytes)
            bitReader = resources.image.bitreader.BitReader(rowBytes)
            for x in range(self._width):
                firstByte = bitReader.ReadByte()
                secondByte = bitReader.ReadByte()
                b = (secondByte >> 3) & 0x1F << 3
                g = ((firstByte >> 5 & 7) | ((secondByte & 7) << 3)) << 2
                r = (firstByte & 0x1F) << 3
                alpha = 255
                color = resources.image.color.Color.fromArgb(alpha, r, g, b)
                image.putpixel((x, y), color)
        return image

    def readImage24(self):
        logging.debug("Read 24 Bit image...")
        image = Image.new('RGBA', (self._width, self._height))

        for y in range(self._height):
            rowBytes = self._reader.read(self._rowLengthInBytes)
            bitReader = resources.image.bitreader.BitReader(rowBytes)
            for x in range(self._width):
                firstByte = bitReader.ReadByte()
                a = 255 - firstByte
                b = bitReader.ReadBits(5) << 3
                g = bitReader.ReadBits(6) << 2
                r = bitReader.ReadBits(5) << 3

                color = resources.image.color.Color.fromArgb(a, r, g, b)
                image.putpixel((x, y), color)
        return image

    def readImage32(self):
        logging.debug("Read 32 Bit image...")
        image = Image.new('RGBA', (self._width, self._height))

        for y in range(self._height):
            rowBytes = self._reader.read(self._rowLengthInBytes)
            for x in range(self._width):
                r = rowBytes[x * 4]
                g = rowBytes[x * 4 + 1]
                b = rowBytes[x * 4 + 2]
                a = rowBytes[x * 4 + 3]
                alpha = 255 - a
                color = resources.image.color.Color.fromArgb(alpha, r, g, b)
                image.putpixel((x, y), color)
        return image

    def readHeader(self):
        logging.debug("Reading image header(readHeaderD)..")
        self._width = int.from_bytes(self._reader.read(2), byteorder='little')
        self._height = int.from_bytes(self._reader.read(2), byteorder='little')
        self._rowLengthInBytes = int.from_bytes(self._reader.read(2), byteorder='little')
        self._bitsPerPixel = int.from_bytes(self._reader.read(2), byteorder='little')
        self._palleteColors = int.from_bytes(self._reader.read(2), byteorder='little')
        self._unknown1 = int.from_bytes(self._reader.read(2), byteorder='little')
        self._transparency = self._unknown1 > 0

        logging.debug("Image header was read:")
        logging.debug(f"Width: {self._width}, Height: {self._height}, RowLength: {self._rowLengthInBytes}")
        logging.debug(f"BPP: {self._bitsPerPixel}, palleteColors: {self._palleteColors}, Transparency: {self._transparency}")

    def readPallete(self):
        logging.debug("Reading palette..")
        self._palleteColorsArray = []
        for item in range(self._palleteColors):
            r = int.from_bytes(self._reader.read(1), byteorder='little')
            g = int.from_bytes(self._reader.read(1), byteorder='little')
            b = int.from_bytes(self._reader.read(1), byteorder='little')
            padding = int.from_bytes(self._reader.read(1), byteorder='little') # // always 0 maybe padding
            a = 0x00 if (self._transparency and item == 0) else 0xFF
            if (padding != 0):
                logging.warning(f"Palette item {item} last byte is not zero: {padding}");

            logging.debug(f"Palette item {item}: R: {hex(r)}, G: {hex(g)}, B: {hex(b)}, A: {hex(a)}")

            self._palleteColorsArray.insert(item, (r, g, b, a ) )
            

    def convert16olorto32(self, pixel):
        (r, g, b, a) = pixel
        r = r << 3
        g = g << 3
        b = b << 3
        return r, g, b