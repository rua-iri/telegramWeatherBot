
from .base_api import Base_API
from constants import OPEN_WEATHER_MAP_BASE_URL

import os


class OpenWeatherMapAPI(Base_API):

    def __init__(self, latitude: float, longitude: float):
        data = self.fetch_api_data(latitude=latitude, longitude=longitude)
        weather_data = data.get('weather')[0]
        main_data = data.get('main')

        self.location = f"{data.get('name')}, "
        self.location += data.get('sys').get('country')

        self.wind = f"{data.get('wind').get('speed')} m/s "
        self.wind += self.calc_direction(data.get('wind').get('deg'))

        self.humidity = main_data.get('humidity')

        self.condition_text = (
            weather_data.get('main')
            + " - "
            + weather_data.get('description')
        )
        self.condition_icon = (
            "https://openweathermap.org/img/wn/"
            + weather_data.get('icon')
            + "@2x.png"
        )

        self.temperature = main_data.get('temp')
        self.feels_like = main_data.get('feels_like')

    def calc_direction(angle: int):
        import math
        angle_list = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE",
                      "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]

        index = math.floor((angle / 22.5) + 0.5)
        return angle_list[index]

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

    def gen_weather_message(self) -> str:

        return """
        Open Weather
        Location: {location}
        Condition: {condition_text}
        Temperature: {temperature}°C (Feels Like: {feels_like}°C)
        Wind: {wind}
        Humidity: {humidity}
        """.format(**self.__dict__)

    def __repr__(self) -> str:
        return f"""
        Location: {self.location},
        Wind: {self.wind},
        Humidity: {self.humidity}
        Condition: {self.condition_text},
        Icon: {self.condition_icon},
        Temperature: {self.temperature},
        Feels Like: {self.feels_like},
        """
