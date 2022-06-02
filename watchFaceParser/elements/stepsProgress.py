from watchFaceParser.elements.basicElements.circleScale import CircleScale
from watchFaceParser.elements.basicElements.image import Image
from watchFaceParser.elements.basicElements.imageScale import ImageScale

class StepsProgress:
    definitions = {
        1: { 'Name': 'GoalImage', 'Type': Image},
        2: { 'Name': 'Linear', 'Type': ImageScale},
        4: { 'Name': 'Circle', 'Type': CircleScale},
    }

