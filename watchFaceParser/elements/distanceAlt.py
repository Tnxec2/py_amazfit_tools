from watchFaceParser.elements.basicElements.numberExt import NumberExtended
from watchFaceParser.elements.basicElements.image import Image

class DistanceAlt:
    definitions = {
        1: { 'Name': 'Number', 'Type': NumberExtended},
        2: { 'Name': 'DelimiterImageIndex', 'Type': 'long'},
        3: { 'Name': 'SuffixKMIcon', 'Type': Image}, #TODO: zepp eARIxYKjIn6MXyuIdwekruLgWHo4sieDJ9JllMdP
        4: { 'Name': 'SuffixMIIcon', 'Type': Image}, #TODO: zepp eARIxYKjIn6MXyuIdwekruLgWHo4sieDJ9JllMdP

    }

