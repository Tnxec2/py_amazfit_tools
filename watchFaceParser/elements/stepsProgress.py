from watchFaceParser.elements.basicElements.circleScale import CircleScale
from watchFaceParser.elements.basicElements.image import Image
from watchFaceParser.elements.basicElements.imageSet import ImageSet
from watchFaceParser.elements.basicElements.linearIconSet import LinearIconSet

class StepsProgress:
    definitions = {
        1: { 'Name': 'GoalImage', 'Type': Image},
        2: { 'Name': 'IconSet', 'Type': ImageSet},
        3: { 'Name': 'Gauge', 'Type': LinearIconSet},
        4: { 'Name': 'Circle', 'Type': CircleScale},
    }

