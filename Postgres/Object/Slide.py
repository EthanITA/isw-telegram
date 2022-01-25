class Slide:
    def __init__(self, records: dict = None, _id=None):
        self.id = records.get('Id')
        self.name = records.get('SlideName')
        self.course = records.get('Course')
        self.link = records.get('Link')
        self.access_count = records.get('AccessCount')
