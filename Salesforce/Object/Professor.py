from typing import List

from Salesforce import query_all
from Salesforce.Object.Course import Course


class Professor:
    def __init__(self, sf_records: dict = None, _id=None):
        if _id is None:
            self.id = sf_records.get('Id')
            self.first_name = sf_records.get('Name')
            self.email = sf_records.get('Email__c')
            self.website = sf_records.get('Website__c')
            self.course: Course = Course(_id=sf_records.get('Course__c'))
            self.last_name = sf_records.get('Last_Name__c')
            self.alias = sf_records.get('Alias__c')
            self.bio = sf_records.get('Bio__c')
            self.personal_website = sf_records.get('Personal_Website__c')
            self.phone = sf_records.get('Phone__c')
            self.tg_user_id = sf_records.get('Telegram_User_ID__c')
            self.tg_username = sf_records.get('Telegram_Username__c')
        else:
            self.id = _id

    def get_formatted_contacts(self):
        text = f"Prof. {self.last_name}: {self.email}" \
               f"\nSito UNIBO: {self.website}"
        if self.phone:
            text += f"\nTelefono: {self.phone}"
        if self.personal_website:
            text += f"\nSito personale: {self.personal_website}"
        return text

    @staticmethod
    def get_all_professors(course_id) -> List:
        sf_query = query_all(
            "select id, name, last_name__c, email__c, website__c, course__c, alias__c, bio__c, personal_website__c, phone__c, telegram_user_id__c, telegram_username__c from professor__c where course__c in {course_id}",
            course_id=[course_id])
        return [Professor(query) for query in sf_query['records']]
