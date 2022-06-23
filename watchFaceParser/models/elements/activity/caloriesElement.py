from watchFaceParser.models.elements.basic.compositeElement import CompositeElement

class CaloriesElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._number = None
        self._prefixImageIndex = None
        super(CaloriesElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        images = []
        if self._prefixImageIndex:
            images.append(resources[self._prefixImageIndex])
        for image in self._number.getImagesForNumber(resources, state.getCalories()):
            images.append(image)

        from watchFaceParser.helpers.drawerHelper import DrawerHelper
        DrawerHelper.drawImages(drawer, images, self._number.getSpacing(), self._number.getAlignment(), self._number.getBox())

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()

        if parameterId == 1:
            from watchFaceParser.models.elements.common.numberElement import NumberElement
            self._number = NumberElement(parameter, self, 'Number')
            return self._number
        elif parameterId == 2:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._prefixImageIndex = parameter.getValue()
            return ValueElement(parameter, self, 'PrefixImageIndex')
        else:
            super(CaloriesElement, self).createChildForParameter(parameter)
