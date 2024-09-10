from .base_api import Base_API

import os
from constants import OPEN_WEATHER_MAP_BASE_URL


class OpenWeatherMapAPI(Base_API):

    def __init__(self, latitude: float, longitude: float):
        data = self.fetch_api_data(latitude=latitude, longitude=longitude)

        self.location = f"{data.get('name')}"
        self.location += f", {data.get('sys').get('country')}"

    def fetch_api_data(self, latitude: float, longitude: float):
        try:
            API_KEY_OPENWEATHER = os.getenv("API_KEY_OPENWEATHER")
            request_url = OPEN_WEATHER_MAP_BASE_URL.format(
                LAT=latitude,
                LON=longitude,
                API_KEY=API_KEY_OPENWEATHER
            )

            return super().make_api_call(url=request_url)

        except Exception as e:
            raise e

    def __repr__(self) -> str:
        return (
            f"Location: {self.location} \n"
        )
