from watchFaceParser.elements.activityElements.distanceFormattedNumber import DistanceFormattedNumber
from watchFaceParser.elements.basicElements.number import Number

class Activity:
    definitions = {
        1: { 'Name': 'Steps', 'Type': Number},
        2: { 'Name': 'StepsGoal', 'Type': Number},
        3: { 'Name': 'Calories', 'Type': Number},
        4: { 'Name': 'Pulse', 'Type': Number},
        5: { 'Name': 'Distance', 'Type': DistanceFormattedNumber},
    }

