import logging

from watchFaceParser.models.elements.common.linearIconSetElement import LinearIconSetElement

class BatteryLinearIconSetElement(LinearIconSetElement):
    def __init__(self, parameter, parent, name = None):
        super(BatteryLinearIconSetElement, self).__init__(parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        super(BatteryLinearIconSetElement, self).draw4(drawer, resources, state.getBatteryLevel(), 100)
