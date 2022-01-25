class QuizSet:
    def __init__(self, records: dict = None, _id=None):
        self.id = records.get('Id')
        self.name = records.get('QuizSetName')
        self.course = records.get('Course')
