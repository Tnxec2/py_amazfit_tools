class Config:
    _image_size = 176
    _preview_size = 110
    _dither = True
    _ditherDepth = 16

    @staticmethod
    def getImageSize():
        return Config._image_size


    @staticmethod
    def getImageSizeHalf():
        return int(Config._image_size / 2)


    @staticmethod
    def getPreviewSize():
        # return (Config._preview_size, Config._preview_size)
        return Config._preview_size

    @staticmethod
    def setDither(nodither):
        Config._dither = False if nodither else True

    @staticmethod
    def isDither():
        return Config._dither