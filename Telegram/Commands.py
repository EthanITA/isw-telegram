from datetime import datetime

import requests
from telegram import Update
from telegram.ext import CallbackContext

from Postgres.Object.Book import Book
from Postgres.Object.Content import Content
from Postgres.Object.Professor import Professor

course_id = "1"


class Lecture:
    def __init__(self, lecture_data):
        self.title = lecture_data.get("title")
        self.period = lecture_data.get("periodo")
        self.address = lecture_data.get("aule")[0].get("des_indirizzo")
        self.building = lecture_data.get("aule")[0].get("des_edificio")
        self.teams_link = lecture_data.get("teams")
        self.professor = lecture_data.get("docente")
        self.start_time = datetime.strptime(lecture_data.get("start"), "%Y-%m-%dT%H:%M:%S")
        self.end_time = datetime.strptime(lecture_data.get("end"), "%Y-%m-%dT%H:%M:%S")
        self.time = lecture_data.get("time")

    @staticmethod
    def get_all_lectures():
        data = requests.get("https://corsi.unibo.it/laurea/informatica/orario-lezioni/@@orario_reale_json?anno=3")
        if data.status_code == 200:
            return sorted([Lecture(lecture_data) for lecture_data in data.json()
                           if "ingegneria del software" in lecture_data.get("title").lower()],
                          key=lambda x: x.start_time)

    def get_formatted_info(self):
        return f"Corso: *{self.title}*\n" \
               f"Location: *{self.building}*,  _{self.address}_\n" \
               f"Giorno: *{self.start_time.strftime('%d/%m/%Y')}*\n" \
               f"Orario: *{self.time}*\n"


def contacts(update: Update, context: CallbackContext):
    for professor in Professor.get_all_professors(course_id):
        context.bot.send_message(chat_id=update.effective_chat.id, text=professor.get_formatted_contacts())


def books(update: Update, context: CallbackContext):
    for book in Book.get_books(course_id):
        context.bot.send_message(chat_id=update.effective_chat.id, text=book.name)


def contents(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=Content.get_formatted_contents(course_id))


def get_next_lecture_info(update: Update, context: CallbackContext):
    lectures = Lecture.get_all_lectures()
    lecture = [lec for lec in lectures if lec.start_time > datetime.now()]
    if len(lecture) > 0:
        lecture = lecture[0]
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Non ci sono lezioni in programma, l'ultima lezione è stata la seguente:")
        lecture = lectures[-1]
    context.bot.send_message(chat_id=update.effective_chat.id, text=lecture.get_formatted_info(), parse_mode="Markdown")


# the list has to be in this format:
# command_name, command_description, callback_function
# !important the command_name must be in lowercase
list = sorted([

    ('contacts', 'Get professors\' contacts', contacts),
    ('books', 'Get course\' books', books),
    ('contents', 'Get course\' contents', contents),
    ('next_lecture', 'Get next lecture info', get_next_lecture_info)
], key=lambda command: command[1])
