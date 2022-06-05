import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement

class WeekdayStatusElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._image1 = None
        self._image2 = None
        self._image3 = None
        self._image4 = None
        self._image5 = None
        self._image6 = None
        self._image7 = None
        super(WeekdayStatusElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        weekday = state.getTime().weekday()
        if weekday == 0:
            if self._image1:
                self._image1.draw2(drawer, resources)
        elif weekday == 1:
            if self._image2:
                self._image2.draw2(drawer, resources)
        elif weekday == 2:
            if self._image3:
                self._image3.draw2(drawer, resources)
        elif weekday == 3:
            if self._image4:
                self._image4.draw2(drawer, resources)
        elif weekday == 4:
            if self._image5:
                self._image5.draw2(drawer, resources)
        elif weekday == 5:
            if self._image6:
                self._image6.draw2(drawer, resources)
        else:
            if self._image7:
                self._image7.draw2(drawer, resources)


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.common.imageElement import ImageElement
            self._image1 = ImageElement(parameter = parameter, parent = self, name = 'Monday')
            return self._image1
        elif parameterId == 2:
            from watchFaceParser.models.elements.common.imageElement import ImageElement
            self._image2 = ImageElement(parameter = parameter, parent = self, name = 'Tuesday')
            return self._image3
        elif parameterId == 3:
            from watchFaceParser.models.elements.common.imageElement import ImageElement
            self._image3 = ImageElement(parameter = parameter, parent = self, name = 'Wednesday')
            return self._image3
        elif parameterId == 4:
            from watchFaceParser.models.elements.common.imageElement import ImageElement
            self._image4 = ImageElement(parameter = parameter, parent = self, name = 'Thursday')
            return self._image4
        elif parameterId == 5:
            from watchFaceParser.models.elements.common.imageElement import ImageElement
            self._image5 = ImageElement(parameter = parameter, parent = self, name = 'Friday')
            return self._image5
        elif parameterId == 6:
            from watchFaceParser.models.elements.common.imageElement import ImageElement
            self._image6 = ImageElement(parameter = parameter, parent = self, name = 'Saturday')
            return self._image6
        elif parameterId == 7:
            from watchFaceParser.models.elements.common.imageElement import ImageElement
            self._image7 = ImageElement(parameter = parameter, parent = self, name = 'Sunday')
            return self._image7
        else:
            return super(WeekdayStatusElement, self).createChildForParameter(parameter)