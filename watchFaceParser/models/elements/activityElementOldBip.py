import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement


class ActivityElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._stepsGoal = None
        self._steps = None
        self._distance = None
        self._pulse = None
        self._calories = None

        super(ActivityElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getStepsGoal(self):
        return self._stepsGoal


    def getSteps(self):
        return self._steps


    def getDistance(self):
        return self._distance


    def getPulse(self):
        return self._pulse


    def getCalories(self):
        return self._calories

    def draw3(self, drawer, images, state):
        if self._steps:
            self._steps.draw4(drawer, images, state.getSteps())
        if self._stepsGoal:
            self._stepsGoal.draw4(drawer, images, state.getGoal())
        if self._calories:
            self._calories.draw4(drawer, images, state.getCalories())
        if self._pulse:
            self._pulse.draw4(drawer, images, state.getPulse())
        if self._distance:
            self._distance.draw3(drawer, images, state)

    def createChildForParameter(self, parameter):
        from watchFaceParser.models.elements.common.numberElement import NumberElement
        parameterId = parameter.getId()
        if parameterId == 1:
            self._steps = NumberElement(parameter = parameter, parent = self, name = '?Steps?')
            return self._steps
        elif parameterId == 2:
            self._stepsGoal = NumberElement(parameter = parameter, parent = self, name = '?StepsGoal?')
            return self._stepsGoal
        elif parameterId == 3:
            self._calories = NumberElement(parameter = parameter, parent = self, name = '?Calories?')
            return self._calories
        elif parameterId == 4:
            self._pulse = NumberElement(parameter = parameter, parent = self, name = '?Pulse?')
            return self._pulse
        elif parameterId == 5:
            from watchFaceParser.models.elements.activity.distanceElement import DistanceElement
            self._distance = DistanceElement(parameter = parameter, parent = self, name = '?DistanceElement?')
            return self._distance
        else:
            return super(ActivityElement, self).createChildForParameter(parameter)

