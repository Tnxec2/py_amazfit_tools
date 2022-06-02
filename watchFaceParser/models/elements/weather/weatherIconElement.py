
from watchFaceParser.models.elements.basic.containerElement import ContainerElement

class WeatherIconElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._customicon = None
        super(WeatherIconElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, images, state):
        if self._customicon:
            self._customicon.draw3(drawer, images, state.getCurrentWeather() or 0)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            pass
        elif parameterId == 2:
            from watchFaceParser.models.elements.common.imageSetElement import ImageSetElement
            self._customicon = ImageSetElement(parameter = parameter, parent = self, name = 'CustomIcon')
            return self._customicon
        else:
            return super(WeatherIconElement, self).createChildForParameter(parameter)
