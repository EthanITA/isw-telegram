from Salesforce.Object.Course import Course


class Slide:
    def __init__(self, records: dict = None, _id=None):
        if _id is None:
            self.id = records.get('Id')
            self.name = records.get('Name')
            self.course = Course(_id=records.get('Course__c'))
            self.link = records.get('Link__c')
            self.access_count = records.get('Access_Count__c')
        else:
            self.id = _id
