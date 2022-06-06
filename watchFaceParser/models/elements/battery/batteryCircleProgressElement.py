import logging

from watchFaceParser.models.elements.common.circularProgressElement import CircularProgressElement

class BatteryCircleProgressElement(CircularProgressElement):
    def __init__(self, parameter, parent, name = None):
        super(BatteryCircleProgressElement, self).__init__(parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        super(BatteryCircleProgressElement, self).draw4(drawer, resources, state.getBatteryLevel() , 100)
