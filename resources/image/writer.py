import imp
from io import BytesIO
import logging
import math


from resources.image.bitwriter import BitWriter
from watchFaceParser.models.color import Color

class Writer:
    signature = bytearray(b'BMd\x00')

    bipSColours = [
     '000000' ,'000055' ,'0000aa' ,'0000ff' ,'005500' ,'005555' ,'0055aa' ,'0055ff' 
    ,'00aa00' ,'00aa55' ,'00aaaa' ,'00aaff' ,'00ff00' ,'00ff55' ,'00ffaa' ,'00ffff'
    ,'550000' ,'550055' ,'5500aa' ,'5500ff' ,'555500' ,'555555' ,'5555aa' ,'5555ff'
    ,'55aa00' ,'55aa55' ,'55aaaa' ,'55aaff' ,'55ff00' ,'55ff55' ,'55ffaa' ,'55ffff'
    ,'aa0000' ,'aa0055' ,'aa00aa' ,'aa00ff' ,'aa5500' ,'aa5555' ,'aa55aa' ,'aa55ff'
    ,'aaaa00' ,'aaaa55' ,'aaaaaa' ,'aaaaff' ,'aaff00' ,'aaff55' ,'aaffaa' ,'aaffff'
    ,'ff0000' ,'ff0055' ,'ff00aa' ,'ff00ff' ,'ff5500' ,'ff5555' ,'ff55aa' ,'ff55ff'
    ,'ffaa00' ,'ffaa55' ,'ffaaaa' ,'ffaaff' ,'ffff00' ,'ffff55' ,'ffffaa' ,'ffffff'
    ]

    def __init__(self, stream):
        self._writer = stream
        self._palleteColorsArray = []
        self._paletteColors = 0
        self._transparency = 0

    def hex_to_tuple(self, s):
        return [ int(s[:2], 16), int(s[2:4], 16), int(s[4:], 16) ]
    

    

    def write(self, image):
        from PIL import Image, features
        # palette = [] 
        # for s in self.bipSColours:
        #     palette.extend(self.hex_to_tuple(s))

        # p_img = Image.new('P', (16, 16))
        # p_img.putpalette( palette * 4 )
        
        from watchFaceParser.config import Config

        if Config.isDither():
            if features.check_feature(feature="libimagequant"):
                logging.debug("Dither image with libimagequant method")
                #self._image = image.convert('RGB').quantize(colors=Config._ditherDepth, method=Image.LIBIMAGEQUANT, palette=p_img, dither=Image.FLOYDSTEINBERG).convert('RGBA')
                self._image = image.quantize(colors=Config._ditherDepth, method=Image.LIBIMAGEQUANT, dither=Image.FLOYDSTEINBERG).convert('RGBA')
            else:
                logging.debug("Dither image with default method")
                #self._image = image.convert('RGB').quantize(colors=Config._ditherDepth, palette=p_img, dither=Image.FLOYDSTEINBERG).convert('RGBA')
                self._image = image.quantize(colors=Config._ditherDepth, dither=Image.FLOYDSTEINBERG).convert('RGBA')
        else: 
            self._image = image.convert('RGBA')

        self._width = image.size[0]
        self._height = image.size[1]

        self.ExtractPalette()

        if (self._bitsPerPixel > 4 and self._bitsPerPixel < 8):
            self._bitsPerPixel = 8;
        if (self._bitsPerPixel == 3):
            self._bitsPerPixel = 4
        if (self._bitsPerPixel == 0):
            self._bitsPerPixel = 1

        if (self._bitsPerPixel > 8):
            raise Exception(
                f"The image has {self._bitsPerPixel} bit/pixel and can't be packed for using on the watches. Looks like dithering works incorrectly on the image."
            )

        self._rowLengthInBytes = math.ceil(self._width * self._bitsPerPixel / 8)

        self._writer.write(Writer.signature)

        self.writeHeader()
        self.writePallete()
        self.writeImage()

    def ExtractPalette(self):
        logging.debug("Extracting palette...");
        self._palleteColorsArray = []
        for y in range(self._height):
            for x in range(self._width):
                coordinate = (x, y)
                pixel_color = self._image.getpixel(coordinate)
                if pixel_color in self._palleteColorsArray:
                    continue
                (r, g, b, a) = pixel_color
                if a < 128 and self._transparency == 0:
                    logging.debug(f"Palette item {len(self._palleteColorsArray)}: R {hex(r)}, G {hex(g)}, B {hex(b)}, Transaparent color")
                    self._palleteColorsArray.insert(0, pixel_color)
                    self._transparency = 1
                else:
                    logging.debug(f"Palette item {len(self._palleteColorsArray)}: R {hex(r)}, G {hex(g)}, B {hex(b)}")
                    self._palleteColorsArray.append(pixel_color)

        startIndex = 1 if (self._transparency != 0) else 0

        palleteColors = len(self._palleteColorsArray)
        for i in range(startIndex, palleteColors - 1):
            minColor = Color.toInt(self._palleteColorsArray[i])
            minIndex = i
            for j in range(i + 1, palleteColors):
                pixel_color = Color.toInt(self._palleteColorsArray[j])
                if (pixel_color >= minColor):
                    continue

                minColor = pixel_color
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
        self._writer.write(self._transparency.to_bytes(2, byteorder='little'))

    def writePallete(self):
        logging.debug("Writing palette...");
        for color in self._palleteColorsArray:
            (r, g, b, a) = color
            self._writer.write(r.to_bytes(1, byteorder='little'))
            self._writer.write(g.to_bytes(1, byteorder='little'))
            self._writer.write(b.to_bytes(1, byteorder='little'))
            self._writer.write(b'\x00') # always 0 maybe padding
            
    def writeImage(self):
        logging.debug("Writing image...")

        paletteHash = {}
        i = 0
        for color in self._palleteColorsArray:
            paletteHash[color] = i
            i += 1
        for y in range(self._height):
            bitWriter = BitWriter(self._writer)
            for x in range(self._width):
                coordinate = (x, y)
                color = self._image.getpixel(coordinate)
                (r, g, b, a) = color
                if (a < 128 and self._transparency == 1):
                    bitWriter.WriteBits(0, self._bitsPerPixel)
                else:
                    paletteIndex = paletteHash[color]
                    bitWriter.WriteBits(paletteIndex, self._bitsPerPixel);
            bitWriter.Flush()
