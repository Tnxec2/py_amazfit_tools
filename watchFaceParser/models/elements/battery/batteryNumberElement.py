from watchFaceParser.models.elements.basic.compositeElement import CompositeElement


class BatteryNumberElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._number = None
        super(BatteryNumberElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        images = self._number.getImagesForNumber(resources, state.getBatteryLevel())

        from watchFaceParser.helpers.drawerHelper import DrawerHelper
        DrawerHelper.drawImages(drawer, images, self._number.getSpacing(), self._number.getAlignment(), self._number.getBox())

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()

        if parameterId == 1:
            from watchFaceParser.models.elements.common.numberElement import NumberElement
            self._number = NumberElement(parameter, self, 'Number')
            return self._number
        else:
            super(BatteryNumberElement, self).createChildForParameter(parameter)
