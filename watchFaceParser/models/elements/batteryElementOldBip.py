import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement


class BatteryElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._text = None
        self._icon = None
        self._scale = None
        super(BatteryElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, images, state):
        if self._text:
            self._text.draw4(drawer, images, state.getBatteryLevel())
        if self._icon:
            self._icon.draw4(drawer, images, state.getBatteryLevel(), 100)
        if self._scale:
            self._scale.draw4(drawer, images, state.getBatteryLevel(), 100)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.common.numberElement import NumberElement
            self._text = NumberElement(parameter = parameter, parent = self, name = '?_text?')
            return self._text
        elif parameterId == 2:
            from watchFaceParser.models.elements.common.imageSetElement import ImageSetElement
            self._icon = ImageSetElement(parameter = parameter, parent = self, name = '?Icon?')
            return self._icon
        elif parameterId == 3:
            from watchFaceParser.models.elements.common.linearIconSetElement import LinearIconSetElement
            self._scale = LinearIconSetElement(parameter = parameter, parent = self, name = 'Scale')
            return self._scale
        else:
            return super(BatteryElement, self).createChildForParameter(parameter)

