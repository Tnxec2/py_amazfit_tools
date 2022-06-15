from watchFaceParser.elements.basicElements.number import Number
from watchFaceParser.elements.basicElements.imageSet import ImageSet
from watchFaceParser.elements.basicElements.linearIconSet import LinearIconSet


class Battery:
    definitions = {
        1: { 'Name': 'Text', 'Type': Number},
        2: { 'Name': 'Icon', 'Type': ImageSet}, 
        3: { 'Name': 'Scale', 'Type': LinearIconSet}, 
    }

