import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement


class SeparateTemperatureElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._day = None
        self._night = None
        self._dayalt = None
        self._nightalt = None
        super(SeparateTemperatureElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def draw3(self, drawer, images, state):
        if self._day:
            self._day.draw4(drawer, images, state.getCurrentTemperature()+7)
        if self._night:
            self._night.draw4(drawer, images, state.getCurrentTemperature()-7)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.temperatureNumberElement import TemperatureNumberElement
            self._day = TemperatureNumberElement(parameter = parameter, parent = self, name = 'Day')
            return self._day
        elif parameterId == 2:
            from watchFaceParser.models.elements.temperatureNumberElement import TemperatureNumberElement
            self._night = TemperatureNumberElement(parameter = parameter, parent = self, name = 'Night')
            return self._night
        elif parameterId == 3:
            from watchFaceParser.models.elements.common.coordinatesElement import CoordinatesElement
            self._dayalt = CoordinatesElement(parameter = parameter, parent = self, name = 'DayAlt')
            return self._dayalt
        elif parameterId == 4:
            from watchFaceParser.models.elements.common.coordinatesElement import CoordinatesElement
            self._nightalt = CoordinatesElement(parameter = parameter, parent = self, name = 'NightAlt')
            return self._nightalt
        else:
            return super(SeparateTemperatureElement, self).createChildForParameter(parameter)
