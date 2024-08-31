
import logging
import os
import time
import typing
import dotenv
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters
)

from constants import (
    help_response_message,
    weather_api_response,
    LOGGING_FILENAME,
    LOGGING_FORMAT
)
from classes.weatherapi import WeatherAPI
from classes.user import User


dotenv.load_dotenv()
TOKEN: typing.Final = os.getenv("TOKEN")

LOGGING_FILENAME = LOGGING_FILENAME.format(
    filename=time.strftime("%Y/%m/%d")
)

os.makedirs(
    os.path.dirname(LOGGING_FILENAME),
    exist_ok=True
)

logger = logging.getLogger(__name__)
logging.basicConfig(
    format=LOGGING_FORMAT,
    level=logging.INFO,
    filename=LOGGING_FILENAME
)


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_html(help_response_message)


async def get_weather_by_location(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):
    try:
        user = update.message.from_user
        print(user)
        longitude = update.message.location.longitude
        latitude = update.message.location.latitude

        print(f"Longitude: {longitude}")
        print(f"Latitude: {latitude}")

        user_obj = User(
            first_name=user.first_name,
            last_name=user.last_name,
            id=user.id,
            username=user.username
        )

        weatherAPI: WeatherAPI = WeatherAPI(
            latitude=latitude,
            longitude=longitude
        )

        weatherAPI_message = weather_api_response.format(**weatherAPI.__dict__)
        await update.message.reply_text(weatherAPI_message)

        location_message = f"Latitude: {latitude}\n"
        location_message += f"Longitude: {longitude}\n"
        await update.message.reply_text(location_message)

    except Exception as e:
        logger.error(e)
        await update.message.reply_text("Error: something went wrong")


# TODO just for testing, remove this eventually
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)


def main() -> None:
    app: Application = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("help", help))

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            echo
        )
    )

    app.add_handler(
        MessageHandler(
            filters.LOCATION & ~filters.COMMAND,
            get_weather_by_location
        )
    )

    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
