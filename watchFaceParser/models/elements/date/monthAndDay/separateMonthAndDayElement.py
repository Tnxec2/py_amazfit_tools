import logging

from watchFaceParser.models.elements.basic.compositeElement import CompositeElement


class SeparateMonthAndDayElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._month = None
        self._monthName = None
        self._day = None
        super(SeparateMonthAndDayElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)



    def draw4(self, drawer, resources, state, twoDigitsMonth=False, twoDigitsDay=False):
        assert(type(resources) == list)
        monthAndDay = self._parent

        if self._month:
            self._month.draw4(drawer, resources, state.getTime().month, 2 if twoDigitsMonth else 1)
        if self._monthName:
            self._monthName.draw3(drawer, resources, state.getTime().month-1)
        if self._day:
            self._day.draw4(drawer, resources, state.getTime().day, 2 if twoDigitsDay else 1)


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.common.numberElement import NumberElement
            self._month = NumberElement(parameter = parameter, parent = self, name = 'Month')
            return self._month
        elif parameterId == 2:
            from watchFaceParser.models.elements.common.imageSetElement import ImageSetElement
            self._monthName = ImageSetElement(parameter = parameter, parent = self, name = 'MonthName')
            return self._monthName
        elif parameterId == 3:
            from watchFaceParser.models.elements.common.numberElement import NumberElement
            self._day = NumberElement(parameter = parameter, parent = self, name = 'Day')
            return self._day
        else:
            return super(SeparateMonthAndDayElement, self).createChildForParameter(parameter)
