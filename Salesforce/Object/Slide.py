from Salesforce.Object.Course import Course


class Slide:
    def __init__(self, records: dict = None, _id=None):
        if _id is None:
            self.id = records['Id']
            self.name = records['Name']
            self.course = Course(records['Course__c'])
            self.link = records['Link__c']
            self.access_count = records['Access_Count__c']
        else:
            self.id = _id
