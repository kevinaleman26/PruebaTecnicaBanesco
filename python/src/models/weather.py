from dataclasses import dataclass
from ..services.weather import fetch_data_from_api_weather

@dataclass
class Weather:
    main: str
    celsius: float

    def __init__(self, lat, lon):
        weather_api_response = self.get_weather_data_from_geo(lat=lat,lon=lon)
        local_weather = weather_api_response['current']
        self.main = local_weather['weather'][0]['main']
        self.celsius = self.temp_kelvin_to_celsius(local_weather["temp"])

    @staticmethod
    def temp_kelvin_to_celsius(kelvin):
        celsius = kelvin - 273.15
        return celsius
    
    @staticmethod
    def get_weather_data_from_geo(lat, lon):
        weather_dt = fetch_data_from_api_weather(lat, lon)
        if weather_dt is None:
            print("\n[FIN] No se pudieron obtener los datos del clima.")
            return None
        return weather_dt
    
    def __repr__(self):
        return f"Weather(Main='{self.main}', Celcius='{self.celsius}')"