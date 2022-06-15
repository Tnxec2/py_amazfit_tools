import logging
from watchFaceParser.models.elements.basic.compositeElement import CompositeElement
from watchFaceParser.models.elements.common.imageElement import ImageElement


class LinearIconSetElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._startImageIndex = None
        self._segments = []
        super(LinearIconSetElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def draw4(self, drawer, resources, number, goal):
        assert(type(resources) == list)
        assert(type(number) == int)
        assert(type(goal) == int)
        end = int(number / (goal / len(self._segments) ))
        if end > len(self._segments):
            end = len(self._segments) 
        
        for i in range(end):
            if self._startImageIndex+i >= len(resources):    # BipS draw only exist images
                return
            image = resources[self._startImageIndex+i]
            x = self._segments[i].getX()
            y = self._segments[i].getY()
            temp = image.getBitmap()
            drawer.paste(temp, (x, y), temp)


    def createChildForParameter(self, parameter):
        if parameter.getId() == 1:
            self._startImageIndex = parameter.getValue()
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            return ValueElement(parameter, self, 'StartImageIndex')
        elif parameter.getId() == 2:
            from watchFaceParser.models.elements.common.coordinatesElement import CoordinatesElement
            self._segments.append(CoordinatesElement(parameter, self, 'Segments'))
            return CoordinatesElement(parameter, self, 'Segments')
        else:
            super(LinearIconSetElement, self).createChildForParameter(parameter)

