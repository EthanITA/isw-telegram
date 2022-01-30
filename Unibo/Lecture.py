from datetime import datetime

import requests


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
        info = f"Corso: *{self.title}*\n" \
               f"Docente: *{self.professor}*\n" \
               f"Location: *{self.building}*,  _{self.address}_\n" \
               f"Giorno: *{self.start_time.strftime('%d/%m/%Y')}*\n" \
               f"Orario: *{self.time}*\n"
        if self.teams_link is not None:
            info += f"Teams: [Link]({self.teams_link})"
        return info
