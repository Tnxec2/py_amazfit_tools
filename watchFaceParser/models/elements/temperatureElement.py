import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement


class TemperatureElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._current = None
        self._today = None
        super(TemperatureElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.temperatureNumberElement import TemperatureNumberElement
            self._current = TemperatureNumberElement(parameter = parameter, parent = self, name = 'Current')
            return self._current
        elif parameterId == 2:
            from watchFaceParser.models.elements.todayElement import TpodayElement
            self._today = TpodayElement(parameter = parameter, parent = self, name = 'Today')
            return self._today
        else:
            return super(TemperatureElement, self).createChildForParameter(parameter)
