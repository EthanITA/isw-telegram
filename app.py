import json

from flask import Flask, request
from telegram import Bot
from telegram.constants import PARSEMODE_MARKDOWN_V2
from telegram.ext import Updater

import Telegram
from Gitlab import Gitlab
from Taiga import Taiga

isw_bot = Bot(Telegram.api_key)

updater = Updater(token=Telegram.api_key, use_context=True)
dispatcher = updater.dispatcher

app = Flask(__name__)


@app.route("/gitlab/<chat_id>", methods=["POST"])
def gitlab_callback(chat_id):
    payload = json.loads(request.data)
    gitlab = Gitlab(payload)
    event = gitlab.get_event()
    try:
        isw_bot.send_message(chat_id=chat_id, text=event.formatted_message_md, parse_mode=PARSEMODE_MARKDOWN_V2,
                             disable_web_page_preview=True)
        isw_bot.send_message(chat_id=chat_id, text=event.formatted_commits_md, parse_mode=PARSEMODE_MARKDOWN_V2,
                             disable_web_page_preview=True)
    except Exception as e:
        print(e)
    return "OK"


@app.route(f"/taiga/<chat_id>", methods=["POST"])
def taiga_callback(chat_id):
    payload = json.loads(request.data)
    taiga = Taiga(payload)
    message, changes = taiga.format_message_md()
    try:
        if message is not None:
            isw_bot.send_message(chat_id=chat_id, text=message, parse_mode=PARSEMODE_MARKDOWN_V2)
        if changes is not None:
            isw_bot.send_message(chat_id=chat_id, text=changes)
    except Exception as e:
        print(e)

    return "OK"


print("Bot started!")
