from watchFaceParser.elements.analogDialFaceElements.clockHand import ClockHand
from watchFaceParser.elements.basicElements.image import Image
from watchFaceParser.elements.timeElements.amPm import AmPm

class AnalogDialFace:
    definitions = {
        1: { 'Name': 'Hours', 'Type': ClockHand},
        2: { 'Name': 'Minutes', 'Type': ClockHand},
        3: { 'Name': 'Seconds', 'Type': ClockHand},
        4: { 'Name': 'AmPm', 'Type': AmPm},
    }

