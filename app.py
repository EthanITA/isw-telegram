import json

from flask import Flask, request
from telegram import Bot
from telegram.ext import Updater

import Telegram

isw_bot = Bot(Telegram.api_key)

updater = Updater(token=Telegram.api_key, use_context=True)
dispatcher = updater.dispatcher

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World!"


@app.route(f"/taiga/<chat_id>", methods=["POST"])
def callback(chat_id):
    data = json.loads(request.data)
    print(f'Progetto: {data["data"]["project"]["name"]}')
    try:
        isw_bot.send_message(chat_id=chat_id, text=f'Progetto: {data["data"]["project"]["name"]}')
    except Exception as e:
        print(e)

    return 200


print("Bot started!")
