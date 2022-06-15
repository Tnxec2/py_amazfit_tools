class Config:
    _image_size = 176
    _preview_size = 108
    _dither = True
    _oldBip = False
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
    def setOldBip(old):
        Config._oldBip = True if old else False

    @staticmethod
    def isDither():
        return Config._dither
    @staticmethod
    def isOldBip():
        return Config._oldBip