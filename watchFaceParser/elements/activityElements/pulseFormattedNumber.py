from watchFaceParser.elements.basicElements.number import Number

class PulseFormattedNumber:
    definitions = {
        1: { 'Name': 'Number', 'Type': Number},
        2: { 'Name': 'SuffixImageIndex', 'Type': 'long'},
        3: { 'Name': 'NoDataImageIndex', 'Type': 'long'}, 
    }

