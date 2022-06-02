from watchFaceParser.elements.timeElements.twoDigits import TwoDigits
from watchFaceParser.elements.timeElements.amPm import AmPm
from watchFaceParser.elements.timeElements.pm import Pm
from watchFaceParser.elements.basicElements.image import Image
from watchFaceParser.models.drawingOrder import DrawingOrder

class Time:
    definitions = {
        1: { 'Name': 'Hours', 'Type': TwoDigits},
        2: { 'Name': 'Minutes', 'Type': TwoDigits},
        3: { 'Name': 'Seconds', 'Type': TwoDigits},
        4: { 'Name': 'AmPm', 'Type': AmPm},
        5: { 'Name': 'DrawingOrder', 'Type': DrawingOrder},
        9: { 'Name': 'Unknown9', 'Type': 'long?'},
    }

