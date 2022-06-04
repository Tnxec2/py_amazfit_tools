from watchFaceParser.elements.basicElements.number import Number
from watchFaceParser.elements.basicElements.image import Image


class Humidity:
    definitions = {
        1: { 'Name': 'Number', 'Type': Number},
        2: { 'Name': 'SuffixImageIndex', 'Type': 'long'},
        3: { 'Name': 'Icon', 'Type': Image},
        4: { 'Name': 'IconCH', 'Type': Image},
        5: { 'Name': 'IconCN', 'Type': Image},
    }

