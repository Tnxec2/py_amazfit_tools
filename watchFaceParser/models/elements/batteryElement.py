import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement


class BatteryElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._text = None
        self._scale = None
        self._icon = None
        self._circle = None
        super(BatteryElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    
    def draw3(self, drawer, images, state):
        if self._text:
            self._text.draw3(drawer, images, state)
        if self._icon:
            self._icon.draw4(drawer, images, state.getBatteryLevel(), 100)
        if self._scale:
            self._scale.draw4(drawer, images, state.getBatteryLevel(), 100)
        if self._circle:
            self._circle.draw4(drawer, images, state.getBatteryLevel() , 100)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        from watchFaceParser.models.elements.basic.valueElement import ValueElement
        if parameterId == 1:
            from watchFaceParser.models.elements.battery.batteryNumberElement import BatteryNumberElement
            self._text = BatteryNumberElement(parameter = parameter, parent = self, name = 'Text')
            return self._text
        elif parameterId == 2:
            from watchFaceParser.models.elements.common.imageSetElement import ImageSetElement # temp.
            self._icon = ImageSetElement(parameter = parameter, parent = self, name = 'Icon')
            return self._icon
        elif parameterId == 3:
            from watchFaceParser.models.elements.common.linearIconSetElement import LinearIconSetElement
            self._scale = LinearIconSetElement(parameter = parameter, parent = self, name = 'Scale')
            return self._scale
        elif parameterId == 4:
            from watchFaceParser.models.elements.common.circularProgressElement import CircularProgressElement
            self._circle = CircularProgressElement(parameter = parameter, parent = self, name = 'Circle')
            return self._circle
        else:
            return super(BatteryElement, self).createChildForParameter(parameter)

