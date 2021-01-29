from watchFaceParser.elements.deviceId import DeviceId
from watchFaceParser.elements.gtr2.background import Background
from watchFaceParser.elements.gtr2.system import System
from watchFaceParser.elements.gtr2.screenNormal import ScreenNormal
from watchFaceParser.elements.gtr2.screenIdle import ScreenIdle

class WatchFace:
    definitions = {
        0: { 'Name': 'Info', 'Type': DeviceId},
        3: { 'Name': 'Background', 'Type': Background},
        4: { 'Name': 'DialFace', 'Type': ScreenNormal},
        5: { 'Name': 'System', 'Type': System},
        10: { 'Name': 'ScreenIdle', 'Type': ScreenIdle},
    }