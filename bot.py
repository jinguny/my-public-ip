import os
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from requests import get


logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


def start(update, context):
    update.message.reply_text("Hi")


def help_command(update, context):
    update.message.reply_text("Help!")


def echo(update, context):
    if update.message.from_user.id == int(os.environ["CHAT_ID"]):
        update.message.reply_text(get("https://api.ipify.org").text)
    else:
        update.message.reply_text(update.message.text)


def main():
    updater = Updater(os.environ["TOKEN"], use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()

    updater.idle()


if __name__ == "__main__":
    main()
