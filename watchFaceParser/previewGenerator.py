from watchFaceParser.config import Config
if Config.isOldBip():
    from watchFaceParser.models.elements.watchFaceOldBip import WatchFace
else:
    from watchFaceParser.models.elements.watchFace import WatchFace
from watchFaceParser.config import Config

class PreviewGenerator:
    @staticmethod
    def createAnimation(descriptor, images, states):
        previewWatchFace = WatchFace(descriptor)
        for watchState in states:
            image = PreviewGenerator.createFrame(previewWatchFace, images, watchState)
            yield image


    @staticmethod
    def createImage(descriptor, images, state):
        previewWatchFace = WatchFace(descriptor)
        return PreviewGenerator.createFrame(previewWatchFace, images, state)


    @staticmethod
    def createFrame(watchFace, resources, state):
        from PIL import Image, ImageDraw

        graphics = Image.new('RGBA', (Config.getImageSize(), Config.getImageSize()))
        watchFace.draw3(graphics, resources, state)
        if Config.isDither():
            from watchFaceParser.helpers.bipsImageHelper import ImageHelper
            return ImageHelper.ditherImage(graphics)
        else: 
            return graphics
