from watchFaceParser.elements.activityElements.caloriesFormattedNumber import CaloriesFormattedNumber
from watchFaceParser.elements.activityElements.distanceFormattedNumber import DistanceFormattedNumber
from watchFaceParser.elements.activityElements.pulseFormattedNumber import PulseFormattedNumber
from watchFaceParser.elements.activityElements.stepsFormattedNumber import StepsFormattedNumber
from watchFaceParser.elements.activityElements.stepPercentageProgressFormattedNumber import StepPercentageProgressFormattedNumber

class Activity:
    definitions = {
        1: { 'Name': 'Steps', 'Type': StepsFormattedNumber},
        2: { 'Name': 'StepsGoal', 'Type': StepsFormattedNumber},
        3: { 'Name': 'Calories', 'Type': CaloriesFormattedNumber},
        4: { 'Name': 'Pulse', 'Type': PulseFormattedNumber},
        5: { 'Name': 'Distance', 'Type': DistanceFormattedNumber},
        7: { 'Name': 'StepPercentageProgress', 'Type': StepPercentageProgressFormattedNumber}, # zepp: kAFXMVWYNeBKAVr7Ubj5ExUCEEXP6k7vu3iSQqr4
    }

