from watchFaceParser.elements.gtr2.analogDialFaceElements.clockHand import ClockHand
from watchFaceParser.elements.basicElements.image import Image

class AnalogDialFace:
    definitions = {
        1: { 'Name': 'Hours', 'Type': ClockHand},
        2: { 'Name': 'Minutes', 'Type': ClockHand},
        3: { 'Name': 'Seconds', 'Type': ClockHand}, 
    }

