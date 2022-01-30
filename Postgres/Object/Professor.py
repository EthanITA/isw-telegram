from typing import List

from Postgres import query_all


class Professor:
    def __init__(self, sf_records: dict = None, _id=None):
        self.id = sf_records.get('Id')
        self.first_name = sf_records.get('FirstName')
        self.email = sf_records.get('Email')
        self.website = sf_records.get('Website')
        self.last_name = sf_records.get('LastName')
        self.personal_website = sf_records.get('Personal Website')
        self.phone = sf_records.get('Phone')
        self.tg_user_id = sf_records.get('Telegram UserID')
        self.tg_username = sf_records.get('Telegram Username')

    @property
    def formatted_contacts_text(self):
        text = f"Prof. {self.last_name}: {self.email}" \
               f"\nSito UNIBO: {self.website}"
        if self.phone:
            text += f"\nTelefono: {self.phone}"
        if self.personal_website:
            text += f"\nSito personale: {self.personal_website}"
        return text

    @staticmethod
    def get_all_professors(course_id) -> List:
        records = query_all(
            'select * from "Professor" where "Course" = %(value)s',
            {"value": course_id})
        return [Professor(record) for record in records]
