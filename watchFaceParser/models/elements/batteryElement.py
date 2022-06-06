import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement


class BatteryElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._text = None
        self._percent = None
        self._scale = None
        self._gauge = None
        self._circle = None
        super(BatteryElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        from watchFaceParser.models.elements.basic.valueElement import ValueElement
        if parameterId == 1:
            from watchFaceParser.models.elements.battery.batteryNumberElement import BatteryNumberElement
            self._text = BatteryNumberElement(parameter = parameter, parent = self, name = '?_text?')
            return self._text
        elif parameterId == 2:
            from watchFaceParser.models.elements.battery.batteryGaugeElement import BatteryGaugeElement # temp.
            self._gauge = BatteryGaugeElement(parameter = parameter, parent = self, name = '?Icon?')
            return self._gauge
        elif parameterId == 3:
            from watchFaceParser.models.elements.battery.batteryIconsetElement import BatteryIconSetElement
            self._scale = BatteryIconSetElement(parameter = parameter, parent = self, name = 'Scale')
            return self._scale
        elif parameterId == 4:
            from watchFaceParser.models.elements.battery.batteryCircleProgressElement import BatteryCircleProgressElement
            self._circle = BatteryCircleProgressElement(parameter = parameter, parent = self, name = 'Circle')
            return self._circle
        else:
            return super(BatteryElement, self).createChildForParameter(parameter)

