import logging
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
        
        super(WatchFace, self).__init__(parameters, parameter = None, parent = None, name = '')

    def draw3(self, drawer, images, state):
        if self._background:
            self._background.draw3(drawer, images, state)

        if self._activity:
            self._activity.draw3(drawer, images, state)
        if self._weather:
            self._weather.draw3(drawer, images, state)
        if self._battery:
            self._battery.draw3(drawer, images, state)
        if self._date:
            self._date.draw3(drawer, images, state)
    
        if self._time:
            self._time.draw3(drawer, images, state)
        if self._analogDial:
            self._analogDial.draw3(drawer, images, state)
        if self._status:
            self._status.draw3(drawer, images, state)


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        logging.debug(parameterId)
        if parameterId == 2:
            from watchFaceParser.models.elements.backgroundElementOldBip import BackgroundElement
            self._background = BackgroundElement(parameter)
            return self._background
        elif parameterId == 3:
            from watchFaceParser.models.elements.timeElementOldBip import TimeElement
            self._time = TimeElement(parameter)
            return self._time
        elif parameterId == 4:
            from watchFaceParser.models.elements.activityElementOldBip import ActivityElement
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
            from watchFaceParser.models.elements.stepsProgressElementOldBip import StepsProgressElement
            self._stepsProgress = StepsProgressElement(parameter)
            return self._stepsProgress
        elif parameterId == 8:
            from watchFaceParser.models.elements.statusElement import StatusElement
            self._status = StatusElement(parameter)
            return self._status
        elif parameterId == 9:
            from watchFaceParser.models.elements.batteryElementOldBip import BatteryElement
            self._battery = BatteryElement(parameter)
            return self._battery
        elif parameterId == 10:
            from watchFaceParser.models.elements.analogDialElement import AnalogDialElement
            self._analogDial = AnalogDialElement(parameter)
            return self._analogDial

        else:
            return super(WatchFace, self).createChildForParameter(parameter)
