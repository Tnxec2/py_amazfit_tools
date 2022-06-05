import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement


class DateExtendedElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._year = None
        self._month = None
        self._day = None

        super(DateExtendedElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def draw3(self, drawer, images, state):
        assert(type(images) == list)

        if self._year:
            self._year.draw3(drawer, images, state.getTime().year)
        if self._month:
            self._month.draw3(drawer, images, state.getTime().month)
        if self._day:
            self._day.draw3(drawer, images, state.getTime().day)



    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.common.fourDigitsElement import FourDigitsElement
            self._year = FourDigitsElement(parameter = parameter, parent = self, name = 'YearSeparate')
            return self._year
        elif parameterId == 2:
            from watchFaceParser.models.elements.common.twoDigitsElement import TwoDigitsElement
            self._month = TwoDigitsElement(parameter = parameter, parent = self, name = 'MonthSeparate')
            return self._month
        elif parameterId == 3:
            from watchFaceParser.models.elements.common.twoDigitsElement import TwoDigitsElement
            self._day = TwoDigitsElement(parameter = parameter, parent = self, name = 'DaySeparate')
            return self._day
        else:
            return super(DateExtendedElement, self).createChildForParameter(parameter)

