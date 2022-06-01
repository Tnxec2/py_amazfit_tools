from watchFaceParser.elements.weatherElements.tempnumber import TempNumber
from watchFaceParser.elements.weatherElements.today import Today

class Temperature:
    definitions = {
        1: { 'Name': 'Current', 'Type': TempNumber},
        2: { 'Name': 'Today', 'Type': Today},
    }

