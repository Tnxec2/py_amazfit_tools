import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement
from resources.image.color import Color
from watchFaceParser.models.elements.basic.valueElement import ValueElement
from watchFaceParser.config import Config

class BackgroundElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._image = None
        self._color = None
        self._frontImage = None
        super(BackgroundElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getImage(self):
        return self._image


    def getFrontImage(self):
        return self._frontImage

    def getColor(self):
        return self._color

    def draw3(self, drawer, resources, state):
        self.draw2(drawer, resources)

    def draw2(self, drawer, images):
        x = 0
        y = 0

        from PIL import ImageDraw

        if self._image is None:
            if self._color is None:
                self._color = Color.fromArgb(0xff000000)
            size = Config.getImageSize()
            d = ImageDraw.Draw(drawer)
            d.rectangle([(x, y), size, size], fill=self.getColor())
        else:
            self._image.draw2(drawer, images)

        if self._frontImage:
            self._frontImage.draw2(drawer, images)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.common.imageElement import ImageElement
            self._image = ImageElement(parameter = parameter, parent = self, name = 'Image')
            return self._image
        elif parameterId == 2: # color
            self._color = Color.fromArgb(0xff000000 | parameter.getValue())
            return ValueElement(parameter = parameter, parent = self, name = 'BackgroundColor')
        elif parameterId == 3:
            pass
        elif parameterId == 4:
            from watchFaceParser.models.elements.common.imageElement import ImageElement
            self._frontImage = ImageElement(parameter = parameter, parent = self, name = 'FrontImage')
            return self._frontImage
        else:
            return super(BackgroundElement, self).createChildForParameter(parameter)