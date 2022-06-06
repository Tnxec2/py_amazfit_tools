import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement

class DistanceProgressElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._circle = None
        self._icon = None
        super(DistanceProgressElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, images, state):
        if self._icon:
            self._icon.draw4(drawer, images, state.getDistance(), 4000)
        if self._circle:
            self._circle.draw4(drawer, images, state.getDistance(), 4000)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            pass
        elif parameterId == 2:
            from watchFaceParser.models.elements.common.imageSetElement import ImageSetElement
            self._icon = ImageSetElement(parameter = parameter, parent = self, name = 'Icon')
            return self._icon
        elif parameterId == 3:
            from watchFaceParser.models.elements.common.circularProgressElement import CircularProgressElement # temp.
            self._circle = CircularProgressElement(parameter = parameter, parent = self, name = 'Circle')
            return self._circle
        else:
            return super(DistanceProgressElement, self).createChildForParameter(parameter)
