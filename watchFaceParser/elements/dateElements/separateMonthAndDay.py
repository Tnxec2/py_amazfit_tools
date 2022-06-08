from watchFaceParser.elements.basicElements.number import Number
from watchFaceParser.elements.basicElements.imageSet import ImageSet

class SeparateMonthAndDay:
    definitions = {
        1: { 'Name': 'Month', 'Type': Number},
        2: { 'Name': 'MonthName', 'Type': ImageSet}, # tested on bips, thies work fine
        3: { 'Name': 'Day', 'Type': Number},
        4: { 'Name': 'MonthAsWord', 'Type': ImageSet}, # zepp
        5: { 'Name': 'MonthAsWordCH', 'Type': ImageSet},
        6: { 'Name': 'MonthAsWordCN', 'Type': ImageSet},
    }
