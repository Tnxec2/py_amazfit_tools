from watchFaceParser.elements.basicElements.coordinates import Coordinates
from watchFaceParser.elements.basicElements.imageSet import ImageSet

class WeatherIcon:
    definitions = {
        1: { 'Name': 'Unknown1', 'Type': 'long?'},
        2: { 'Name': 'CustomIcon', 'Type': ImageSet},
        3: { 'Name': 'UnknownCoords3', 'Type': Coordinates}, # TODO: zepp 2UTgO1V4APZpnGAvWcP50ca3wODjloDYbeqZ6i9J
        4: { 'Name': 'UnknownCoords4', 'Type': Coordinates}, # TODO: zepp 2UTgO1V4APZpnGAvWcP50ca3wODjloDYbeqZ6i9J
    }

