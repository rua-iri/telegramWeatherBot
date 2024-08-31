from .base_api import Base_API

import os
import constants


class WeatherAPI(Base_API):

    def __init__(self, latitude: int, longitude: int):
        data = self.fetch_api_data(latitude=latitude, longitude=longitude)

        self.location = f"{data['location'].get('name')}, "
        self.location += f"{data['location'].get('region')}, "
        self.location += f"{data['location'].get('country')}"

        self.wind = f"{data['current'].get('wind_mph')} mph "
        self.wind += f"{data['current'].get('wind_dir')}"

        self.precipitation = f"{data['current'].get('precip_mm')} mm"

        self.condition = data['current'].get('condition').get('text')
        self.icon = data['current'].get('condition').get('icon')
        self.temperature = data['current'].get('temp_c')
        self.feels_like = data['current'].get('feelslike_c')
        self.humidity = data['current'].get('humidity'),

    def fetch_api_data(self, latitude: int, longitude: int):
        try:
            API_KEY_WEATHERAPI = os.getenv("API_KEY_WEATHERAPI")

            req_url = f"{constants.weather_api_base_url}current.json"
            req_url += f"?q={latitude},{longitude}"
            req_url += f"&key={API_KEY_WEATHERAPI}"

            return super().make_api_call(url=req_url)

        except Exception as e:
            raise e

    def __repr__(self) -> str:
        return f"""
        Location: {self.location},
        Wind: {self.wind},
        Precipitation: {self.precipitation},
        Condition: {self.condition},
        Temperature: {self.temperature},
        Feels Like: {self.feels_like},
        Humidity: {self.humidity}
        """
