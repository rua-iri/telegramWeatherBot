from .base_api import Base_API

import os
from constants import WEATHER_API_BASE_URL


class WeatherAPI(Base_API):

    def __init__(self, latitude: float, longitude: float):
        data = self.fetch_api_data(latitude=latitude, longitude=longitude)
        location_data = data.get('location')
        current_data = data.get('current')

        self.location = f"{location_data.get('name')}, "
        self.location += f"{location_data.get('region')}, "
        self.location += f"{location_data.get('country')}"

        self.wind = f"{current_data.get('wind_mph')} mph "
        self.wind += f"{current_data.get('wind_dir')}"

        self.precipitation = f"{current_data.get('precip_mm')} mm"
        self.humidity = current_data.get('humidity')

        self.condition_text = current_data.get('condition').get('text')
        self.condition_icon = current_data.get('condition').get('icon')

        self.temperature = current_data.get('temp_c')
        self.feels_like = current_data.get('feelslike_c')

        print(self.__dict__)

    def fetch_api_data(self, latitude: float, longitude: float):
        try:
            API_KEY_WEATHERAPI = os.getenv("API_KEY_WEATHERAPI")

            request_url = WEATHER_API_BASE_URL
            request_url += f"?q={latitude},{longitude}"
            request_url += f"&key={API_KEY_WEATHERAPI}"

            return super().make_api_call(url=request_url)

        except Exception as e:
            raise e

    def gen_weather_message(self) -> str:

        return """
        WeatherAPI
        Location: {location}
        Conditions: {condition_text}
        Temperature: {temperature}°C (Feels Like: {feels_like}°C)
        Wind: {wind}
        Humidity: {humidity}%
        Precipitation: {precipitation}
        """.format(**self.__dict__)

    def __repr__(self) -> str:
        return f"""
        Location: {self.location},
        Wind: {self.wind},
        Precipitation: {self.precipitation},
        Humidity: {self.humidity}
        Condition: {self.condition_text},
        Icon: {self.condition_icon},
        Temperature: {self.temperature},
        Feels Like: {self.feels_like},
        """
