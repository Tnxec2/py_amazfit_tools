from ast import Num
from watchFaceParser.elements.basicElements.number import Number
from watchFaceParser.elements.basicElements.coordinates import Coordinates

class OneLine:
    definitions = {
        1: { 'Name': 'Number', 'Type': Number},
        2: { 'Name': 'MinusSignImageIndex', 'Type': 'long'},
        3: { 'Name': 'DelimiterImageIndex', 'Type': 'long'},
        4: { 'Name': 'AppendDegresForBoth', 'Type': 'bool'},
        5: { 'Name': 'DegreesImageIndex', 'Type': 'long'},
    }

