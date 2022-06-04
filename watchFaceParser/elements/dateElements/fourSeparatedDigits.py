from watchFaceParser.elements.basicElements.number import Number

class YearMonthDay:
    definitions = {
        1: { 'Name': 'Year', 'Type': Number},
        2: { 'Name': 'Month', 'Type': Number},
        3: { 'Name': 'TwoDigitsMonth', 'Type': 'bool'},
        4: { 'Name': 'TwoDigitsDay', 'Type': 'bool'},
    }
