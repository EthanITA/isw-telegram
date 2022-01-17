class Course:
    def __init__(self,
                 _id,
                 name,
                 about=None,
                 about_exam=None,
                 about_materials=None,
                 contents=None,
                 site=None):
        self.id = _id
        self.name = name
        self.about = about
        self.about_exam = about_exam
        self.about_materials = about_materials
        self.contents = contents
        self.site = site
