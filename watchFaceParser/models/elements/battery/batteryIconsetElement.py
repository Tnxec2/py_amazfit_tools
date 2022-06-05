import logging

from watchFaceParser.models.elements.common.iconSetElement import IconSetElement

class BatteryIconSetElement(IconSetElement):
    def __init__(self, parameter, parent, name = None):
        super(BatteryIconSetElement, self).__init__(parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        super(BatteryIconSetElement, self).draw3(drawer, resources, int(state.getBatteryLevel() * self.getImagesCount() / 100))
