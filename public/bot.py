import json

from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from keecenter.settings import BOT_TOKEN


def send_photo(photo, chat):
    nonlocal bot
    message = bot.send_photo(
        chat_id=chat,
        photo=photo
    )
    photo_hash = message.photo[-1].file_id
    return photo_hash


def send_file(document, chat):
    nonlocal bot
    message = bot.send_document(
        chat_id=chat,
        document=document
    )
    file_hash = message.document.file_id
    return file_hash


def get_photo(photo_hash):
    pass


def get_file(photo_hash):
    pass


bot = Bot(
    token=BOT_TOKEN,
)
