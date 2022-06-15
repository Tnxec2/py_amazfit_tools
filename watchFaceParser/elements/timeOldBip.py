from watchFaceParser.elements.basicElements.separateDigits import  TwoDigits
from watchFaceParser.elements.timeElements.amPmOldBip import AmPm
from watchFaceParser.models.drawingOrder import DrawingOrder


class Time:
    definitions = {
        1: { 'Name': 'Hours', 'Type': TwoDigits},
        2: { 'Name': 'Minutes', 'Type': TwoDigits},
        3: { 'Name': 'Seconds', 'Type': TwoDigits},
        4: { 'Name': 'AmPm', 'Type': AmPm},
        5: { 'Name': 'DrawingOrder', 'Type': DrawingOrder},
    }

