
from constants import ACCUWEATHER_GEO_BASE_URL
from .base_api import BaseAPI

import os


class AccuWeatherAPI(BaseAPI):

    def __init__(self, latitude: float, longitude: float):
        data = self.fetch_api_data(latitude, longitude)

    def fetch_api_data(self, latitude: float, longitude: float):
        try:
            API_KEY_ACCUWEATHER = os.getenv("API_KEY_ACCUWEATHER")
            geo_request_url = ACCUWEATHER_GEO_BASE_URL.format(
                LAT=latitude,
                LON=longitude,
                API_KEY=API_KEY_ACCUWEATHER
            )

            geo_data = super().make_api_call(url=geo_request_url)

            location_id = geo_data.get("")

        except Exception as e:
            raise e
