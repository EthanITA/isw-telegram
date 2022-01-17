from Salesforce.Object.QuizSet import QuizSet


class Quiz:
    def __init__(self,
                 _id,
                 name,
                 quiz_set: QuizSet,
                 question,
                 choices: list[str],
                 solutions: list[str]):
        self.id = _id
        self.name = name
        self.quiz_set: QuizSet = quiz_set
        self.question = question
        self.choices = choices
        self.solutions = solutions
