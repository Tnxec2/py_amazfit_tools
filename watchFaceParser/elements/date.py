from watchFaceParser.elements.basicElements.coordinates import Coordinates
from watchFaceParser.elements.basicElements.imageSet import ImageSet
from watchFaceParser.elements.basicElements.numberExt import NumberExtended
from watchFaceParser.elements.dateElements.monthAndDay import MonthAndDay
from watchFaceParser.elements.basicElements.number import Number

class Date:
    definitions = {
        1: { 'Name': 'MonthAndDay', 'Type': MonthAndDay},
        2: { 'Name': 'WeekDay', 'Type': ImageSet},
        3: { 'Name': 'WeekDayCh', 'Type': ImageSet},
        4: { 'Name': 'WeekDayCn', 'Type': ImageSet},
        11: { 'Name': 'Unknown11', 'Type': NumberExtended}, # TODO: zepp eARIxYKjIn6MXyuIdwekruLgWHo4sieDJ9JllMdP
        12: { 'Name': 'Unknown12', 'Type': NumberExtended}, # TODO: zepp eARIxYKjIn6MXyuIdwekruLgWHo4sieDJ9JllMdP
    }

