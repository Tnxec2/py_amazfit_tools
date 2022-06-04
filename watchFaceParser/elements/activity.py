from watchFaceParser.elements.activityElements.formattedNumber import FormattedNumber

class Activity:
    definitions = {
        1: { 'Name': 'Steps', 'Type': FormattedNumber},
        2: { 'Name': 'StepsGoal', 'Type': FormattedNumber},
        3: { 'Name': 'Calories', 'Type': FormattedNumber},
        4: { 'Name': 'Pulse', 'Type': FormattedNumber},
        5: { 'Name': 'Distance', 'Type': FormattedNumber},
        6: { 'Name': 'PAI', 'Type': FormattedNumber},
    }

