import json

from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from keecenter.settings import BOT_TOKEN


def get_chat(chat_title):
    with open('static/bot_chats.json', 'r') as f:
        chats = json.load(f)

    if chat_title in chats:
        chat_id = chats[chat_title]
        return chat_id
    else:
        test_chat_id = chats['test']
        return test_chat_id


def do_start(update: Update):
    message = update.message
    if message.chat.type == 'group':
        chat_title = message.chat.title
    else:
        chat_title = message.chat.type + message.from_user

    with open('static/bot_chats.json', 'r') as f:
        chats = json.load(f)

    with open('static/bot_chats.json', 'w') as f:
        chats[chat_title] = message.chat_id
        json.dump(chats, f)

    bot.send_message(
        chat_id=message.chat_id,
        text='Chat added',
    )


def send_photo(photo, chat):
    chat_id = get_chat(chat)

    message = bot.send_photo(
        chat_id=chat_id,
        photo=photo
    )

    photo_hash = message.photo[-1].file_id
    return photo_hash


def send_file(document, chat):
    chat_id = get_chat(chat)

    message = bot.send_document(
        chat_id=chat_id,
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
