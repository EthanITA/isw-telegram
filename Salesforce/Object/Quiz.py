from typing import List

from Salesforce.Object.QuizSet import QuizSet


class Quiz:
    def __init__(self, records: dict = None, _id=None):
        if _id is None:
            self.id = records.get('Id')
            self.name = records.get('Name')
            self.quiz_set: QuizSet = QuizSet(_id=records.get('Quiz_Set__c'))
            self.question = records.get('Question__c')
            self.choices: List[str] = [record for record in records.get('Choices__c').split('\n')
                                       if record.split() != '']
            self.solutions: List[str] = [record for record in records.get('Solutions__c').split('\n')
                                         if record.split() != '']
        else:
            self.id = _id
