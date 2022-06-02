from watchFaceParser.elements.batteryNumber import BatteryNumber
from watchFaceParser.elements.basicElements.image import Image
from watchFaceParser.elements.basicElements.imageSet import ImageSet
from watchFaceParser.elements.basicElements.imageScale import IconSet


class Battery:
    definitions = {
        1: { 'Name': 'Text', 'Type': BatteryNumber},
        2: { 'Name': 'Icon', 'Type': ImageSet}, 
        3: { 'Name': 'Scale', 'Type': IconSet}, 
        4: { 'Name': 'Unknown4', 'Type': 'long?'}, 
        5: { 'Name': 'Unknown5', 'Type': 'long?'}, 
        6: { 'Name': 'Unknown6', 'Type': 'long?'}, 
    }

