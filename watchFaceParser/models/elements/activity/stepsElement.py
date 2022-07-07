import logging

from watchFaceParser.models.elements.basic.compositeElement import CompositeElement

class StepsElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._step = None
        self._prefixImageIndex = None

        super(StepsElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def getStep(self):
        return self._step

    def draw3(self, drawer, resources, state):
        images = []
        if self._prefixImageIndex:
            images.append(resources[self._prefixImageIndex])
        for image in self._step.getImagesForNumber(resources, state.getSteps()):
            images.append(image)

        from watchFaceParser.helpers.drawerHelper import DrawerHelper
        DrawerHelper.drawImages(drawer, images, self.getStep().getSpacing(), self.getStep().getAlignment(), self.getStep().getBox())

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()

        if parameterId == 1:
            from watchFaceParser.models.elements.common.numberElement import NumberElement
            self._step = NumberElement(parameter, self, 'Number')
            return self._step
        elif parameterId == 2:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._prefixImageIndex = parameter.getValue()
            return ValueElement(parameter, self, 'PrefixImageIndex')
        else:
            super(StepsElement, self).createChildForParameter(parameter)
