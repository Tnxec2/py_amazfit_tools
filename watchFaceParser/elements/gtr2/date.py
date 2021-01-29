from watchFaceParser.elements.gtr2.digitalElements.digitalDateDigit import DigitalDateDigit
from watchFaceParser.elements.gtr2.digitalElements.digitalCommonDigit import DigitalCommonDigit
from watchFaceParser.elements.gtr2.basicElements.image import Image 
from watchFaceParser.elements.gtr2.progress import Progress  
class Date:
    definitions = {
        1: { 'Name': 'DateDigits', 'Type': [DigitalDateDigit] },
        2: { 'Name': 'WeeksDigits', 'Type': DigitalCommonDigit },
        3: { 'Name': 'DateProgress', 'Type': Progress},
    }
