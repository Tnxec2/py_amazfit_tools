import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement
from resources.image.color import Color
from watchFaceParser.models.elements.basic.valueElement import ValueElement
from watchFaceParser.config import Config

class BackgroundElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._image = None
        super(BackgroundElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getImage(self):
        return self._image


    def draw3(self, drawer, resources, state):
        self.draw2(drawer, resources)

    def draw2(self, drawer, images):
        if self._image:
            self._image.draw2(drawer, images)


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.common.imageElement import ImageElement
            self._image = ImageElement(parameter = parameter, parent = self, name = 'Image')
            return self._image
        else:
            return super(BackgroundElement, self).createChildForParameter(parameter)