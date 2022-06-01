
from watchFaceParser.elements.basicElements.coordinates import Coordinates
from watchFaceParser.elements.basicElements.image import Image
from watchFaceParser.models.color import Color

class ClockHand:
    definitions = {
        1: { 'Name': 'OnlyBorder', 'Type': 'bool'},
        2: { 'Name': 'Color', 'Type': Color},
        3: { 'Name': 'Center', 'Type': Coordinates},
        4: { 'Name': 'Shape', 'Type': [Coordinates]},
        5: { 'Name': 'CenterImage', 'Type': Image},
    }

