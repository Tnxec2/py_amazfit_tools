import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement


class OneLineElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._number = None
        self._minus_image_index = None
        self._delimiter_image_index = None
        self._degrees_image_index = None
        self._append_degres_for_both = None
        super(OneLineElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        
        if self._number:
            images = []
            min = state.getCurrentTemperature()-7
            max = state.getCurrentTemperature()+7
            if min < 0 and self._minus_image_index:
                images.append(resources[self._minus_image_index])
            for image in self._number.getImagesForNumber(resources, abs(min)):
                images.append(image)
            if self._degrees_image_index and self._append_degres_for_both:
                images.append(resources[self._degrees_image_index])
            if self._delimiter_image_index:
                images.append(resources[self._delimiter_image_index])
            if max < 0 and self._minus_image_index:
                images.append(resources[self._minus_image_index])
            for image in self._number.getImagesForNumber(resources, abs(max)):
                images.append(image)
            if self._degrees_image_index:
                images.append(resources[self._degrees_image_index])

            from watchFaceParser.helpers.drawerHelper import DrawerHelper
            DrawerHelper.drawImages(drawer, images, self._number.getSpacing(), self._number.getAlignment(), self._number.getBox())

    def createChildForParameter(self, parameter):
        from watchFaceParser.models.elements.basic.valueElement import ValueElement
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.common.numberElement import NumberElement
            self._customicon = NumberElement(parameter = parameter, parent = self, name = 'Number')
            return self._weekDay
        elif parameterId == 2:
            self._minus_image_index = parameter.getValue()
            return ValueElement(parameter, self, 'MinusSignImageIndex')
        elif parameterId == 3:
            self._delimiter_image_index = parameter.getValue()
            return ValueElement(parameter, self, 'DelimiterImageIndex')
        elif parameterId == 4:
            self._append_degres_for_both = parameter.getValue()
            return ValueElement(parameter, self, 'AppendDegresForBoth')
        elif parameterId == 5:
            self._degrees_image_index = parameter.getValue()
            return ValueElement(parameter, self, 'DegreesImageIndex')
        else:
            return super(OneLineElement, self).createChildForParameter(parameter)
