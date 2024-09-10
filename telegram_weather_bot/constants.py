
LOGGING_FORMAT = "[%(asctime)s] [%(levelname)s] - %(message)s"
LOGGING_FILENAME = "logs/{filename}.log"

WEATHER_API_BASE_URL = "https://api.weatherapi.com/v1/current.json"

OPEN_WEATHER_MAP_BASE_URL = "https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&units=metric&appid={API_KEY}"

HELP_RESPONSE_MESSAGE = """
Here are the functions I'm currently capable of performing:

/help - The command you've just run

Share your location to get a local weather forecast
"""

USER_REQUEST_LIMIT_MESSAGE = """
Error: User has exceeded the daily rate limit

Please try again tomorrow
"""
