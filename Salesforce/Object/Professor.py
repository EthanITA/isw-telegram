from typing import List

from simple_salesforce import format_soql

from Salesforce import query_all
from Salesforce.Object.Group import Group
from Salesforce.Object.Manage import Manage


class Professor:
    def __init__(self, sf_records: dict = None, _id=None):
        if _id is None:
            self.id = sf_records.get('Id')
            self.first_name = sf_records.get('Name')
            self.email = sf_records.get('Email__c')
            self.website = sf_records.get('Website__c')
            self.manage: Manage = Manage(_id=sf_records.get('Manage__c'))
            self.last_name = sf_records.get('Last_Name__c')
            self.alias = sf_records.get('Alias__c')
            self.bio = sf_records.get('Bio__c')
            self.personal_website = sf_records.get('Personal_Website__c')
            self.phone = sf_records.get('Phone__c')
            self.tg_user_id = sf_records.get('Telegram_User_ID__c')
            self.tg_username = sf_records.get('Telegram_Username__c')
        else:
            self.id = _id

    @staticmethod
    def get_all_professors(course_id) -> List:
        groups: List[Group] = Group.get_groups([course_id])
        manages: List[Manage] = Manage.get_manages([g.id for g in groups])
        sf_query = query_all(format_soql(
            f"select id, first_name, last_name, email, website, manage__c, alias__c, bio__c, personal_website__c, phone__c, tg_user_id__c, tg_username__c "
            f"from professor__c where manage__c in {[m.id for m in manages]}"))
        return [Professor(query) for query in sf_query['records']]
