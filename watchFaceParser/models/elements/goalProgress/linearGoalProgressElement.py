import logging

from watchFaceParser.models.elements.common.iconSetElement import IconSetElement

class LinearGoalProgressElement(IconSetElement):
    def __init__(self, parameter, parent, name = None):
        super(LinearGoalProgressElement, self).__init__(parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        super(LinearGoalProgressElement, self).draw4(drawer, resources, state.getSteps(), state.getGoal())
