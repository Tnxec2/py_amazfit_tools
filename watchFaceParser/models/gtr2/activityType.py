class ActivityType:
    Battery = 1
    Steps = 2
    Calories = 3
    HeartRate = 4
    PAI = 5
    Distance = 6
    StandUp = 7
    Weather = 8
    UVindex = 9
    AirQuality = 10
    Humidity = 11
    Sunrise = 12 # Two Images possible
    ActivityUnknown13 = 13
    ActivityUnknown14 = 14
    ActivityUnknown15 = 15
    ActivityUnknown16 = 16
    ActivityGoal = 17
    FatBurning = 18
   
    Converter = {
        Battery : "Battery",
        Steps : "Steps", 
        Calories : "Calories", 
        HeartRate : "HeartRate", 
        Distance : "Distance", 
        Weather : "Weather",  
        PAI : "PAI",  
        StandUp : "StandUp",  
        UVindex : "UVindex",  
        AirQuality : "AirQuality",  
        Humidity : "Humidity",  
        Sunrise : "Sunrise",  
        ActivityUnknown13 : "ActivityUnknown13",  
        ActivityUnknown14 : "ActivityUnknown14",  
        ActivityUnknown15 : "ActivityUnknown15",  
        ActivityUnknown16 : "ActivityUnknown16",  
        ActivityGoal : "ActivityGoal",
        FatBurning  : "FatBurning",
    }

    def __init__(self, flag):
        self._flag = flag

    def hasFlag(self, flag):
        return (self._flag & flag) != 0

    def toJSON(self):
        if self._flag == None:
            self._flag = 0
        return ActivityType.Converter[self._flag]

    @staticmethod
    def fromJSON(strFlag):
        for flag in ActivityType.Converter:
            if strFlag == ActivityType.Converter[flag]:
                return flag
        return 0
