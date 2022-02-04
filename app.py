import json
from datetime import datetime

from flask import Flask, request
from telegram import Bot
from telegram.ext import Updater

import Helper
import Telegram
from Taiga import Taiga

isw_bot = Bot(Telegram.api_key)

updater = Updater(token=Telegram.api_key, use_context=True)
dispatcher = updater.dispatcher

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World!"


@app.route(f"/taiga/<chat_id>", methods=["POST"])
def taiga_callback(chat_id):
    payload = json.loads(request.data)
    taiga = Taiga(payload)

    try:
        isw_bot.send_message(chat_id=chat_id, text=taiga.format_message_md(), parse_mode="Markdown")
    except Exception as e:
        print(e)

    return "OK"


print("Bot started!")
