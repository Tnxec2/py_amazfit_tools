from watchFaceParser.elements.weatherElements.weathericon import WeatherIcon
from watchFaceParser.elements.weatherElements.temperature import Temperature


class Weather:
    definitions = {
        1: { 'Name': 'Icon', 'Type': WeatherIcon} ,
        2: { 'Name': 'Temperature', 'Type': Temperature},
    }

