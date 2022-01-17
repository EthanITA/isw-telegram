from Salesforce.Object.Course import Course


class QuizSet:
    def __init__(self, _id, name, course: Course):
        self.id = _id
        self.name = name
        self.course = course
