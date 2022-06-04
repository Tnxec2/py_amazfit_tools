from watchFaceParser.elements.basicElements.circleScale import CircleScale
from watchFaceParser.elements.basicElements.image import Image
from watchFaceParser.elements.basicElements.imageSet import ImageSet
from watchFaceParser.elements.basicElements.iconSet import IconSet
from watchFaceParser.elements.basicElements.linearIconSet import LinearIconSet

class UnknownProgress:
    definitions = {
        3: { 'Name': 'Circle', 'Type': CircleScale},
    }

