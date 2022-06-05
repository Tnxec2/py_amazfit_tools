from watchFaceParser.elements.basicElements.coordinates import Coordinates

class Shortcut:
    definitions = {
        1: { 'Name': 'Start', 'Type': Coordinates},
        2: { 'Name': 'End', 'Type': Coordinates},
        3: { 'Name': 'Unknown3', 'Type': 'bool'},
    }