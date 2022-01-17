from typing import List

from Salesforce.Object.QuizSet import QuizSet


class Quiz:
    def __init__(self, records: dict = None, _id=None):
        if _id is None:
            self.id = records['Id']
            self.name = records['Name']
            self.quiz_set: QuizSet = QuizSet(records['Quiz_Set__c'])
            self.question = records['Question__c']
            self.choices: List[str] = [record for record in records['Choices__c'].split('\n')
                                       if record.split() != '']
            self.solutions: List[str] = [record for record in records['Solutions__c'].split('\n')
                                         if record.split() != '']
        else:
            self.id = _id
