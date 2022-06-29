from watchFaceParser.elements.basicElements.number import Number
from watchFaceParser.elements.basicElements.image import Image
from watchFaceParser.elements.basicElements.imageSet import ImageSet


class AQI:
    definitions = {
        1: { 'Name': 'Number', 'Type': Number},
        2: { 'Name': 'IconProgress', 'Type': ImageSet},
        4: { 'Name': 'Icon', 'Type': Image},
        5: { 'Name': 'IconCH', 'Type': Image},
        6: { 'Name': 'IconCN', 'Type': Image},
    }

