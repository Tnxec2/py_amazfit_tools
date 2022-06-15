from watchFaceParser.elements.backgroundOldBip import Background
from watchFaceParser.elements.timeOldBip import Time
from watchFaceParser.elements.activityOldBip import Activity
from watchFaceParser.elements.dateOldBip import Date
from watchFaceParser.elements.stepsProgressOldBip import StepsProgress
from watchFaceParser.elements.status import Status
from watchFaceParser.elements.batteryOldBip import Battery
from watchFaceParser.elements.analogDialFace import AnalogDialFace
from watchFaceParser.elements.weather import Weather

class WatchFaceOldBip:
    definitions = {
        2: { 'Name': 'Background', 'Type': Background},
        3: { 'Name': 'Time', 'Type': Time},
        4: { 'Name': 'Activity', 'Type': Activity},
        5: { 'Name': 'Date', 'Type': Date},
        6: { 'Name': 'Weather', 'Type': Weather},
        7: { 'Name': 'StepsProgress', 'Type': StepsProgress},
        8: { 'Name': 'Status', 'Type': Status},
        9: { 'Name': 'Battery', 'Type': Battery},
        10: { 'Name': 'AnalogDialFace', 'Type': AnalogDialFace},
    }
