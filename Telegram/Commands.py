from datetime import datetime

from telegram import Update
from telegram.ext import CallbackContext

from Postgres.Object.Book import Book
from Postgres.Object.Content import Content
from Postgres.Object.Professor import Professor
from Postgres.Object.Slide import Slide
from Unibo.Lecture import Lecture

course_id = "1"


def get_professor_contacts(update: Update, context: CallbackContext):
    for professor in Professor.get_all_professors(course_id):
        context.bot.send_message(chat_id=update.effective_chat.id, text=professor.formatted_contacts_text)


def get_books(update: Update, context: CallbackContext):
    for book in Book.get_all_books(course_id):
        context.bot.send_message(chat_id=update.effective_chat.id, text=book.name)


def get_contents(update: Update, context: CallbackContext):
    contents = [content.formatted_text for content in Content.get_all_contents(course_id)]

    context.bot.send_message(chat_id=update.effective_chat.id, text="\n".join(contents))


def get_next_lecture_info(update: Update, context: CallbackContext):
    lectures = Lecture.get_all_lectures()
    lecture = [lec for lec in lectures if lec.start_time > datetime.now()]
    if len(lecture) > 0:
        lecture = lecture[0]
    else:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Non ci sono lezioni in programma, l'ultima lezione è stata la seguente:")
        lecture = lectures[-1]
    context.bot.send_message(chat_id=update.effective_chat.id, text=lecture.get_formatted_info(), parse_mode="Markdown")


def get_slides(update: Update, context: CallbackContext):
    slides = [slide.formatted_text_md for slide in Slide.get_all_slides(course_id)]
    context.bot.send_message(chat_id=update.effective_chat.id, text="\n".join(slides), parse_mode="Markdown",
                             disable_web_page_preview=True)


def get_help(update: Update, context: CallbackContext):
    global list_of_commands
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="\n".join([f"/{command} : {descr}" for command, descr, _ in list_of_commands]))


def generate_taiga_webhooks(update: Update, context: CallbackContext):
    heroku_app = "https://isw-bot.herokuapp.com"
    help = "Go in your Taiga Board settings -> Integrations -> Webhooks\n" \
           "Choose a name you like, put whatever you want as secret key and add the following Payload URL: "
    webhook = f"{heroku_app}/taiga/{update.effective_chat.id}"
    context.bot.send_message(chat_id=update.effective_chat.id, text=help)
    context.bot.send_message(chat_id=update.effective_chat.id, text=webhook)


def generate_gitlab_webhooks(update: Update, context: CallbackContext):
    heroku_app = "https://isw-bot.herokuapp.com"
    help = "Go in your GitLab Project settings -> Webhooks\n" \
           "Add the following URL: "
    webhook = f"{heroku_app}/gitlab/{update.effective_chat.id}"
    add_help = "The following events are supported: \n" \
               "* Push events\n" \
               "* Issue events\n" \
               "* Comment events\n" \
               "* Merge request events\n" \
               "* Wiki page events"
    context.bot.send_message(chat_id=update.effective_chat.id, text=help)
    context.bot.send_message(chat_id=update.effective_chat.id, text=webhook)
    context.bot.send_message(chat_id=update.effective_chat.id, text=add_help)


# the list has to be in this format:
# command_name, command_description, callback_function
# !important the command_name must be in lowercase
list_of_commands = sorted([

    ('contacts', 'Get professors\' contacts', get_professor_contacts),
    ('books', 'Get course\' books', get_books),
    ('contents', 'Get course\' contents', get_contents),
    ('next_lecture', 'Get next lecture info', get_next_lecture_info),
    ('slides', 'Get slides', get_slides),
    ('help', 'Get list of available commands', get_help),
    ('taiga_webhook', 'Generate Taiga webhooks', generate_taiga_webhooks),
    ('gitlab_webhook', 'Generate GitLab webhooks', generate_gitlab_webhooks)
], key=lambda command: command[1])
