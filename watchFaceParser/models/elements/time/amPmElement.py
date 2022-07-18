from watchFaceParser.models.elements.common.coordinatesElement import CoordinatesElement
import logging


class AmPmElement(CoordinatesElement):
    def __init__(self, parameter, parent, name = None):
        self._imageIndexAmCn = None
        self._imageIndexPmCn = None
        self._imageIndexAmEn = None
        self._imageIndexPmEn = None
        super(AmPmElement, self).__init__(parameter = parameter, parent = parent, name = name)


    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        imageIndex = self._imageIndexAmEn if state.getTime().hour < 12 else self._imageIndexPmEn
        if not imageIndex:
            imageIndex = self._imageIndexAmCn if state.getTime().hour < 12 else self._imageIndexPmCn
        temp = resources[imageIndex].getBitmap()
        drawer.paste(temp, (self._x, self._y), temp)


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        from watchFaceParser.models.elements.basic.valueElement import ValueElement
        if parameterId == 3:
            self._imageIndexAmCn = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'ImageIndexAMCN')
        elif parameterId == 4:
            self._imageIndexPmCn = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'ImageIndexPMCN')
        if parameterId == 5:
            self._imageIndexAmEn = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'ImageIndexAMEN')
        elif parameterId == 6:
            self._imageIndexPmEn = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'ImageIndexPMEN')
        else:
            return super(AmPmElement, self).createChildForParameter(parameter)

