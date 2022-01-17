from Salesforce.Object.Course import Course


class QuizSet:
    def __init__(self, records: dict = None, _id=None):
        if _id is None:
            self.id = records.get('Id')
            self.name = records.get('Name')
            self.course = Course(records.get('Course__c'))
        else:
            self.id = _id
