
LOGGING_FORMAT = "[%(asctime)s] [%(levelname)s] - %(message)s"
LOGGING_FILENAME = "logs/{filename}.log"

DB_NAME="weather_bot.db"

WEATHER_API_BASE_URL = "https://api.weatherapi.com/v1/current.json"

weather_api_response = """
WeatherAPI
Location: {location}
Conditions: {condition_text}
Temperature: {temperature}°C (Feels Like: {feels_like}°C)
Wind: {wind}
Humidity: {humidity}%
Precipitation: {precipitation}
"""


help_response_message = """
Here are the functions I'm currently capable of performing:

/help - The command you've just run

Share your location to get a local weather forecast
"""
