from watchFaceParser.elements.basicElements.circleScale import CircleScale
from watchFaceParser.elements.batteryNumber import BatteryNumber
from watchFaceParser.elements.basicElements.imageSet import ImageSet
from watchFaceParser.elements.basicElements.linearIconSet import LinearIconSet


class Battery:
    definitions = {
        1: { 'Name': 'Text', 'Type': BatteryNumber},
        2: { 'Name': 'Icon', 'Type': ImageSet}, 
        3: { 'Name': 'Scale', 'Type': LinearIconSet}, 
        4: { 'Name': 'Circle', 'Type': CircleScale}, 
        5: { 'Name': 'Unknown5', 'Type': 'long?'}, 
        6: { 'Name': 'Unknown6', 'Type': 'long?'}, 
    }

