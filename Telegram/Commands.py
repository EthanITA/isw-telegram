from telegram import Update
from telegram.ext import CallbackContext

from Salesforce.Object.Course import Course
from Salesforce.Object.Professor import Professor

course_id = "a017Q00000JZn8qQAD"


def contacts(update: Update, context: CallbackContext):
    for professor in Professor.get_all_professors(course_id):
        print(professor.get_formatted_contacts())
        context.bot.send_message(chat_id=update.effective_chat.id, text=professor.get_formatted_contacts())


def books(update: Update, context: CallbackContext):
    for book in Course.get_books(course_id):
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"{book}")


def contents(update: Update, context: CallbackContext):
    for content in Course.get_contents(course_id):
        context.bot.send_message(chat_id=update.effective_chat.id, text=content)


# the list has to be in this format:
# command_name, command_description, callback_function
# !important the command_name must be in lowercase
list = sorted([

    ('contacts', 'Get professors\' contacts', contacts),
    ('books', 'Get course\' books', books),
    ('contents', 'Get course\' contents', contents)
], key=lambda command: command[1])
