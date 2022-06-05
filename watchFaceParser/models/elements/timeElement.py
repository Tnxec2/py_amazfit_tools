import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement


class TimeElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._hours = None
        self._minutes = None
        self._seconds = None
        self._amPm = None
        self._drawingOrder = None
        self._sunriseHours = None
        self._sunriseMinutes = None
        self._sunsetHours = None
        self._sunsetMinutes = None
        self._sunriseHoursNoData = None
        self._sunriseMinutesNoData = None
        self._sunsetHoursNoData = None
        self._sunsetMinutesNoData = None
        self._pm = None
        super(TimeElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def draw3(self, drawer, images, state):
        assert(type(images) == list)
        if self._amPm:
            self._amPm.draw3(drawer, images, state)

        logging.debug(state.getTime())

        hours = state.getTime().hour if self._amPm is None else state.getTime().hour % 12
        # drawingOrder = 0x1234 if self.getDrawingOrder() is None else self.getDrawingOrder()

        if self._hours and self._hours.getTens():
            self._hours.getTens().draw3(drawer, images, int(hours % 100 / 10))
        if self._hours and self._hours.getOnes():
            self._hours.getOnes().draw3(drawer, images, hours % 10)

        if self._minutes and self._minutes.getTens():
            self._minutes.getTens().draw3(drawer, images, int(state.getTime().minute % 100 / 10))
        if self._minutes and self._minutes.getOnes():
            self._minutes.getOnes().draw3(drawer, images, state.getTime().minute % 10)

        if self._seconds:
            self._seconds.draw3(drawer, images, state.getTime().second)
        if self._delimiter:
            self._delimiter.draw3(drawer, images, state)
        
        if self._sunriseHours:
            self._sunriseHours.draw4(drawer, images, state.getSunrise().hour, 2 )        
        if self._sunriseMinutes:
            self._sunriseMinutes.draw4(drawer, images, state.getSunrise().minutes, 2 )
            
        if self._sunsetHours:
            self._sunsetHours.draw4(drawer, images, state.getSunset().hour, 2 )        
        if self._sunsetMinutes:
            self._sunsetMinutes.draw4(drawer, images, state.getSunset().minutes, 2 )


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.common.twoDigitsElement import TwoDigitsElement
            self._hours = TwoDigitsElement(parameter = parameter, parent = self, name = 'Hours')
            return self._hours
        elif parameterId == 2:
            from watchFaceParser.models.elements.common.twoDigitsElement import TwoDigitsElement
            self._minutes = TwoDigitsElement(parameter = parameter, parent = self, name = 'Minutes')
            return self._minutes
        elif parameterId == 3:
            from watchFaceParser.models.elements.common.twoDigitsElement import TwoDigitsElement
            self._seconds = TwoDigitsElement(parameter = parameter, parent = self, name = 'Seconds')
            return self._seconds
        elif parameterId == 4:
            from watchFaceParser.models.elements.time.amPmElement import AmPmElement
            self._amPm = AmPmElement(parameter = parameter, parent = self, name = 'AmPm')
            return self._amPm
        elif parameterId == 5:
            pass
        elif parameterId == 10:
            from watchFaceParser.models.elements.common.numberElement import NumberElement
            self._sunriseHours = NumberElement(parameter = parameter, parent = self, name = 'SunriseHours')
            return self._sunriseHours
        elif parameterId == 11:
            from watchFaceParser.models.elements.common.numberElement import NumberElement
            self._sunriseMinutes = NumberElement(parameter = parameter, parent = self, name = 'SunriseMinutes')
            return self._sunriseMinutes
        elif parameterId == 12:
            from watchFaceParser.models.elements.common.numberElement import NumberElement
            self._sunsetHours = NumberElement(parameter = parameter, parent = self, name = 'SunsetHours')
            return self._sunsetHours
        elif parameterId == 13:
            from watchFaceParser.models.elements.common.numberElement import NumberElement
            self._sunsetMinutes = NumberElement(parameter = parameter, parent = self, name = 'SunsetMinutes')
            return self._sunsetMinutes
        elif parameterId == 14:
            self._sunriseHoursNoData = parameter.getValue()
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            return ValueElement(parameter, self, 'SunriseHoursNoDataImage')
        elif parameterId == 15:
            self._sunriseMinutesNoData = parameter.getValue()
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            return ValueElement(parameter, self, 'SunriseMinutesNoDataImage')
        elif parameterId == 16:
            self._sunsetHoursNoData = parameter.getValue()
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            return ValueElement(parameter, self, 'SunsetHoursNoDataImage')
        elif parameterId == 17:
            self._sunsetMinutesNoData = parameter.getValue()
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            return ValueElement(parameter, self, 'SunsetMinutesNoDataImage')
        else:
            return super(TimeElement, self).createChildForParameter(parameter)

