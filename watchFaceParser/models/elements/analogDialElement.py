import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement


class AnalogDialElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._hours = None
        self._minutes = None
        self._seconds = None
        self._amPm = None
        super(AnalogDialElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def draw3(self, drawer, images, state):
        assert(type(images) == list)
        if self._amPm:
            self._amPm.draw3(drawer, images, state)
        if self._hours:
            self._hours.draw3(drawer, images, state)
        if self._minutes:
            self._minutes.draw3(drawer, images, state)
        if self._seconds:
            self._seconds.draw3(drawer, images, state)

        
    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.analogDial.hoursClockHandElement import HoursClockHandElement
            self._hours = HoursClockHandElement(parameter = parameter, parent = self, name = 'Hours')
            return self._hours
        elif parameterId == 2:
            from watchFaceParser.models.elements.analogDial.minutesClockHandElement import MinutesClockHandElement
            self._minutes = MinutesClockHandElement(parameter = parameter, parent = self, name = 'Minutes')
            return self._minutes
        elif parameterId == 3:
            from watchFaceParser.models.elements.analogDial.secondsClockHandElement import SecondsClockHandElement
            self._seconds = SecondsClockHandElement(parameter = parameter, parent = self, name = 'Seconds')
            return self._seconds
        elif parameterId == 4:
            from watchFaceParser.models.elements.time.amPmElement import AmPmElement
            self._amPm = AmPmElement(parameter = parameter, parent = self, name = 'AmPm')
            return self._amPm
        else:
            return super(AnalogDialElement, self).createChildForParameter(parameter)