from watchFaceParser.elements.basicElements.circleScale import CircleScale
from watchFaceParser.elements.basicElements.image import Image
from watchFaceParser.elements.basicElements.imageSet import ImageSet
from watchFaceParser.elements.basicElements.linearIconSet import LinearIconSet


class CaloriesProgress:
    definitions = {
        1: { 'Name': 'GoalImage', 'Type': Image},  # TODO: test on watch
        2: { 'Name': 'Icon', 'Type': ImageSet}, # zepp: ex5urh0a24zK8SgYzj80wOZ0cqB3TX8NIpPVYNHS
        3: { 'Name': 'Gauge', 'Type': LinearIconSet}, # TODO: test on watch
        4: { 'Name': 'Circle', 'Type': CircleScale}, # zepp: Q45abXyTkaM6IFZdCsUwdseezHZhuZmi70i39r97
    }

