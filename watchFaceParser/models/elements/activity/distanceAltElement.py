import logging

from watchFaceParser.models.elements.basic.compositeElement import CompositeElement
from watchFaceParser.utils.parametersConverter import uint2int


class DistanceAltElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._number = None
        self._suffixImageIcon = None
        self._decimalPointImageIndex = None
        super(DistanceAltElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        kilometers = int(state.getDistance() / 1000)
        decimals = int(state.getDistance() % 1000 / 10)

        images = self._number.getImagesForNumber(resources, kilometers)
        if self._decimalPointImageIndex:
            images.append(resources[self._decimalPointImageIndex])
        for image in self._number.getImagesForNumber(resources, decimals):
            images.append(image)

        from watchFaceParser.helpers.drawerHelper import DrawerHelper
        DrawerHelper.drawImages(drawer, images, uint2int(self._number.getSpacing()), self._number.getAlignment(), self._number.getBox(), self._number.getVerticalOffset())

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.common.numberExtendedElement import NumberExtendedElement
            self._number = NumberExtendedElement(parameter, self, 'Number')
            return self._number
        elif parameterId == 2:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._decimalPointImageIndex = parameter.getValue()
            return ValueElement(parameter, self, 'DecimalPointerImageIndex')
        elif parameterId == 3:
            from watchFaceParser.models.elements.common.imageElement import ImageElement
            self._suffixImageIcon = ImageElement(parameter, self, 'SuffixKMIcon')
            return self._suffixImageIcon
        else:
            super(DistanceAltElement, self).createChildForParameter(parameter)
