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
        2: { 'Name': 'Background', 'Type': Background},
        3: { 'Name': 'Time', 'Type': Time},
        4: { 'Name': 'U4', 'Type': 'long?'},
        5: { 'Name': 'Date', 'Type': Date},
        6: { 'Name': 'Weather', 'Type': 'long?'},
        7: { 'Name': 'U7', 'Type': 'long?'},
        8: { 'Name': 'U8', 'Type': 'long?'},
        9: { 'Name': 'U9', 'Type': 'long?'},
    }
