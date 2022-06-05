from watchFaceParser.elements.basicElements.separateDigits import FourDigits, TwoDigits

class DateExtended:
    definitions = {
        1: { 'Name': 'YearSeparate', 'Type': FourDigits},
        2: { 'Name': 'MonthSeparate', 'Type': TwoDigits},
        3: { 'Name': 'DaySeparate', 'Type': TwoDigits},
    }

