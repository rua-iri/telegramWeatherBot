
LOGGING_FORMAT = "[%(asctime)s] [%(levelname)s] - %(message)s"
LOGGING_FILENAME = "logs/{filename}.log"

WEATHER_API_BASE_URL = "https://api.weatherapi.com/v1/current.json"

OPEN_WEATHER_MAP_BASE_URL = "https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&units=metric&appid={API_KEY}"

ACCUWEATHER_GEO_BASE_URL = "http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey={API_KEY}&q={LAT},{LON}"
ACCUWEATHER_DAY_BASE_URL = "http://dataservice.accuweather.com/forecasts/v1/daily/1day/{LOCATION_KEY}?apikey={API_KEY}&metric=true"


HELP_RESPONSE_MESSAGE = """
Here are the functions I'm currently capable of performing:

/help - The command you've just run

Share your location to get a local weather forecast
"""

USER_REQUEST_LIMIT_MESSAGE = """
Error: User has exceeded the daily rate limit

Please try again tomorrow
"""

INTERNAL_SERVER_ERROR_MESSAGE = """
Error: something went wrong

Please try again later
"""
