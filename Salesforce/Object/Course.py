class Course:
    def __init__(self, records: dict = None, _id=None):
        if _id is None:
            self.id = records['Id']
            self.name = records['Name']
            self.about = records['About__c']
            self.about_exam = records['About_Exam__c']
            self.about_materials = records['About_Materials__c']
            self.contents = records['Contents__c']
            self.site = records['Site__c']
        else:
            self.id = _id
