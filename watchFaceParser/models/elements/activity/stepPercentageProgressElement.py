from watchFaceParser.models.elements.basic.compositeElement import CompositeElement

class StepPercentageProgressElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._number = None
        self._suffixImageIndex = None
        super(StepPercentageProgressElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        images = []

        procentageValue = int(state.getSteps() / (state.getGoal() / 100))

        for image in self._number.getImagesForNumber(resources, procentageValue):
            images.append(image)
        if self._suffixImageIndex:
            images.append(resources[self._suffixImageIndex])
            
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
            self._suffixImageIndex = parameter.getValue()
            return ValueElement(parameter, self, 'SuffixImageIndex')
        else:
            super(StepPercentageProgressElement, self).createChildForParameter(parameter)
