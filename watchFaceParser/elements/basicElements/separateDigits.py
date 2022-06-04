from watchFaceParser.elements.basicElements.imageSet import ImageSet

class ThreeDigits:
    definitions = {
        1: { 'Name': 'Hundreds', 'Type': ImageSet},
        2: { 'Name': 'Tens', 'Type': ImageSet},
        3: { 'Name': 'Ones', 'Type': ImageSet},
    }

class FourDigits:
    definitions = {
        1: { 'Name': 'Thousands', 'Type': ImageSet},
        2: { 'Name': 'Hundreds', 'Type': ImageSet},
        3: { 'Name': 'Tens', 'Type': ImageSet},
        4: { 'Name': 'Ones', 'Type': ImageSet},
    }

class FiveDigits:
    definitions = {
        1: { 'Name': 'TenThousands', 'Type': ImageSet},
        2: { 'Name': 'Thousands', 'Type': ImageSet},
        3: { 'Name': 'Hundreds', 'Type': ImageSet},
        4: { 'Name': 'Tens', 'Type': ImageSet},
        5: { 'Name': 'Ones', 'Type': ImageSet},
    }