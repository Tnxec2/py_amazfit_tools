
import logging
from watchFaceParser.models.elements.basic.compositeElement import CompositeElement


class AqiElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._number = None
        self._icon = None
        super(AqiElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        if self._number:
            self._number.draw4(drawer, resources, state.getAqi())
        if self._icon:
            self._icon.draw3(drawer, resources)

    def createChildForParameter(self, parameter):
        from watchFaceParser.models.elements.basic.valueElement import ValueElement
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.common.numberElement import NumberElement
            self._number = NumberElement(parameter = parameter, parent = self, name = 'Number')
            return self._number
        elif parameterId == 2:
            from watchFaceParser.models.elements.common.imageElement import ImageElement
            self._icon = ImageElement(parameter = parameter, parent = self, name = 'Icon')
            return self._icon
        else:
            return super(AqiElement, self).createChildForParameter(parameter)
