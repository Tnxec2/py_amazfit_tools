from watchFaceParser.elements.activityElements.formattedNumber import FormattedNumber
from watchFaceParser.elements.activityElements.pulseFormattedNumber import PulseFormattedNumber

class Activity:
    definitions = {
        1: { 'Name': 'Steps', 'Type': FormattedNumber},
        2: { 'Name': 'StepsGoal', 'Type': FormattedNumber},
        3: { 'Name': 'Calories', 'Type': FormattedNumber},
        4: { 'Name': 'Pulse', 'Type': PulseFormattedNumber},
        5: { 'Name': 'Distance', 'Type': FormattedNumber},
    }

