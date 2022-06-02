from watchFaceParser.elements.basicElements.number import Number

class BatteryNumber:
    definitions = {
        1: { 'Name': 'Number', 'Type': Number},
        2: { 'Name': 'SuffixImageIndex', 'Type': 'long?'},
        3: { 'Name': 'Unknown3', 'Type': 'long?'},
        4: { 'Name': 'IconImageIndex', 'Type': 'long?'},
    }

