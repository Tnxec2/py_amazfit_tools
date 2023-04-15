
import logging
from watchFaceParser.models.elements.basic.compositeElement import CompositeElement


class TemperatureNumberElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._number = None
        self._minusImageIndex = None
        self._degreesImageIndex = None
        super(TemperatureNumberElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def draw3(self, drawer, resources, number):
        assert(type(resources) == list)
        if self._number:
            
            images = []
            
            if number < 0 and self._minusImageIndex:
                images.append(resources[self._minusImageIndex])
            for image in self._number.getImagesForNumber(resources, abs(number)):
                images.append(image)
            if self._degreesImageIndex:
                images.append(resources[self._degreesImageIndex])

            from watchFaceParser.helpers.drawerHelper import DrawerHelper
            DrawerHelper.drawImages(drawer, images, self._number.getSpacing(), self._number.getAlignment(), self._number.getBox())

    def createChildForParameter(self, parameter):
        from watchFaceParser.models.elements.basic.valueElement import ValueElement
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.common.numberElement import NumberElement
            self._number = NumberElement(parameter = parameter, parent = self, name = 'Number')
            return self._number
        elif parameterId == 2:
            self._minusImageIndex = parameter.getValue() 
            return ValueElement(parameter, self, 'MinusImageIndex')
        elif parameterId == 3:
            self._degreesImageIndex = parameter.getValue() 
            return ValueElement(parameter, self, 'DegreesImageIndex')
        else:
            return super(TemperatureNumberElement, self).createChildForParameter(parameter)
