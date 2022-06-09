from watchFaceParser.models.color import Color
from watchFaceParser.elements.basicElements.image import Image

class Background:
    definitions = {
        1: { 'Name': 'Image', 'Type': Image},
        2: { 'Name': 'BackgroundColor', 'Type': Color}, # zepp ZnRgGPytintLQRm5jL9Hfju9olMIzkGDIIFDSs2s
        3: { 'Name': 'Preview', 'Type': Image},
        4: { 'Name': 'FrontImage', 'Type': Image},
    }