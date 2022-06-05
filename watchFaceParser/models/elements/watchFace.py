from watchFaceParser.models.elements.basic.containerElement import ContainerElement


class WatchFace(ContainerElement):
    def __init__(self, parameters):
        self._background = None
        self._time = None
        self._activity = None
        self._date = None
        self._weather = None
        self._stepsProgress = None
        self._status = None
        self._battery = None
        self._analogDial = None
        self._pulseStatus = None
        super(WatchFace, self).__init__(parameters, parameter = None, parent = None, name = '')

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 2:
            from watchFaceParser.models.elements.backgroundElement import BackgroundElement
            self._background = BackgroundElement(parameter)
            return self._background
        elif parameterId == 3:
            from watchFaceParser.models.elements.timeElement import TimeElement
            self._time = TimeElement(parameter)
            return self._time
        elif parameterId == 4:
            from watchFaceParser.models.elements.activityElement import ActivityElement
            self._activity = ActivityElement(parameter)
            return self._activity
        elif parameterId == 5:
            from watchFaceParser.models.elements.dateElement import DateElement
            self._date = DateElement(parameter)
            return self._date
        elif parameterId == 6:
            from watchFaceParser.models.elements.weatherElement import WeatherElement
            self._weather = WeatherElement(parameter)
            return self._weather
        elif parameterId == 7:
            from watchFaceParser.models.elements.stepsProgressElement import StepsProgressElement
            self._stepsProgress = StepsProgressElement(parameter)
            return self._stepsProgress
        elif parameterId == 8:
            from watchFaceParser.models.elements.statusElement import StatusElement
            self._status = StatusElement(parameter)
            return self._status
        elif parameterId == 9:
            from watchFaceParser.models.elements.batteryElement import BatteryElement
            self._battery = BatteryElement(parameter)
            return self._battery
        elif parameterId == 10:
            from watchFaceParser.models.elements.analogDialElement import AnalogDialElement
            self._analogDial = AnalogDialElement(parameter)
            return self._analogDial
        elif parameterId == 13: # Pulse Status
            from watchFaceParser.models.elements.activity.pulseStatusElement import PulseStatusElement
            self._pulseStatus = PulseStatusElement(parameter)
            return self._pulseStatus
        elif parameterId == 15: # Shortcuts?
            pass
        elif parameterId == 16: # WeekdayIcon
            pass
        elif parameterId == 17: # DistanceProgress
            pass
        elif parameterId == 18: # DateExtended
            pass
        elif parameterId == 20: # ActivityAlt
            pass
        elif parameterId == 21: # CaloriesProgress
            pass
        elif parameterId == 22: # PaiProgress
            pass
        else:
            return super(WatchFace, self).createChildForParameter(parameter)
