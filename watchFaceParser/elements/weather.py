from watchFaceParser.elements.weatherElements.weathericon import WeatherIcon
from watchFaceParser.elements.weatherElements.temperature import Temperature
from watchFaceParser.elements.weatherElements.aqi import AQI
from watchFaceParser.elements.weatherElements.humidity import Humidity


class Weather:
    definitions = {
        1: { 'Name': 'Icon', 'Type': WeatherIcon} ,
        2: { 'Name': 'Temperature', 'Type': Temperature},
        3: { 'Name': 'AQI', 'Type': AQI}, #  zepp 6EKQ2lOS3HFKbK4RJOEV4sgGbmOKqZrDFTinZdLe
        4: { 'Name': 'Humidity', 'Type': Humidity}, #  zepp 6EKQ2lOS3HFKbK4RJOEV4sgGbmOKqZrDFTinZdLe
    }

