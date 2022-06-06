from watchFaceParser.models.elements.basic.compositeElement import CompositeElement


class BatteryNumberElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._number = None
        self._circle = None
        self._suffix = None
        super(BatteryNumberElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        images = self._number.getImagesForNumber(resources, state.getBatteryLevel())
        if self._suffix:
            images.append(resources[self._suffix])
        from watchFaceParser.helpers.drawerHelper import DrawerHelper
        DrawerHelper.drawImages(drawer, images, self._number.getSpacing(), self._number.getAlignment(), self._number.getBox())

        if self._circle:
            self._circle.draw4(drawer, resources, state.getBatteryLevel(), 100)

    def createChildForParameter(self, parameter):
        from watchFaceParser.models.elements.basic.valueElement import ValueElement
        parameterId = parameter.getId()

        if parameterId == 1:
            from watchFaceParser.models.elements.common.numberElement import NumberElement
            self._number = NumberElement(parameter, self, 'Number')
            return self._number
        elif parameterId == 2:
            from watchFaceParser.models.elements.battery.batteryCircleProgressElement import BatteryCircleProgressElement
            self._circle = BatteryCircleProgressElement(parameter = parameter, parent = self, name = 'Circle')
            return self._circle
        elif parameterId == 4:
            self._suffix = parameter.getValue()
            return ValueElement(parameter, self, 'SuffixImageIndex')
        else:
            super(BatteryNumberElement, self).createChildForParameter(parameter)
