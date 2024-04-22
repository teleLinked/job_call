from pyrogram import Client

from decouple import config

from . import FORMATTED_TEXT_ALERT


API_ID = config("TELEGRAM_API_ID")
API_HASH = config("TELEGRAM_API_HASH")
BOT_TOKEN = config("TELEGRAM_BOT_TOKEN")
ADMIN_CHAT_ID = config("TELEGRAM_ADMIN_ID")

app = Client(name=".system-alert", api_id=API_ID,
             api_hash=API_HASH, bot_token=BOT_TOKEN)


def send_alert(data: dict):
    """ send alert notification on telegram """
    with app:
        app.send_message(chat_id=ADMIN_CHAT_ID, text=FORMATTED_TEXT_ALERT.format(
            platform=data['platform'],
            title=data['title'],
            category=data['category'],
            description=data['description'],
            location=data['location'],
            date=data['date'],
        ))
