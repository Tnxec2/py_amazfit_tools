from watchFaceParser.elements.activityAlt import ActivityAlt
from watchFaceParser.elements.background import Background
from watchFaceParser.elements.caloriesProgress import CaloriesProgress
from watchFaceParser.elements.paiProgress import PaiProgress
from watchFaceParser.elements.distanceProgress import DistanceProgress
from watchFaceParser.elements.pulseStatus import PulseStatus
from watchFaceParser.elements.shortcutElements.shortcuts import Shortcuts
from watchFaceParser.elements.time import Time
from watchFaceParser.elements.activity import Activity
from watchFaceParser.elements.date import Date
from watchFaceParser.elements.stepsProgress import StepsProgress
from watchFaceParser.elements.status import Status
from watchFaceParser.elements.battery import Battery
from watchFaceParser.elements.analogDialFace import AnalogDialFace
from watchFaceParser.elements.weather import Weather
from watchFaceParser.elements.dateExt import DateExtended
from watchFaceParser.elements.weekdayStatus import WeekdayStatus

class WatchFace:
    definitions = {
        1: { 'Name': 'U1', 'Type': 'long?'},
        2: { 'Name': 'Background', 'Type': Background},
        3: { 'Name': 'Time', 'Type': Time},
        4: { 'Name': 'Activity', 'Type': Activity},
        5: { 'Name': 'Date', 'Type': Date},
        6: { 'Name': 'Weather', 'Type': Weather},
        7: { 'Name': 'StepsProgress', 'Type': StepsProgress},
        8: { 'Name': 'Status', 'Type': Status},
        9: { 'Name': 'Battery', 'Type': Battery},
        10: { 'Name': 'AnalogDialFace', 'Type': AnalogDialFace},
        13: { 'Name': 'PulseStatus', 'Type': PulseStatus}, # zepp 6T9UoXZxYRma9lv9DZH0infCu269fAck4EF6DPUw
        14: { 'Name': 'Unknown14', 'Type': 'long?'}, # TODO: zepp 6EKQ2lOS3HFKbK4RJOEV4sgGbmOKqZrDFTinZdLe
        15: { 'Name': 'Shortcuts', 'Type': Shortcuts}, # TODO: zepp 2UTgO1V4APZpnGAvWcP50ca3wODjloDYbeqZ6i9J
        16: { 'Name': 'WeekdayIcon', 'Type': WeekdayStatus}, # zepp U8tlMNRdHSjVK44n55Hj6fp41AEW3jD3FXPVWbqq
        17: { 'Name': 'DistanceProgress', 'Type': DistanceProgress}, # zepp 6T9UoXZxYRma9lv9DZH0infCu269fAck4EF6DPUw
        18: { 'Name': 'DateExtended', 'Type': DateExtended}, # zepp 6EKQ2lOS3HFKbK4RJOEV4sgGbmOKqZrDFTinZdLe
        19: { 'Name': 'Unknown19-PAI?', 'Type': 'long?'}, # TODO: zepp iydgD8W5wmb7n3adhPSK9Dx0p3QLDexG3ZfKaxUo
        20: { 'Name': 'ActivityAlt', 'Type': ActivityAlt}, # zepp eARIxYKjIn6MXyuIdwekruLgWHo4sieDJ9JllMdP
        21: { 'Name': 'CaloriesProgress', 'Type': CaloriesProgress}, # zepp 6T9UoXZxYRma9lv9DZH0infCu269fAck4EF6DPUw
        22: { 'Name': 'PaiProgress', 'Type': PaiProgress}, # TODO: check PAI or Pulse? zepp Dz9GUS6zjaJEJpsdNaKVdJieyELjKoSRf9VJOMi6
    }
