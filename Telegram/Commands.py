from telegram import Update
from telegram.ext import CallbackContext

from Postgres.Object.Book import Book
from Postgres.Object.Content import Content
from Postgres.Object.Professor import Professor

course_id = "1"


def contacts(update: Update, context: CallbackContext):
    for professor in Professor.get_all_professors(course_id):
        context.bot.send_message(chat_id=update.effective_chat.id, text=professor.get_formatted_contacts())


def books(update: Update, context: CallbackContext):
    for book in Book.get_books(course_id):
        context.bot.send_message(chat_id=update.effective_chat.id, text=book.name)


def contents(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=Content.get_formatted_contents(course_id))


# the list has to be in this format:
# command_name, command_description, callback_function
# !important the command_name must be in lowercase
list = sorted([

    ('contacts', 'Get professors\' contacts', contacts),
    ('books', 'Get course\' books', books),
    ('contents', 'Get course\' contents', contents)
], key=lambda command: command[1])
