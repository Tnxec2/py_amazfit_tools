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
        self._weekdayIcon = None
        self._dateext = None
        self._activityAlt = None
        self._caloriesProgress = None
        self._distanceProgress = None
        self._paiProgress = None
        super(WatchFace, self).__init__(parameters, parameter = None, parent = None, name = '')

    def draw3(self, drawer, images, state):
        if self._background:
            self._background.draw3(drawer, images, state)
        if self._activity:
            self._activity.draw3(drawer, images, state)
        if self._activityAlt:
            self._activityAlt.draw3(drawer, images, state)
        if self._stepsProgress:
            self._stepsProgress.draw3(drawer, images, state)
        if self._caloriesProgress:
            self._caloriesProgress.draw3(drawer, images, state)
        if self._pulseStatus:
            self._pulseStatus.draw3(drawer, images, state)
        if self._paiProgress:
            self._paiProgress.draw3(drawer, images, state)
        if self._distanceProgress:
            self._distanceProgress.draw3(drawer, images, state)
        if self._weather:
            self._weather.draw3(drawer, images, state)
        if self._battery:
            self._battery.draw3(drawer, images, state)

        if self._dateext:
            self._dateext.draw3(drawer, images, state)
        if self._date:
            self._date.draw3(drawer, images, state)
        if self._weekdayIcon:
            self._weekdayIcon.draw3(drawer, images, state)
        if self._time:
            self._time.draw3(drawer, images, state)
        if self._analogDial:
            self._analogDial.draw3(drawer, images, state)
        if self._status:
            self._status.draw3(drawer, images, state)


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
            from watchFaceParser.models.elements.date.weekdayStatusElement import WeekdayStatusElement
            self._weekdayIcon = WeekdayStatusElement(parameter)
            return self._weekdayIcon
        elif parameterId == 17: # DistanceProgress
            from watchFaceParser.models.elements.activity.distanceProgressElement import DistanceProgressElement
            self._distanceProgress = DistanceProgressElement(parameter)
            return self._distanceProgress
        elif parameterId == 18: # DateExtended
            from watchFaceParser.models.elements.dateExtElement import DateExtendedElement
            self._dateext = DateExtendedElement(parameter)
            return self._dateext
        elif parameterId == 20: # ActivityAlt
            from watchFaceParser.models.elements.activityAltElement import ActivityAltElement
            self._activityAlt = ActivityAltElement(parameter)
            return self._activityAlt
        elif parameterId == 21: # CaloriesProgress
            from watchFaceParser.models.elements.activity.caloriesProgressElement import CaloriesProgressElement
            self._caloriesProgress = CaloriesProgressElement(parameter)
            return self._caloriesProgress
        elif parameterId == 22: # PaiProgress
            from watchFaceParser.models.elements.activity.paiProgressElement import PaiProgressElement
            self._paiProgress = PaiProgressElement(parameter)
            return self._paiProgress
        else:
            return super(WatchFace, self).createChildForParameter(parameter)
