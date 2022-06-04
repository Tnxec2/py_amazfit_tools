from watchFaceParser.elements.basicElements.coordinates import Coordinates
from watchFaceParser.elements.basicElements.imageSet import ImageSet
from watchFaceParser.elements.dateElements.monthAndDay import MonthAndDay
from watchFaceParser.elements.dateElements.dateUnknown3 import DateUnknown3

class Date:
    definitions = {
        1: { 'Name': 'MonthAndDay', 'Type': MonthAndDay},
        2: { 'Name': 'WeekDay', 'Type': ImageSet},
        3: { 'Name': 'WeekDayCh', 'Type': ImageSet},
        4: { 'Name': 'WeekDayCn', 'Type': ImageSet},
        11: { 'Name': 'Unknown11', 'Type': 'long?'}, # TODO: zepp eARIxYKjIn6MXyuIdwekruLgWHo4sieDJ9JllMdP
        12: { 'Name': 'Unknown12', 'Type': 'long?'}, # TODO: zepp eARIxYKjIn6MXyuIdwekruLgWHo4sieDJ9JllMdP
    }

