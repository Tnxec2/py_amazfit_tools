import logging

from watchFaceParser.models.elements.basic.compositeElement import CompositeElement
from watchFaceParser.utils.parametersConverter import uint2int


class OneLineMonthAndDayElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._number = None
        self._delimiterImageIndex = None
        super(OneLineMonthAndDayElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def draw4(self, drawer, resources, state, twoDigitsMonth=False, twoDigitsDay=False):
        assert(type(resources) == list)

        images = self._number.getImagesForNumber(resources, state.getTime().month, 2 if twoDigitsMonth else 1)

        if (self._delimiterImageIndex):
            images.append(resources[self._delimiterImageIndex])
        for image in self._number.getImagesForNumber(resources, state.getTime().day, 2 if twoDigitsDay else 1):
            images.append(image)

        from watchFaceParser.helpers.drawerHelper import DrawerHelper
        DrawerHelper.drawImages(drawer, images, uint2int(self._number.getSpacing()), self._number.getAlignment(), self._number.getBox())


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.common.numberElement import NumberElement
            self._number = NumberElement(parameter = parameter, parent = self, name = 'MonthAndDay')
            return self._number
        elif parameterId == 2:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._delimiterImageIndex = parameter.getValue() 
            return ValueElement(parameter = parameter, parent = self, name = 'DelimiterImageIndex')
        else:
            return super(OneLineMonthAndDayElement, self).createChildForParameter(parameter)
