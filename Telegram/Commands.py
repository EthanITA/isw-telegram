from telegram import Update
from telegram.ext import CallbackContext

from Salesforce.Object.Professor import Professor


def contacts(update: Update, context: CallbackContext):
    for professor in Professor.get_all_professors("a017Q00000JZn8qQAD"):
        print(professor.get_formatted_contacts())
        context.bot.send_message(chat_id=update.effective_chat.id, text=professor.get_formatted_contacts())


# the list has to be in this format:
# command_name, command_description, callback_function
# !important the command_name must be in lowercase
list = sorted([

    ('contacts', 'Get professors\' contacts', contacts),

], key=lambda command: command[1])
