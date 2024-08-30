
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
import constants


dotenv.load_dotenv()
TOKEN: typing.Final = os.getenv("TOKEN")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_html("This is the help message")


# TODO use api calls passing long and latt
# into helpers functions to generate response

# function to handle the location sent by a user
async def weatherByLocation(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):
    user = update.message.from_user
    print(user)
    print(f"Longitude: {update.message.location.longitude}")
    print(f"Latitude: {update.message.location.latitude}")

    userData = {"name": f"{user.first_name} {user.last_name}",
                "id": user.id, "username": user.username,
                "longitude": update.message.location.longitude,
                "latitude": update.message.location.latitude}

    with open("userdata.json", "a") as jsonFile:
        jsonFile.write(json.dumps(userData))
        jsonFile.write("\n")

    weatherAPIData = helpers.getWeatherAPIReport(
        update.message.location.latitude, update.message.location.longitude)
    weatherAPIMessage = constants.weather_api_response.format(
        location=weatherAPIData[0],
        condition=weatherAPIData[1],
        temperature=weatherAPIData[2],
        feelsLike=weatherAPIData[3],
        wind=weatherAPIData[4],
        humidity=weatherAPIData[5],
        precipitation=weatherAPIData[6],
    )

    await update.message.reply_text(weatherAPIMessage)
    location_message = f"""Longitude: {update.message.location.longitude}
    Latitude: {update.message.location.latitude}
    """
    await update.message.reply_text()
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
                    weatherByLocation))

    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
