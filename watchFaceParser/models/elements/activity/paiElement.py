from watchFaceParser.models.elements.basic.compositeElement import CompositeElement
from watchFaceParser.models.elements.common.numberElement import NumberElement
from watchFaceParser.models.elements.common.imageElement import ImageElement

class PaiElement(CompositeElement):
    def __init__(self, parameter, parent = None, name = None):
        
        self._image1 = None
        self._image2 = None
        self._image3 = None
        self._number4 = None
        self._number5 = None
        self._number6 = None
        self._nodata = None
        self._number11 = None
        super(PaiElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        if (state.getPAI() < 50):
            if self._image1:
                self._image1.draw2(drawer, resources)
            if self._number4:
                self._number4.draw4(drawer, resources, state.getPAI())
        elif (state.getPAI() < 70):
            if self._image2:
                self._image2.draw2(drawer, resources)
            if self._number5:
                self._number5.draw4(drawer, resources, state.getPAI())
        else:
            if self._image3:
                self._image3.draw2(drawer, resources)
            if self._number6:
                self._number6.draw4(drawer, resources, state.getPAI())

        if (self._number11):
            images = self._number11.getImagesForNumber(resources, state.getPAI())
            from watchFaceParser.helpers.drawerHelper import DrawerHelper
            DrawerHelper.drawImages(drawer, images, self._number11.getSpacing(), self._number11.getAlignment(), self._number11.getBox())

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()

        if parameterId == 1:
            self._image1 = ImageElement(parameter, self, 'IconLow')
            return self._image1
        elif parameterId == 2:
            self._image2 = ImageElement(parameter, self, 'IconNormal')
            return self._image2
        elif parameterId == 3:
            self._image3 = ImageElement(parameter, self, 'IconHigh')
            return self._image3
        elif parameterId == 4:
            self._number4 = NumberElement(parameter, self, 'NumberLow')
            return self._number4
        elif parameterId == 5:
            self._number5 = NumberElement(parameter, self, 'NumberNormal')
            return self._number5
        elif parameterId == 6:
            self._number6 = NumberElement(parameter, self, 'NumberHigh')
            return self._number6
        elif parameterId == 7:
            self._nodata = ImageElement(parameter, self, 'NoDataImage')
            return self._nodata
        elif parameterId == 11:
            self._number11 = NumberElement(parameter, self, 'NumberGeneric')
            return self._number11
        else:
            super(PaiElement, self).createChildForParameter(parameter)
