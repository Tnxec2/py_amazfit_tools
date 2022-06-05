import logging

from watchFaceParser.models.elements.common.linearIconSetElement import LinearIconSetElement

class StepGaugeElement(LinearIconSetElement):
    def __init__(self, parameter, parent, name = None):
        super(StepGaugeElement, self).__init__(parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        super(StepGaugeElement, self).draw4(drawer, resources, state.getSteps(), state.getGoal())

