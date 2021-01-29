﻿from watchFaceParser.elements.gtr2.basicElements.multilangImage import MultilangImage 
from watchFaceParser.elements.basicElements.coordinates import Coordinates
from watchFaceParser.models.color import Color

class SystemFont:
    definitions = {
        2: { 'Name': 'Coordinates', 'Type': Coordinates}, 
        3: { 'Name': 'Angle', 'Type': 'long'}, 
        4: { 'Name': 'Size', 'Type': 'long'},
        5: { 'Name': 'Color', 'Type': Color},
        6: { 'Name': 'ShowUnit', 'Type': 'bool'},
    }