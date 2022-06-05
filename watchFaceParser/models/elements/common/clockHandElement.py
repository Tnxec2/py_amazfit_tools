import logging
import math
from watchFaceParser.models.elements.basic.compositeElement import CompositeElement
from watchFaceParser.models.elements.basic.valueElement import ValueElement
from watchFaceParser.config import Config

class ClockHandElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._onlyBorder = False
        self._color = None
        self._center = None
        self._shape = []
        self._centerImage = None
        super(ClockHandElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def draw4(self, drawer, resources, value, total):
        assert(type(resources) == list)

        angle = 90 - (value * 360 / total)

        from PIL import Image, ImageDraw
        
        temp = Image.new('RGBA', (Config.getImageSize(), Config.getImageSize()))
        poly = ImageDraw.Draw(temp)

        # set shape to center
        centered_rotated_shape = []
        if self._center:
            for sh in self._shape:
                (x, y) = (self._center.getX() + sh.getX(), self._center.getY() + sh.getY())
                centered_rotated_shape.append((x, y))

        fill=(None if self._onlyBorder else self._color)
        coords = tuple(centered_rotated_shape)
        poly.polygon(coords, fill=fill, outline=self._color)
        temp = temp.rotate(angle, expand=True, center=(self._center.getX(), self._center.getY()))
        (nw, nh) = (temp.size[0], temp.size[1])
        (dw, dh) = (drawer.size[0], drawer.size[1])
        drawer.paste(temp, ( int(dw/2 - nw/2), int(dh/2 - nh/2)), temp)


        if self._centerImage:
            self._centerImage.draw2(drawer, resources)


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            self._onlyBorder = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'OnlyBorder')
        elif parameterId == 2:
            from resources.image.color import Color
            self._color = Color.fromArgb(0xff000000 | parameter.getValue())
            return ValueElement(parameter = parameter, parent = self, name = 'Color')
        elif parameterId == 3:
            from watchFaceParser.models.elements.common.coordinatesElement import CoordinatesElement
            self._center = CoordinatesElement(parameter = parameter, parent = self, name = 'Center')
            return self._centerImage
        elif parameterId == 4:
            from watchFaceParser.models.elements.common.coordinatesElement import CoordinatesElement
            self._shape.append(CoordinatesElement(parameter, self, 'Shape'))
            return CoordinatesElement(parameter, self, 'Shape')
        elif parameterId == 5:
            from watchFaceParser.models.elements.common.imageElement import ImageElement
            self._centerImage = ImageElement(parameter = parameter, parent = self, name = 'CenterImage')
            return self._centerImage
        else:
            return super(ClockHandElement, self).createChildForParameter(parameter)
