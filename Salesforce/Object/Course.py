import Salesforce


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

    @staticmethod
    def get_books(course_id):
        records = Salesforce.query_all(f"SELECT Id, About_Materials__c FROM Course__c where id='{course_id}'")['records']
        return [str(book) for book in records[0]['About_Materials__c'].split('\n')]

    @staticmethod
    def get_contents(course_id):
        records = Salesforce.query_all(f"SELECT Id, Contents__c FROM Course__c where id='{course_id}'")['records']
        return [str(content) for content in records[0]['Contents__c'].split('\n')]