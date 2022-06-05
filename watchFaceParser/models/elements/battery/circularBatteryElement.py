import logging

from watchFaceParser.models.elements.common.iconSetElement import IconSetElement


class CircularBatteryElement(IconSetElement):
    def __init__(self, parameter, parent, name = None):
        super(CircularBatteryElement, self).__init__(parameter = parameter, parent = parent, name = name)


    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        super(CircularBatteryElement, self).draw4(drawer, resources, state.getBatteryLevel(), 100)

