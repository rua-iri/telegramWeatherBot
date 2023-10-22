
import json
import logging
import os
import typing
import dotenv
from telegram import Update
from telegram.ext import (Application, CommandHandler, ContextTypes,
                          MessageHandler, filters)


dotenv.load_dotenv()
TOKEN: typing.Final = os.getenv("TOKEN")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_html("This is the help message")


# TODO make api calls using the data from this 
# function to handle the location sent by a user
async def weatherByLocation(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"{update.message.location.longitude} \n {update.message.location.latitude}")


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
