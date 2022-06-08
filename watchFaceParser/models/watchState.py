import datetime

from watchFaceParser.models.weatherCondition import WeatherCondition


class WatchState:
    def __init__(self, BatteryLevel = 67, Pulse = 62, Steps = 14876, Calories = 764, PAI = 52, Distance = 2367, Bluetooth = True, Unlocked = True, Alarm = True, DoNotDisturb = True, CurrentTemperature=-10, CurrentWeather = WeatherCondition.PartlyCloudy, Aqi = 15, Humidity = 68):
        self._time = datetime.datetime.now().replace(hour = 10, minute = 10, second = 30)
        self._steps = Steps
        self._goal = 8000
        self._distance = Distance
        self._calories = Calories
        self._pulse = Pulse
        self._pai = PAI
        self._batteryLevel = BatteryLevel
        self._bluetooth = Bluetooth
        self._unlocked = Unlocked
        self._alarm = Alarm
        self._doNotDisturb = DoNotDisturb
        self._currentWeather = CurrentWeather
        self._currentTemperature = CurrentTemperature
        self._aqi = Aqi
        self._humidity = Humidity
        self._sunrise = datetime.datetime.now().replace(hour = 6, minute = 23, second = 12)
        self._sunset = datetime.datetime.now().replace(hour = 21, minute = 12, second = 38)


    def setCurrentWeather(self, n):
        self._currentWeather = n

    def setCurrentTemperature(self, n):
        self._currentTemperature = n

    def getCurrentWeather(self):
        return self._currentWeather

    def getCurrentTemperature(self):
        return self._currentTemperature

    def getTime(self):
        return self._time


    def setTime(self, _time):
        self._time = _time


    def getSteps(self):
        return self._steps


    def getGoal(self):
        return self._goal


    def getPulse(self):
        return self._pulse

    def getPAI(self):
        return self._pai


    def getBatteryLevel(self):
        return self._batteryLevel


    def getDistance(self):
        return self._distance


    def getCalories(self):
        return self._calories


    def getBluetooth(self):
        return self._bluetooth


    def getUnlocked(self):
        return self._unlocked


    def getAlarm(self):
        return self._alarm


    def getDoNotDisturb(self):
        return self._doNotDisturb

    def getSunrise(self):
        return self._sunrise
    def getSunset(self):
        return self._sunset
    
    def getAqi(self):
        return self._aqi

    def getHumidity(self):
        return self._humidity


    def toJSON(self):
        return {
            'Time': self.datetimeToJson(self._time),
            'Steps': self._steps,
            'Goal': self._goal,
            'Pulse': self._pulse,
            'PAI': self._pai,
            'BatteryLevel': self._batteryLevel,
            'Distance': self._distance,
            'Calories': self._calories,
            'Bluetooth': self._bluetooth,
            'Unlocked': self._unlocked,
            'Alarm': self._alarm,
            'DoNotDisturb': self._doNotDisturb,
            'CurrentWeather': self._currentWeather,
            'CurrentTemperature': self._currentTemperature,
            'Sunrise': self.datetimeToJson(self._sunrise),
            'Sunset': self.datetimeToJson(self._sunset),
            'AQI': self._aqi,
            'Humidity': self._humidity,

        }

    def datetimeToJson(self, t):
        return { 'Year': t.year, 'Month': t.month, 'Day': t.day, 'Hour': t.hour, 'Minute': t.minute, 'Second': t.second }


    @staticmethod
    def fromJson(j):
        w = WatchState()
        w._time = j['Time']
        w._sunrise = j['Sunrise'] if 'Sunrise' in j else w._sunrise
        w._sunset = j['Sunset'] if 'Sunset' in j else w._sunset
        w._steps = j['Steps']
        w._goal = j['Goal']
        w._pulse = j['Pulse']
        w._pai = j['PAI'] if 'PAI' in j else w._pai
        w._batteryLevel = j['BatteryLevel']
        w._distance = j['Distance']
        w._calories = j['Calories']
        w._bluetooth = j['Bluetooth']
        w._unlocked = j['Unlocked']
        w._alarm = j['Alarm']
        w._doNotDisturb = j['DoNotDisturb']
        w._currentWeather = j['CurrentWeather'] if 'CurrentWeather' in j else w._currentWeather
        w._currentTemperature = j['CurrentTemperature'] if 'CurrentTemperature' in j else w._currentTemperature
        w._aqi = j['AQI'] if 'AQI' in j else w._aqi
        w._humidity = j['Humidity'] if 'Humidity' in j else w._humidity
        return w

