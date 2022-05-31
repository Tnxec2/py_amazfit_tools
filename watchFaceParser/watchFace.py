from watchFaceParser.elements.background import Background
from watchFaceParser.elements.time import Time
from watchFaceParser.elements.activity import Activity
from watchFaceParser.elements.date import Date
from watchFaceParser.elements.stepsProgress import StepsProgress
from watchFaceParser.elements.status import Status
from watchFaceParser.elements.battery import Battery
from watchFaceParser.elements.analogDialFace import AnalogDialFace
from watchFaceParser.elements.unknownType14 import UnknownType14

class WatchFace:
    definitions = {
        1: { 'Name': 'U1', 'Type': 'long?'},
        2: { 'Name': 'U2', 'Type': 'long?'},
        3: { 'Name': 'U3', 'Type': 'long?'},
        4: { 'Name': 'U4', 'Type': 'long?'},
        5: { 'Name': 'U5', 'Type': 'long?'},
        6: { 'Name': 'U6', 'Type': 'long?'},
    }
