import logging

class ImageHelper:
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

    @staticmethod
    def ditherImage(image):
        from PIL import Image, features
        transparentCoords = []
        width = image.size[0]
        height = image.size[1]
        # save coordinates of transparent pixels in list
        for y in range(height):
            for x in range(width):
                coordinate = (x, y)
                pixel_color = image.getpixel(coordinate)
                (r, g, b, a) = pixel_color
                if a < 128:
                    transparentCoords.append(coordinate)

        palette = [] 
        for s in ImageHelper.bipSColours:
            palette.extend(ImageHelper.hex_to_tuple(s))

        p_img = Image.new('P', (16, 16))
        p_img.putpalette( palette * 4 )

        if features.check_feature(feature="libimagequant"):
            logging.debug("Dither image with libimagequant method")
            image = image.convert('RGB').quantize(method=Image.LIBIMAGEQUANT, palette=p_img, dither=Image.FLOYDSTEINBERG).convert('RGBA')
        else:
            logging.debug("Dither image with default method")
            image = image.convert('RGB').quantize(palette=p_img, dither=Image.FLOYDSTEINBERG).convert('RGBA')
        # restore transparent pixels
        for coordinate in transparentCoords:
            image.putpixel(coordinate, (0, 0, 0, 0))
        return image

    @staticmethod
    def hex_to_tuple(s):
        return [ int(s[:2], 16), int(s[2:4], 16), int(s[4:], 16) ]
    