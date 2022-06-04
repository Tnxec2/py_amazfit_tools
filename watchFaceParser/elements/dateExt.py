from watchFaceParser.elements.basicElements.coordinates import Coordinates
from watchFaceParser.elements.basicElements.imageSet import ImageSet
from watchFaceParser.elements.dateElements.monthAndDay import MonthAndDay
from watchFaceParser.elements.dateElements.dateUnknown3 import DateUnknown3

class DateExtended:
    definitions = {
        1: { 'Name': 'YearSeparateDigits', 'Type': YearMonthDay},
    }

