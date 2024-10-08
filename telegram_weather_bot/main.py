
import logging
import os
import time
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
    LOGGING_FILENAME,
    LOGGING_FORMAT,
    USER_REQUEST_LIMIT_MESSAGE,
    HELP_RESPONSE_MESSAGE,
    INTERNAL_SERVER_ERROR_MESSAGE,
)
from classes.weatherapi import WeatherAPI
from helpers import check_is_user_valid


dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN")

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
    await update.message.reply_html(HELP_RESPONSE_MESSAGE)


async def get_weather_by_location(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):
    try:
        user = update.message.from_user
        logger.info(user)
        longitude = update.message.location.longitude
        latitude = update.message.location.latitude

        logger.info(f"Longitude: {longitude}")
        logger.info(f"Latitude: {latitude}")

        user_dict = {
            "name": user.full_name,
            "username": user.name,
            "external_id": user.id,
        }

        is_user_valid = check_is_user_valid(user_data=user_dict)

        if is_user_valid:
            weatherAPI: WeatherAPI = WeatherAPI(
                latitude=latitude,
                longitude=longitude
            )

            await update.message.reply_text(
                weatherAPI.gen_weather_message()
            )

            location_message = f"Latitude: {latitude}\n"
            location_message += f"Longitude: {longitude}\n"
            await update.message.reply_text(location_message)

        else:
            await update.message.reply_text(USER_REQUEST_LIMIT_MESSAGE)

    except Exception as e:
        logger.error(e)
        await update.message.reply_text(INTERNAL_SERVER_ERROR_MESSAGE)


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
