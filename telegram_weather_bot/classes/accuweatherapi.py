
from constants import ACCUWEATHER_GEO_BASE_URL, ACCUWEATHER_DAY_BASE_URL
from .base_api import BaseAPI

import os


class AccuWeatherAPI(BaseAPI):

    def __init__(self, latitude: float, longitude: float):
        API_KEY_ACCUWEATHER = os.getenv("API_KEY_ACCUWEATHER")

        geo_data = self.fetch_location_data(
            latitude,
            longitude,
            API_KEY_ACCUWEATHER
        )

        weather_data = self.fetch_api_data(
            geo_data.get("key"),
            API_KEY_ACCUWEATHER
        )

        self.location = f"{geo_data.get('EnglishName')}, "
        self.location = geo_data.get("Country").get("EnglishName")

        temperature = weather_data.get("DailyForecasts").get("Temperature")

        self.temp_min = temperature.get("Minimum").get("Value")
        self.temp_max = temperature.get("Maximum").get("Value")

        self.condition = weather_data.get("Headline").get("Text")

    def fetch_location_data(
            self,
            latitude: float,
            longitude: float,
            api_key: str
    ):
        try:
            geo_request_url: str = ACCUWEATHER_GEO_BASE_URL.format(
                LAT=latitude,
                LON=longitude,
                API_KEY=api_key
            )

            return super().make_api_call(url=geo_request_url)

        except Exception as e:
            raise e

    def fetch_api_data(self, location_key: int, api_key: str):
        try:
            weather_request_url: str = ACCUWEATHER_DAY_BASE_URL.format(
                LOCATION_KEY=location_key,
                API_KEY=api_key
            )

            return super().make_api_call(url=weather_request_url)

        except Exception as e:
            raise e

    def gen_weather_message(self) -> str:

        return """
        Open Weather
        Location: {location}
        Condition: {condition}
        Max Temperature: {temp_max}℃
        Min Temperature: {temp_min}℃
        """.format(**self.__dict__)

    def __repr__(self) -> str:
        return f"""
        Location: {self.location},
        Condition: {self.condition},
        Icon: {self.condition_icon},
        Max Temperature: {self.temp_max},
        Min Temperature: {self.temp_min}
        """
