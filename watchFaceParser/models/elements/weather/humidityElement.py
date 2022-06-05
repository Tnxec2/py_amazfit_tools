
import logging
from watchFaceParser.models.elements.basic.compositeElement import CompositeElement
from watchFaceParser.utils.parametersConverter import uint2int

class HumidityElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._number = None
        self._suffix = None
        self._icon = None
        super(HumidityElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        if self._number:
            images = self._number.getImagesForNumber(resources, state.getHumidity())
            if self.getSuffixImageIndex():
                images.append(resources[self.getSuffixImageIndex()])

            from watchFaceParser.helpers.drawerHelper import DrawerHelper
            DrawerHelper.drawImages(drawer, images, uint2int(self._number.getSpacing()), self._number.getAlignment(), self._number.getBox())

        if self._icon:
            self._icon.draw3(drawer, resources)

    def createChildForParameter(self, parameter):
        from watchFaceParser.models.elements.basic.valueElement import ValueElement
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.common.numberElement import NumberElement
            self._number = NumberElement(parameter = parameter, parent = self, name = 'Number')
            return self._number
        elif parameterId == 2:
            self._suffix = parameter.getValue()
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            return ValueElement(parameter, self, '?SuffixImageIndex?')
        elif parameterId == 3:
            from watchFaceParser.models.elements.common.imageElement import ImageElement
            self._icon = ImageElement(parameter = parameter, parent = self, name = 'Icon')
            return self._icon
        else:
            return super(HumidityElement, self).createChildForParameter(parameter)
