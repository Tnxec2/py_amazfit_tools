import logging

from watchFaceParser.models.elements.common.imageSetElement import ImageSetElement

class BatteryImageSetElement(ImageSetElement):
    def __init__(self, parameter, parent, name = None):
        super(BatteryImageSetElement, self).__init__(parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        super(BatteryImageSetElement, self).draw4(drawer, resources, state.getBatteryLevel(), 100)
