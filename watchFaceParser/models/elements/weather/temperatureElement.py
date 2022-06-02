import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement


class TemperatureElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._current = None
        self._today = None
        super(TemperatureElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, images, state):
        if self._current:
            self._current.draw3(drawer, images, state.getCurrentTemperature())
        if self._today:
            self._today.draw3(drawer, images, state)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.weather.temperatureNumberElement import TemperatureNumberElement
            self._current = TemperatureNumberElement(parameter = parameter, parent = self, name = 'Current')
            return self._current
        elif parameterId == 2:
            from watchFaceParser.models.elements.weather.todayElement import TodayElement
            self._today = TodayElement(parameter = parameter, parent = self, name = 'Today')
            return self._today
        else:
            return super(TemperatureElement, self).createChildForParameter(parameter)
