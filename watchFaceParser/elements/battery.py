from watchFaceParser.elements.basicElements.number import Number
from watchFaceParser.elements.basicElements.image import Image
from watchFaceParser.elements.basicElements.imageSet import ImageSet
from watchFaceParser.elements.basicElements.circleScale import CircleScale

class Battery:
    definitions = {
        1: { 'Name': 'Text', 'Type': Number},
        2: { 'Name': 'Icon', 'Type': ImageSet}, 
    }

