import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement

class StepsProgressElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._goalimage = None
        self._linear = None
        self._gauge = None
        self._circle = None
        super(StepsProgressElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, images, state):
        if self._goalimage:
            if state.getSteps() >= state.getGoal():
                self._goalimage.draw3(drawer, images, state)
        if self._linear:
            self._linear.draw4(drawer, images, state.getSteps(), state.getGoal())
        if self._gauge:
            self._gauge.draw3(drawer, images, state)
        if self._circle:
            self._circle.draw3(drawer, images, state)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.common.imageElement import ImageElement
            self._goalimage = ImageElement(parameter = parameter, parent = self, name = 'GoalImage')
            return self._goalimage
        elif parameterId == 2:
            from watchFaceParser.models.elements.common.iconSetElement import IconSetElement
            self._linear = IconSetElement(parameter = parameter, parent = self, name = 'Linear')
            return self._linear
        elif parameterId == 3:
            from watchFaceParser.models.elements.goalProgress.stepGaugeElement import StepGaugeElement
            self._gauge = StepGaugeElement(parameter = parameter, parent = self, name = 'Gauge')
            return self._gauge
        elif parameterId == 4:
            from watchFaceParser.models.elements.goalProgress.circularGoalProgressElement import CircularGoalProgressElement # temp.
            self._circle = CircularGoalProgressElement(parameter = parameter, parent = self, name = 'Circle')
            return self._circle
        else:
            return super(StepsProgressElement, self).createChildForParameter(parameter)
