from watchFaceParser.elements.weatherElements.weathericon import WeatherIcon
from watchFaceParser.elements.weatherElements.temperature import Temperature


class Weather:
    definitions = {
        1: { 'Name': 'Icon', 'Type': WeatherIcon} ,
        2: { 'Name': 'Temperature', 'Type': Temperature},
        3: { 'Name': 'Unknown3', 'Type': 'long?'}, # TODO: zepp 6EKQ2lOS3HFKbK4RJOEV4sgGbmOKqZrDFTinZdLe
        4: { 'Name': 'Unknown4', 'Type': 'long?'}, # TODO: zepp 6EKQ2lOS3HFKbK4RJOEV4sgGbmOKqZrDFTinZdLe
    }

