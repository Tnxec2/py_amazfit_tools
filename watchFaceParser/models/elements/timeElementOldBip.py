import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement


class TimeElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._hours = None
        self._minutes = None
        self._seconds = None
        self._amPm = None
        self._drawingOrder = None
        self._pm = None
        super(TimeElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def draw3(self, drawer, images, state):
        assert(type(images) == list)
        if self._amPm:
            self._amPm.draw3(drawer, images, state)

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
        else:
            return super(TimeElement, self).createChildForParameter(parameter)

