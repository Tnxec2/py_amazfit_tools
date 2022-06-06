from watchFaceParser.elements.basicElements.separateDigits import  TwoDigits
from watchFaceParser.elements.timeElements.amPm import AmPm
from watchFaceParser.elements.timeElements.pm import Pm
from watchFaceParser.elements.basicElements.image import Image
from watchFaceParser.models.drawingOrder import DrawingOrder
from watchFaceParser.elements.basicElements.number import Number
class Time:
    definitions = {
        1: { 'Name': 'Hours', 'Type': TwoDigits},
        2: { 'Name': 'Minutes', 'Type': TwoDigits},
        3: { 'Name': 'Seconds', 'Type': TwoDigits},
        4: { 'Name': 'AmPm', 'Type': AmPm},
        5: { 'Name': 'DrawingOrder', 'Type': DrawingOrder},
        9: { 'Name': 'UnknownBoolean9', 'Type': 'bool'},
        10: { 'Name': 'SunriseHours', 'Type': Number}, # zepp: 2UTgO1V4APZpnGAvWcP50ca3wODjloDYbeqZ6i9J
        11: { 'Name': 'SunriseMinutes', 'Type': Number}, # zepp: 2UTgO1V4APZpnGAvWcP50ca3wODjloDYbeqZ6i9J
        12: { 'Name': 'SunsetHours', 'Type': Number}, # zepp: 2UTgO1V4APZpnGAvWcP50ca3wODjloDYbeqZ6i9J
        13: { 'Name': 'SunsetMinutes', 'Type': Number}, # zepp: 2UTgO1V4APZpnGAvWcP50ca3wODjloDYbeqZ6i9J
        14: { 'Name': 'SunriseHoursNoDataImage', 'Type': Image}, # zepp: 2UTgO1V4APZpnGAvWcP50ca3wODjloDYbeqZ6i9J
        15: { 'Name': 'SunriseMinutesNoDataImage', 'Type': Image}, # zepp: 2UTgO1V4APZpnGAvWcP50ca3wODjloDYbeqZ6i9J
        16: { 'Name': 'SunsetHoursNoDataImage', 'Type': Image}, # zepp: 2UTgO1V4APZpnGAvWcP50ca3wODjloDYbeqZ6i9J
        17: { 'Name': 'SunsetMinutesNoDataImage', 'Type': Image}, # zepp: 2UTgO1V4APZpnGAvWcP50ca3wODjloDYbeqZ6i9J
    }

