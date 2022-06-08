import logging
from watchFaceParser.models.elements.basic.compositeElement import CompositeElement
from watchFaceParser.models.elements.common.imageElement import ImageElement


class IconSetElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._imageIndex = None
        self._imagesCount = None
        self._x = None
        self._y = None
        super(IconSetElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getImagesCount(self):
        return self._imagesCount or 1
        
    def getX(self):
        return self._x or 0

    def getY(self):
        return self._y or 0


    def draw4(self, drawer, resources, value, total):
        index = int(value / ( total / self._imagesCount))
        self.draw3(drawer, resources, index)

    def draw3(self, drawer, resources, index):
        assert(type(resources) == list)
        assert(type(index) == int)
        if index >= self.getImagesCount():
            index = int(self.getImagesCount()) - 1
        imageIndex = int(self._imageIndex + index)
        temp = resources[imageIndex].getBitmap()

        drawer.paste(temp, (self.getX(), self.getY()), temp)


    def createChildForParameter(self, parameter):
        if parameter.getId() == 3:
            self._imageIndex = parameter.getValue()
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            return ValueElement(parameter, self, 'StartImageIndex')
        elif parameter.getId() == 1:
            self._x = parameter.getValue()
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            return ValueElement(parameter, self, 'X')
        elif parameter.getId() == 2:
            self._y = parameter.getValue()
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            return ValueElement(parameter, self, 'Y')
        elif parameter.getId() == 4:
            self._imagesCount = parameter.getValue()
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            return ValueElement(parameter, self, 'ImagesCount')
        else:
            super(IconSetElement, self).createChildForParameter(parameter)

