
import json
import logging
import os
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

import helpers
from constants import (
    help_response_message,
    weather_api_response
)
from classes.weatherapi import WeatherAPI


dotenv.load_dotenv()
TOKEN: typing.Final = os.getenv("TOKEN")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_html(help_response_message)


async def get_weather_by_location(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):
    user = update.message.from_user
    print(user)
    longitude = update.message.location.longitude
    latitude = update.message.location.latitude

    print(f"Longitude: {longitude}")
    print(f"Latitude: {latitude}")

    userData = {
        "name": f"{user.first_name} {user.last_name}",
        "id": user.id, "username": user.username,
        "longitude": update.message.location.longitude,
        "latitude": update.message.location.latitude
    }

    weatherAPI: WeatherAPI = WeatherAPI(
        latitude=latitude,
        longitude=longitude
    )

    weatherAPIMessage = weather_api_response.format(
        location=weatherAPI.location,
        condition=weatherAPI.condition,
        temperature=weatherAPI.temperature,
        feels_like=weatherAPI.feels_like,
        wind=weatherAPI.wind,
        humidity=weatherAPI.humidity,
        precipitation=weatherAPI.precipitation,
    )

    await update.message.reply_text(weatherAPIMessage)

    location_message = f"Latitude: {latitude}\n"
    location_message += f"Longitude: {longitude}\n"
    await update.message.reply_text(location_message)


# TODO just for testing, remove this eventually
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)


def main() -> None:
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("help", help))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    app.add_handler(MessageHandler(
                    filters.LOCATION & ~filters.COMMAND,
                    get_weather_by_location))

    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
