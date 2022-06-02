import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement


class TpodayElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._separate_temperature = None
        self._oneline = None
        super(TpodayElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, images, state):
        if self._separate_temperature:
            self._separate_temperature.draw3(drawer, images, state)
        if self._oneline:
            self._oneline.draw3(drawer, images, state)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.separateTemperature import SeparateTemperatureElement
            self._separate_temperature = SeparateTemperatureElement(parameter = parameter, parent = self, name = 'SeparateTemperature')
            return self._wee_separate_temperaturekDay
        elif parameterId == 2:
            from watchFaceParser.models.elements.oneLineTemperature import OneLineElement
            self._oneline = OneLineElement(parameter = parameter, parent = self, name = 'OneLine')
            return self._oneline
        else:
            return super(TpodayElement, self).createChildForParameter(parameter)
