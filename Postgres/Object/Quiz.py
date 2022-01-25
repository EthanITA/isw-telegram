from typing import List


class Quiz:
    def __init__(self, records: dict = None, _id=None):
        self.id = records.get('Id')
        self.name = records.get('QuizName')
        self.quiz_set: int = records.get('Quiz Set')
        self.question = records.get('Question')
        self.choices: List[str] = [record for record in records.get('Choices__c').split('\n')
                                   if record.split() != '']
        self.solutions: List[str] = [record for record in records.get('Solutions__c').split('\n')
                                     if record.split() != '']
