import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement


class DateElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._monthAndDay = None
        self._weekDay = None
        self._monthalt = None
        self._dayalt = None
        super(DateElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, images, state):
        if self._monthAndDay:
            self._monthAndDay.draw3(drawer, images, state)
        
        if self._weekDay:
            self._weekDay.draw3(drawer, images, state)
        if self._monthalt:
            self._monthalt.draw4(drawer, images, state.getMonth(), 2)
        if self._dayalt:
            self._dayalt.draw4(drawer, images, state.getDay(), 2)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.date.monthAndDayElement import MonthAndDayElement
            self._monthAndDay = MonthAndDayElement(parameter = parameter, parent = self, name = 'MonthAndDay')
            return self._monthAndDay
        elif parameterId == 2:
            from watchFaceParser.models.elements.date.weekDayElement import WeekDayElement
            self._weekDay = WeekDayElement(parameter = parameter, parent = self, name = 'WeekDay')
            return self._weekDay
        elif parameterId == 11:
            from watchFaceParser.models.elements.common.numberExtendedElement import NumberExtendedElement
            self._monthalt = NumberExtendedElement(parameter = parameter, parent = self, name = 'MonthAlt')
            return self._monthalt
        elif parameterId == 12:
            from watchFaceParser.models.elements.common.numberExtendedElement import NumberExtendedElement
            self._dayalt = WeekDayElement(parameter = parameter, parent = self, name = 'DayAlt')
            return self._dayalt
        else:
            return super(DateElement, self).createChildForParameter(parameter)
