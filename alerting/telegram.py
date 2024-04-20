from pyrogram import Client
from . import FORMATTED_TEXT_ALERT

app = Client(name=".system-alert", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


def send_alert(data: dict):
    app.send_message(chat_id=ADMIN_CHAT_ID, text=FORMATTED_TEXT_ALERT.format(
        platform=data['platform'],
        title=data['title'],
        category=data['category'],
        description=data['description'],
        location=data['location'],
        date=data['date'],
    ))
