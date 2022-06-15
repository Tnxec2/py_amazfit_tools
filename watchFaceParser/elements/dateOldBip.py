from watchFaceParser.elements.basicElements.imageSet import ImageSet
from watchFaceParser.elements.dateElements.monthAndDay import MonthAndDay

class Date:
    definitions = {
        1: { 'Name': 'MonthAndDay', 'Type': MonthAndDay},
        2: { 'Name': 'WeekDay', 'Type': ImageSet},
    }

