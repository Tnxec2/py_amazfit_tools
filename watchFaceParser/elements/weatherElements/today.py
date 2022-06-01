from watchFaceParser.elements.weatherElements.oneline import OneLine
from watchFaceParser.elements.weatherElements.separate import Separate


class Today:
    definitions = {
        1: { 'Name': 'SeparateTemperature', 'Type': Separate},
        2: { 'Name': 'OneLine', 'Type': OneLine},
    }

