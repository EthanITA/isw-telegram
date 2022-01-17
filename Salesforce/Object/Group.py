from typing import List

from Salesforce import query_all
from Salesforce.Object.Course import Course


class Group:
    def __init__(self, records: dict = None, _id=None):
        if _id is None:
            self.id = records['Id']
            self.group_name = records['Name']
            self.course: Course = Course(records['Course__c'])
            self.description = records['Description__c']
            self.tg_chat_id = records['Telegram_Chat_Id__c']
            self.tg_link = records['Telegram_Link__c']
        else:
            self.id = _id

    @staticmethod
    def get_groups(course_id: List[str]) -> list:
        sf_query = query_all(
            f"SELECT Id, Name, Description__c, Course__c, Course__r.Name "
            f"FROM Group__c WHERE Course__c in {course_id}"
        )
        return [Course(query) for query in sf_query['records']]
