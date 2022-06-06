from watchFaceParser.elements.basicElements.numberExt import NumberExtended
from watchFaceParser.elements.basicElements.image import Image
from watchFaceParser.elements.distanceAlt import DistanceAlt

class ActivityAlt:
    definitions = {
        1: { 'Name': 'Pulse', 'Type': NumberExtended},
        2: { 'Name': 'Battery', 'Type': NumberExtended},
        3: { 'Name': 'Calories', 'Type': NumberExtended},
        4: { 'Name': 'Steps', 'Type': NumberExtended},
        5: { 'Name': 'BatterySuffixImageIndex', 'Type': 'long'},
        6: { 'Name': 'PulseNoDataImageIndex', 'Type': 'long'}, # TODO: zepp eARIxYKjIn6MXyuIdwekruLgWHo4sieDJ9JllMdP, sRJsTgan1VapqNNnujGVZfbMeyjlGawzwrZy7nFe
        9: { 'Name': 'Distance', 'Type': DistanceAlt}, # zepp ex5urh0a24zK8SgYzj80wOZ0cqB3TX8NIpPVYNHS
        10: { 'Name': 'Icon1', 'Type': Image}, # zepp ex5urh0a24zK8SgYzj80wOZ0cqB3TX8NIpPVYNHS
        11: { 'Name': 'Icon2', 'Type': Image}, # zepp ex5urh0a24zK8SgYzj80wOZ0cqB3TX8NIpPVYNHS
        12: { 'Name': 'Icon3', 'Type': Image}, # zepp ex5urh0a24zK8SgYzj80wOZ0cqB3TX8NIpPVYNHS
        13: { 'Name': 'Icon4', 'Type': Image}, # zepp ex5urh0a24zK8SgYzj80wOZ0cqB3TX8NIpPVYNHS
        14: { 'Name': 'Icon5', 'Type': Image}, # zepp ex5urh0a24zK8SgYzj80wOZ0cqB3TX8NIpPVYNHS

    }

