from watchFaceParser.elements.basicElements.number import Number

class DistanceFormattedNumber:
    definitions = {
        1: { 'Name': 'Number', 'Type': Number},
        2: { 'Name': 'SuffixImageIndex', 'Type': 'long'},
        3: { 'Name': 'DecimalPointImageIndex', 'Type': 'long'},
        4: { 'Name': 'SuffixMilesImageIndex', 'Type': 'long'}, #! BipS need this SuffixMiles to show SuffixImageIndex
    }

