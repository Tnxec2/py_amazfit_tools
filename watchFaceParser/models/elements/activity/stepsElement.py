import logging

from watchFaceParser.models.elements.basic.compositeElement import CompositeElement

class StepsElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._step = None
        super(StepsElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def getStep(self):
        return self._step

    def draw3(self, drawer, resources, state):
        images = self.getStep().getImagesForNumber(resources, state.getSteps())

        from watchFaceParser.helpers.drawerHelper import DrawerHelper
        DrawerHelper.drawImages(drawer, images, self.getStep().getSpacing(), self.getStep().getAlignment(), self.getStep().getBox())

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()

        if parameterId == 1:
            from watchFaceParser.models.elements.common.numberElement import NumberElement
            self._step = NumberElement(parameter, self, 'Number')
            return self._step
        else:
            super(StepsElement, self).createChildForParameter(parameter)
