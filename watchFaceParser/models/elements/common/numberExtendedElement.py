import logging

from watchFaceParser.models.elements.common.coordinatesElement import CoordinatesElement
from watchFaceParser.helpers.drawerHelper import DrawerHelper
from watchFaceParser.utils.parametersConverter import uint2int

class Box:
    def __init__(self, x, y, width, height):
        self._x = x
        self._y = y
        self._width = width
        self._height = height


    def getX(self):
        return self._x


    def getY(self):
        return self._y


    def getWidth(self):
        return self._width


    def getHeight(self):
        return self._height


    def getLeft(self):
        return self._x


    def getRight(self):
        return self._x + self._width


    def getTop(self):
        return self._y


    def getBottom(self):
        return self._y + self._height


class NumberExtendedElement(CoordinatesElement):
    def __init__(self, parameter, parent, name):
        self._bottomRightX = None
        self._bottomRightY = None
        self._alignment = None
        self._spacing = None
        self._verticaloffset = None
        self._imageIndex = None
        self._imagesCount = None
        super(NumberExtendedElement, self).__init__(parameter = parameter, parent = parent, name = name)


    def getBottomRightX(self):
        return self._bottomRightX or 0


    def getBottomRightY(self):
        return self._bottomRightY or 0


    def getAlignment(self):
        return self._alignment or 0


    def getSpacing(self):
        return self._spacing or 0


    def getImageIndex(self):
        return self._imageIndex or 0


    def getImagesCount(self):
        return self._imagesCount or 1

    def getVerticalOffset(self):
        return self._verticaloffset or 0


    def getBox(self):
        return Box(self.getX(), self.getY(), self.getBottomRightX() - self.getX(), self.getBottomRightY() - self.getY())


    def getAltBox(self, altCoordinates):
        return Box(altCoordinates.getX(), altCoordinates.getY(), self.getBottomRightX() - self.getX(), self.getBottomRightY() - self.getY())


    def draw5(self, drawer, resources, number, minimumDights = 1, suffix = None):
        if suffix is None:
            return self.draw4(drawer, resources, number, minimumDights)
        images = self.getImagesForNumber(resources, number)
        images.append(resources[suffix])
        DrawerHelper.drawImages(drawer, images, uint2int(self.getSpacing()), self.getAlignment(), self.getBox(), self.getVerticalOffset())
        
    def draw4(self, drawer, images, number, minimumDights = 1):
        DrawerHelper.drawImages(drawer, self.getImagesForNumber(images, number, minimumDights), self.getSpacing(), self.getAlignment(), self.getBox(), self.getVerticalOffset())


    def getImagesForNumber(self, images, number, minimumDigits = 1):
        stringNumber = str(number).zfill(minimumDigits)
        return [images[self.getImageIndex() + int(digit)] for digit in stringNumber if int(digit) < self.getImagesCount()]


    def createChildForParameter(self, parameter):
        from watchFaceParser.models.elements.basic.valueElement import ValueElement

        parameterId = parameter.getId()
        if parameterId == 3:
            self._bottomRightX = parameter.getValue() 
            return ValueElement(parameter, self, 'BottomRightX')
        elif parameterId == 4:
            self._bottomRightY = parameter.getValue() 
            return ValueElement(parameter, self, 'BottomRightY')
        elif parameterId == 5:
            self._alignment = parameter.getValue() 
            return ValueElement(parameter, self, 'Alignment')
        elif parameterId == 6:
            self._spacing = parameter.getValue() 
            return ValueElement(parameter, self, 'Spacing')
        elif parameterId == 7:
            self._verticaloffset = parameter.getValue() 
            return ValueElement(parameter, self, 'VerticalOffset')
        elif parameterId == 8:
            self._imageIndex = parameter.getValue() 
            return ValueElement(parameter, self, 'ImageIndex')
        elif parameterId == 9:
            self._imagesCount = parameter.getValue()
            return ValueElement(parameter, self, 'ImagesCount')
        else:
            super(NumberExtendedElement, self).createChildForParameter(parameter)

