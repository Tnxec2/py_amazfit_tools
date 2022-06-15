import logging

from watchFaceParser.models.elements.common.linearIconSetElement import LinearIconSetElement

class BatteryIconSetElement(LinearIconSetElement):
    def __init__(self, parameter, parent, name = None):
        super(BatteryIconSetElement, self).__init__(parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        super(BatteryIconSetElement, self).draw4(drawer, resources, state.getBatteryLevel(), 100)
