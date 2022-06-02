
from watchFaceParser.elements.basicElements.coordinates import Coordinates


class IconSet:
    definitions = {
        1: { 'Name': 'StartImageIndex', 'Type': 'long'},
        2: { 'Name': 'Segments', 'Type': [Coordinates]},
    }

