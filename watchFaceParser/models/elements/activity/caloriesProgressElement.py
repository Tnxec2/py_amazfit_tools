import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement

class CaloriesProgressElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._goalimage = None
        self._circle = None
        self._icon = None
        super(CaloriesProgressElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, images, state):
        goal = 200
        if self._goalimage:
            if state.getCalories() >= goal:
                self._goalimage.draw3(drawer, images, state)
        if self._icon:
            self._icon.draw4(drawer, images, state.getCalories(), goal)
        if self._circle:
            self._circle.draw4(drawer, images, state.getCalories(), goal)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.common.imageElement import ImageElement
            self._goalimage = ImageElement(parameter = parameter, parent = self, name = 'GoalImage')
            return self._goalimage
        elif parameterId == 2:
            from watchFaceParser.models.elements.common.imageSetElement import ImageSetElement
            self._icon = ImageSetElement(parameter = parameter, parent = self, name = 'Icons')
            return self._icon
        elif parameterId == 3:
            pass
        elif parameterId == 4:
            from watchFaceParser.models.elements.common.circularProgressElement import CircularProgressElement # temp.
            self._circle = CircularProgressElement(parameter = parameter, parent = self, name = 'Circle')
            return self._circle
        else:
            return super(CaloriesProgressElement, self).createChildForParameter(parameter)
