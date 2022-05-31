import logging
import io
from PIL import Image

import resources.image.bitreader
import resources.image.color


class Reader():
    def __init__(self, stream):
        self._reader = stream
        self._bip = True
        self._bme = False
        self._bmc = False
        self._bmd = False
        self._palleteColorsArray = []


    def read(self):
        signature = self._reader.read(4)
        if signature[0] != ord('B') or signature[1] != ord('M'):
            print(signature)
            raise TypeError("Image signature doesn't match.")

        if signature[2] == 0xff and signature[2] == 0xff:
            logging.warn("The image is 32bit.")
            self._bip = False
        if signature[0] == ord('B') and signature[1] == ord('M') and signature[2] == ord('e'):
            self._bme = True

        if signature[0] == ord('B') and signature[1] == ord('M') and signature[2] == 0x1c:
            self._bmc = True
        if signature[0] == ord('B') and signature[1] == ord('M') and signature[2] == 0x09:
            self._bmc = True
        if signature[0] == ord('B') and signature[1] == ord('M') and signature[2] == 0x64:
            self._bmd = True

        if self._bmd:
            logging.info("The image is bmd.")
            self.readHeaderD()
            return self.readImageD()
        elif self._bme:
            logging.info("The image is bme.")
            self.readHeader16E()
            return self.readImage16E()
        elif self._bmc:
            logging.info("The image is bmc.")
            self.readHeader16C()
            if self._bitsPerPixel == 32:
                return self.readImage()
            elif self._bitsPerPixel == 24:
                return self.readImage24()
            else:
                return self.readImage16()
        else:
            if self._bip:
                self.readHeader16()
            else:
                self.readHeader()

            if self._bitsPerPixel == 32:
                return self.readImage()
            else:
                return self.readImage16()

    def readImageD(self):
        
        image = Image.new('RGBA', (self._width, self._height))
        
        for y in range(self._height):
            rowBytes = self._reader.read(self._rowLengthInBytes)
            reader = resources.image.bitreader.BitReader(rowBytes)
            for x in range(self._width):
                pixelColorIndex = reader.ReadBits(self._bitsPerPixel)
                if (pixelColorIndex < len(self._palleteColorsArray)):
                    color = self._palleteColorsArray[pixelColorIndex]
                    image.putpixel((x, y), color)
        return image

    def readImage(self):
        image = Image.new('RGBA', (self._width, self._height))
        
        alpha = 0
        if self._step != 4:
            alpha = 255
        for y in range(self._height):
            rowBytes = self._reader.read(self._rowLengthInBytes)
            for x in range(self._width):
                b = 0
                g = 0
                r = 0
                try: 
                    b = rowBytes[x * self._step]
                    g = rowBytes[x * self._step + 1]
                    r = rowBytes[x * self._step + 2]
                    if self._step == 4:
                        alpha = rowBytes[x * self._step + 3] 
                except Exception as e:
                    logging.warn(f"missing image bytes x:{x}, y:{y}, skip pixel")
                color = resources.image.color.Color.fromArgb(alpha, r, g, b)
                image.putpixel((x,y), color)
        return image

    def readImage16E(self):
        image = Image.new('RGBA', (self._width, self._height))

        dataIndex = 0
        while dataIndex < self._datasize:
            _y = int.from_bytes(self._reader.read(2), byteorder='little')
            _start = int.from_bytes(self._reader.read(2), byteorder='little')
            _width = int.from_bytes(self._reader.read(2), byteorder='little')
            dataIndex += 6
            #logging.info(f"y: {_y}, start: {_start}, _width: {_width}")

            rowBytes = self._reader.read(_width*2)

            for x in range(_width):
                firstByte = rowBytes[x * self._step]
                secondByte = rowBytes[x * self._step + 1]
                dataIndex += 2
                b = (firstByte & 0x1f)
                g = (((firstByte >> 5) & 0x7) | ((secondByte & 0x07) << 3))
                r = ((secondByte >> 3) & 0x1f)
                b = int(255*b/31.0)
                g = int(255*g/63.0)
                r = int(255*r/31.0)
                alpha = 255
                color = resources.image.color.Color.fromArgb(alpha, r, g, b)
                try:
                    if _start + x < self._width and _y < self._height:
                        image.putpixel(( _start + x, _y), color)
                except Exception as e:
                    logging.fatal(f"start: {_start}, x: {x}, y: {_y}")
                    logging.exception(e)
                    raise e


        return image

    def readImage16(self):
        image = Image.new('RGBA', (self._width, self._height))

        for y in range(self._height):
            rowBytes = self._reader.read(self._rowLengthInBytes)
            for x in range(self._width):
                firstByte = rowBytes[x * self._step]
                secondByte = rowBytes[x * self._step + 1]
                b = (firstByte & 0x1f)
                g = (((firstByte >> 5) & 0x7) | ((secondByte & 0x07) << 3))
                r = ((secondByte >> 3) & 0x1f)
                b = int(255*b/31.0)
                g = int(255*g/63.0)
                r = int(255*r/31.0)
                alpha = 255
                color = resources.image.color.Color.fromArgb(alpha, r, g, b)
                image.putpixel((x, y), color)
        return image

    def readImage24(self):
        image = Image.new('RGBA', (self._width, self._height))
        a = 0
        if self._step != 3:
            a = 255
        for y in range(self._height):
            rowBytes = self._reader.read(self._rowLengthInBytes)
            for x in range(self._width):
                alphaByte = rowBytes[x * self._step]
                firstByte = rowBytes[x * self._step + 2]
                secondByte = rowBytes[x * self._step + 1]

                a = 255 - alphaByte
                b = (firstByte & 0x1f)
                g = (((firstByte >> 5) & 0x7) | ((secondByte & 0x07) << 3))
                r = ((secondByte >> 3) & 0x1f)
                b = int(255*b/31.0)
                g = int(255*g/63.0)
                r = int(255*r/31.0)

                color = resources.image.color.Color.fromArgb(a, r, g, b)
                image.putpixel((x, y), color)
        return image

    def readHeader16(self):
        logging.info("Reading image header(readHeader16)...")
        self._width = int.from_bytes(self._reader.read(2), byteorder='little')
        self._height = int.from_bytes(self._reader.read(2), byteorder='little')
        self._unknown1 = int.from_bytes(self._reader.read(2), byteorder='little')
        self._bitsPerPixel = int.from_bytes(self._reader.read(2), byteorder='little')
        self._step = int(self._bitsPerPixel / 8)
        self._rowLengthInBytes = self._width * self._step
        self._transparency = False
        logging.info("Image header was read:")
        logging.info(f"Width: {self._width}, Height: {self._height}, RowLength: {self._rowLengthInBytes}")
        logging.info(f"unknown1: {self._unknown1}, _step: {self._step}")
        logging.info(f"BPP: {self._bitsPerPixel}, Transparency: {self._transparency}")

    def readHeader16C(self):
        logging.info("Reading image header(readHeader16C)...")
        self._width = int.from_bytes(self._reader.read(2), byteorder='little')
        self._height = int.from_bytes(self._reader.read(2), byteorder='little')
        self._rowLengthInBytes = int.from_bytes(self._reader.read(2), byteorder='little')
        self._bitsPerPixel = int.from_bytes(self._reader.read(2), byteorder='little')
        self._unknown2 = int.from_bytes(self._reader.read(4), byteorder='little')
        self._step = int(self._bitsPerPixel / 8)
        self._transparency = False
        logging.info("Image header was read:")
        logging.info(f"Width: {self._width}, Height: {self._height}, RowLength: {self._rowLengthInBytes}")
        logging.info(f"_step: {self._step}, unknown2: {self._unknown2},")
        logging.info(f"BPP: {self._bitsPerPixel}, Transparency: {self._transparency}")

    def readHeader16E(self):
        logging.info("Reading image header(readHeader16E)...")
        self._width = int.from_bytes(self._reader.read(2), byteorder='little')
        self._height = int.from_bytes(self._reader.read(2), byteorder='little')
        self._rowLengthInBytes = int.from_bytes(self._reader.read(2), byteorder='little')
        self._bitsPerPixel = int.from_bytes(self._reader.read(2), byteorder='little')
        self._datasize = int.from_bytes(self._reader.read(4), byteorder='little')
        self._step = int(self._bitsPerPixel / 8)
        #self._rowLengthInBytes = self._unknown1
        self._transparency = False
        logging.info("Image header was read:")
        logging.info(f"Width: {self._width}, Height: {self._height}, RowLength: {self._rowLengthInBytes}")
        logging.info(f"datalength: {self._datasize}, _step: {self._step}")
        logging.info(f"BPP: {self._bitsPerPixel}, Transparency: {self._transparency}")
        
    def readHeaderD(self):
        logging.info("Reading image header(readHeaderD)...")
        self._width = int.from_bytes(self._reader.read(2), byteorder='little')
        self._height = int.from_bytes(self._reader.read(2), byteorder='little')
        self._rowLengthInBytes = int.from_bytes(self._reader.read(2), byteorder='little')
        self._bitsPerPixel = int.from_bytes(self._reader.read(2), byteorder='little')
        self._palleteColors = int.from_bytes(self._reader.read(2), byteorder='little')
        self._unknown1 = int.from_bytes(self._reader.read(2), byteorder='little')
        self._transparency = self._unknown1 > 0

        logging.info("Image header was read:")
        logging.info(f"Width: {self._width}, Height: {self._height}, RowLength: {self._rowLengthInBytes}")
        logging.info(f"BPP: {self._bitsPerPixel}, palleteColors: {self._palleteColors}, Transparency: {self._transparency}")

        logging.info("Reading palette...")
        self._palleteColorsArray = []
        for item in range(self._palleteColors):
            r = int.from_bytes(self._reader.read(1), byteorder='little')
            g = int.from_bytes(self._reader.read(1), byteorder='little')
            b = int.from_bytes(self._reader.read(1), byteorder='little')
            self._reader.read(1) # // always 0 maybe padding
            a = 0x00 if (self._transparency and item == 0) else 0xFF
            self._palleteColorsArray.append( resources.image.color.Color.fromArgb(a, r, g, b) )
            logging.info(f"Palette item {item}: R: {hex(r)}, G: {hex(g)}, B: {hex(b)}, A: {hex(a)}")


    def readHeader(self):
        logging.info("Reading image header(non-bip)...")
        b = self._reader.read(4)
        logging.debug("basename 7 byte hash " + ''.join(format(x, '02x') for x in b))
        self._width = int.from_bytes(b, byteorder='little')
        self._height = int.from_bytes(self._reader.read(4), byteorder='little')
        self._bitsPerPixel = int.from_bytes(self._reader.read(4), byteorder='little')
        self._unknown1 = int.from_bytes(self._reader.read(4), byteorder='little')
        self._datasize = int.from_bytes(self._reader.read(4), byteorder='little')
        self._step = int(self._bitsPerPixel / 8)
        self._rowLengthInBytes = self._width * self._step
        self._transparency = False
        logging.info("Image header was read:")
        logging.info(f"Width: {self._width}, Height: {self._height}, RowLength: {self._rowLengthInBytes}")
        logging.info(f"unknown1: {self._unknown1}, _unknown2: {self._datasize}, _step: {self._step}")
        logging.info(f"BPP: {self._bitsPerPixel}, Transparency: {self._transparency}")

    def convert16olorto32(self, pixel):
        (r, g, b, a) = pixel
        r = r << 3
        g = g << 3
        b = b << 3
        return r, g, b