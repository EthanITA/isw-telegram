class Course:
    def __init__(self, records: dict = None):
        self.id: int = records.get('Id')
        self.name: str = records.get('CourseName')
        self.about: str = records.get('About')
        self.about_exam: str = records.get('About Exam')
        self.site: str = records.get('Site')
