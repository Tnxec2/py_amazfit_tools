import logging

from watchFaceParser.models.elements.basic.compositeElement import CompositeElement


class FourDigitsElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._thousands = None
        self._hundreds = None
        self._tens = None
        self._ones = None
        super(FourDigitsElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def draw3(self, drawer, images, number):
        assert(type(images) == list)
        assert(type(number) == int)
        if number > 9999:
            number = number % 1000

        if self.getTens():
            self.getTens().draw3(drawer, images, int(number / 10))
        if self.getOnes():
            self.getOnes().draw3(drawer, images, int(number % 10))


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()

        if parameterId == 1:
            from watchFaceParser.models.elements.common.imageSetElement import ImageSetElement
            self._thousands = ImageSetElement(parameter, self, 'Thousands')
            return self._thousands
        elif parameterId == 2:
            from watchFaceParser.models.elements.common.imageSetElement import ImageSetElement
            self._hundreds = ImageSetElement(parameter, self, 'Hundreds')
            return self._hundreds
        if parameterId == 3:
            from watchFaceParser.models.elements.common.imageSetElement import ImageSetElement
            self._tens = ImageSetElement(parameter, self, 'Tens')
            return self._tens
        elif parameterId == 4:
            from watchFaceParser.models.elements.common.imageSetElement import ImageSetElement
            self._ones = ImageSetElement(parameter, self, 'Ones')
            return self._ones
        else:
            super(FourDigitsElement, self).createChildForParameter(parameter)
