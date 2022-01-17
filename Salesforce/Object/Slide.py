from Salesforce.Object.Course import Course


class Slide:
    def __init__(self,
                 _id,
                 name,
                 course: Course,
                 link,
                 access_count: int):
        self.id = _id
        self.name = name
        self.course = course
        self.link = link
        self.access_count = access_count
