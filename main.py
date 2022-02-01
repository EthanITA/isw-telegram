from telegram import Bot, BotCommand
from telegram.ext import CommandHandler
from telegram.ext import Updater

import Telegram.Commands

isw_bot = Bot(Telegram.api_key)

updater = Updater(token=Telegram.api_key, use_context=True)
dispatcher = updater.dispatcher

bot_commands = [BotCommand(name, desc) for name, desc, callback in Telegram.Commands.list_of_commands]

for name, desc, callback in Telegram.Commands.list_of_commands:
    dispatcher.add_handler(CommandHandler(name, callback))
updater.bot.set_my_commands(commands=bot_commands)

updater.start_polling()

print("Bot started!")