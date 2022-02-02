import json
from datetime import datetime

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
def taiga_callback(chat_id):
    data = json.loads(request.data)
    board = data["data"]["project"]["name"]
    action = data["action"]
    type = data["type"]
    user = data["by"]["full_name"]
    link = data["data"]["project"]["permalink"]
    date = datetime.strptime(data["date"], "%Y-%m-%dT%H:%M:%S.%fZ")

    print(data)
    text = f"*{user}* ha fatto una *{action}* di *{type}* sulla board [*{board}*]({link}) " \
           f"alle *{date.strftime('%H:%M')}* del *{date.strftime('%d/%m/%Y')}*"
    try:
        isw_bot.send_message(chat_id=chat_id, text=text)
    except Exception as e:
        print(e)

    return "OK"


print("Bot started!")
