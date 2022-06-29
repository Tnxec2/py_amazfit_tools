from watchFaceParser.elements.basicElements.circleScale import CircleScale
from watchFaceParser.elements.basicElements.image import Image
from watchFaceParser.elements.basicElements.linearIconSet import LinearIconSet

class StepsProgress:
    definitions = {
        1: { 'Name': 'GoalImage', 'Type': Image},
        2: { 'Name': 'Gauge', 'Type': LinearIconSet},
        3: { 'Name': 'Circle', 'Type': CircleScale},
    }

