from watchFaceParser.elements.weatherElements.tempnumber import TempNumber
from watchFaceParser.elements.basicElements.coordinates import Coordinates

class Separate:
    definitions = {
        1: { 'Name': 'Day', 'Type': TempNumber},
        2: { 'Name': 'Night', 'Type': TempNumber},
        3: { 'Name': 'DayAlt', 'Type': Coordinates},
        4: { 'Name': 'NightAlt', 'Type': Coordinates},
        5: { 'Name': 'Unknown5', 'Type': Coordinates},
        6: { 'Name': 'Unknown6', 'Type': Coordinates},
    }

