from typing import List

from Salesforce import query_all
from Salesforce.Object.Group import Group


class Manage:
    def __init__(self, records: dict = None, _id=None):
        if _id is None:
            self.id = records['Id']
            self.name = records['Name']
            self.group: Group = Group(records['Group__c'])
        else:
            self.id = _id

    @staticmethod
    def get_manages(groups_id: List[str]) -> List:
        sf_query = query_all(f"select Id, Name, Group__c from Manage__c where Group__c in {groups_id}")
        return [Manage(query) for query in sf_query['records']]
