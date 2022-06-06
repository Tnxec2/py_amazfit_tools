import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement

class PaiProgressElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._circle = None

        super(PaiProgressElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, images, state):
        if self._circle:
            self._circle.draw4(drawer, images, state.getPai(), 100)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.common.circularProgressElement import CircularProgressElement # temp.
            self._circle = CircularProgressElement(parameter = parameter, parent = self, name = 'Circle')
            return self._circle
        else:
            return super(PaiProgressElement, self).createChildForParameter(parameter)
