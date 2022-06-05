import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement


class ActivityAltElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._steps = None
        self._battery = None
        self._calories = None
        self._pulse = None
        self._batterySuffix = None
        self._unknown6ImageIndex = None
        self._distance = None
        self._icon1 = None
        self._icon2 = None
        self._icon3 = None
        self._icon4 = None
        self._icon5 = None
        super(ActivityAltElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, images, state):
        if self._battery:
            self._battery.draw5(drawer, images, state.getBatteryLevel(), suffix=self._batterySuffix)
        if self._pulse:
            self._pulse.draw4(drawer, images, state.getPulse())
        if self._steps:
            self._steps.draw4(drawer, images, state.getSteps())
        if self._calories:
            self._calories.draw4(drawer, images, state.getCalories())
        if self._distance:
            self._distance.draw3(drawer, images, state)
        if self._icon1:
            self._icon1.draw2(drawer, images)
        if self._icon2:
            self._icon2.draw2(drawer, images)
        if self._icon3:
            self._icon3.draw2(drawer, images)
        if self._icon4:
            self._icon4.draw2(drawer, images)
        if self._icon5:
            self._icon5.draw2(drawer, images)

    def createChildForParameter(self, parameter):
        from watchFaceParser.models.elements.common.numberExtendedElement import NumberExtendedElement
        parameterId = parameter.getId()
        if parameterId == 1:
            self._pulse = NumberExtendedElement(parameter = parameter, parent = self, name = 'Pulse')
            return self._pulse
        elif parameterId == 2:
            self._battery = NumberExtendedElement(parameter = parameter, parent = self, name = 'Battery')
            return self._battery
        elif parameterId == 3:
            self._calories = NumberExtendedElement(parameter = parameter, parent = self, name = 'Calories')
            return self._calories
        elif parameterId == 4:
            self._steps = NumberExtendedElement(parameter = parameter, parent = self, name = 'Steps')
            return self._steps
        elif parameterId == 5:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._batterySuffix = parameter.getValue() 
            return ValueElement(parameter, self, 'BatterySuffixImageIndex')
        elif parameterId == 6:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._unknown6ImageIndex = parameter.getValue() 
            return ValueElement(parameter, self, 'Unknow6ImageIndex')
        elif parameterId == 7:
            from watchFaceParser.models.elements.activity.distanceAltElement import DistanceAltElement
            self._distance = DistanceAltElement(parameter = parameter, parent = self, name = 'Distance')
            return self._distance
        elif parameterId == 10:
            from watchFaceParser.models.elements.common.imageElement import ImageElement
            self._icon1 = ImageElement(parameter = parameter, parent = self, name = 'Icon1')
            return self._icon1
        elif parameterId == 11:
            from watchFaceParser.models.elements.common.imageElement import ImageElement
            self._icon2 = ImageElement(parameter = parameter, parent = self, name = 'Icon2')
            return self._icon2
        elif parameterId == 12:
            from watchFaceParser.models.elements.common.imageElement import ImageElement
            self._icon3 = ImageElement(parameter = parameter, parent = self, name = 'Icon3')
            return self._icon3
        elif parameterId == 13:
            from watchFaceParser.models.elements.common.imageElement import ImageElement
            self._icon4 = ImageElement(parameter = parameter, parent = self, name = 'Icon4')
            return self._icon4
        elif parameterId == 14:
            from watchFaceParser.models.elements.common.imageElement import ImageElement
            self._icon5 = ImageElement(parameter = parameter, parent = self, name = 'Icon5')
            return self._icon5
        else:
            return super(ActivityAltElement, self).createChildForParameter(parameter)

