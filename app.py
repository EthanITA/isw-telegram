from flask import Flask, request
from telegram import Bot
from telegram.ext import Updater

import Telegram.Commands

isw_bot = Bot(Telegram.api_key)

updater = Updater(token=Telegram.api_key, use_context=True)
dispatcher = updater.dispatcher

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World!"


@app.route(f"/taiga", methods=["POST"])
def callback():
    print(request.data)
    print(request.headers)


print("Bot started!")
