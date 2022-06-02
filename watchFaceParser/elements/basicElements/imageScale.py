
from watchFaceParser.elements.basicElements.coordinates import Coordinates


class ImageScale:
    definitions = {
        1: { 'Name': 'StartImageIndex', 'Type': 'long'},
        2: { 'Name': 'Segments', 'Type': [Coordinates]},
    }

