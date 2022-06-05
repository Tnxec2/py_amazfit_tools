import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement

class PulseStatusElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._image1 = None
        self._image2 = None
        self._image3 = None
        self._image4 = None
        self._image5 = None
        self._image6 = None
        super(PulseStatusElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        pulse = state.getPulse()
        if pulse <= 86:
            if self._image1:
                self._image1.draw2(drawer, resources)
        elif pulse <= 106:
            if self._image2:
                self._image2.draw2(drawer, resources)
        elif pulse <= 130:
            if self._image3:
                self._image3.draw2(drawer, resources)
        elif pulse <= 150:
            if self._image4:
                self._image4.draw2(drawer, resources)
        elif pulse <= 170:
            if self._image5:
                self._image5.draw2(drawer, resources)
        else:
            if self._image6:
                self._image6.draw2(drawer, resources)


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.common.imageElement import ImageElement
            self._image1 = ImageElement(parameter = parameter, parent = self, name = 'Image1')
            return self._image1
        elif parameterId == 2:
            from watchFaceParser.models.elements.common.imageElement import ImageElement
            self._image2 = ImageElement(parameter = parameter, parent = self, name = 'Image2')
            return self._image3
        elif parameterId == 3:
            from watchFaceParser.models.elements.common.imageElement import ImageElement
            self._image3 = ImageElement(parameter = parameter, parent = self, name = 'Image3')
            return self._image3
        elif parameterId == 4:
            from watchFaceParser.models.elements.common.imageElement import ImageElement
            self._image4 = ImageElement(parameter = parameter, parent = self, name = 'Image4')
            return self._image4
        elif parameterId == 5:
            from watchFaceParser.models.elements.common.imageElement import ImageElement
            self._image5 = ImageElement(parameter = parameter, parent = self, name = 'Image5')
            return self._image5
        elif parameterId == 6:
            from watchFaceParser.models.elements.common.imageElement import ImageElement
            self._image6 = ImageElement(parameter = parameter, parent = self, name = 'Image6')
            return self._image6
        else:
            return super(PulseStatusElement, self).createChildForParameter(parameter)