from watchFaceParser.elements.basicElements.circleScale import CircleScale
from watchFaceParser.elements.basicElements.image import Image
from watchFaceParser.elements.basicElements.imageSet import ImageSet
from watchFaceParser.elements.basicElements.iconSet import IconSet

class StepsProgress:
    definitions = {
        1: { 'Name': 'GoalImage', 'Type': Image},
        2: { 'Name': 'Linear', 'Type': IconSet},
        3: { 'Name': 'Gauge', 'Type': ImageSet},
        4: { 'Name': 'Circle', 'Type': CircleScale},
    }

