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
        9: { 'Name': 'UnknownLong9', 'Type': 'long'},
        10: { 'Name': 'Unknown10', 'Type': 'long?'}, # TODO: zepp: 2UTgO1V4APZpnGAvWcP50ca3wODjloDYbeqZ6i9J
        11: { 'Name': 'Unknown11', 'Type': 'long?'}, # TODO: zepp: 2UTgO1V4APZpnGAvWcP50ca3wODjloDYbeqZ6i9J
        12: { 'Name': 'Unknown12', 'Type': 'long?'}, # TODO: zepp: 2UTgO1V4APZpnGAvWcP50ca3wODjloDYbeqZ6i9J
        13: { 'Name': 'Unknown13', 'Type': 'long?'}, # TODO: zepp: 2UTgO1V4APZpnGAvWcP50ca3wODjloDYbeqZ6i9J
        14: { 'Name': 'Unknown14', 'Type': 'long?'}, # TODO: zepp: 2UTgO1V4APZpnGAvWcP50ca3wODjloDYbeqZ6i9J
        15: { 'Name': 'Unknown15', 'Type': 'long?'}, # TODO: zepp: 2UTgO1V4APZpnGAvWcP50ca3wODjloDYbeqZ6i9J
        16: { 'Name': 'Unknown16', 'Type': 'long?'}, # TODO: zepp: 2UTgO1V4APZpnGAvWcP50ca3wODjloDYbeqZ6i9J
        17: { 'Name': 'Unknown17', 'Type': 'long?'}, # TODO: zepp: 2UTgO1V4APZpnGAvWcP50ca3wODjloDYbeqZ6i9J
    }

