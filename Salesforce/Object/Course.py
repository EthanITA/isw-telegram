class Course:
    def __init__(self, records: dict = None, _id=None):
        if _id is None:
            self.id = records.get('Id')
            self.name = records.get('Name')
            self.about = records.get('About__c')
            self.about_exam = records.get('About_Exam__c')
            self.about_materials = records.get('About_Materials__c')
            self.contents = records.get('Contents__c')
            self.site = records.get('Site__c')
        else:
            self.id = _id
