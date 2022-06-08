from watchFaceParser.elements.basicElements.number import Number
from watchFaceParser.elements.basicElements.image import Image

class PAI:
    definitions = {
        1: { 'Name': 'IconLow', 'Type': Image},
        2: { 'Name': 'IconNormal', 'Type': Image},
        3: { 'Name': 'IconHigh', 'Type': Image},
        4: { 'Name': 'NumberLow', 'Type': Number},
        5: { 'Name': 'NumberNormal', 'Type': Number},
        6: { 'Name': 'NumberHigh', 'Type': Number},
        7: { 'Name': 'NoDataImage', 'Type': Image},
        11: { 'Name': 'NumberGeneric', 'Type': Number},
    }

