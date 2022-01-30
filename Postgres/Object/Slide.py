from Postgres import query_all


class Slide:
    def __init__(self, records: dict = None, _id=None):
        self.id = records.get('Id')
        self.name = records.get('SlideName')
        self.course = records.get('Course')
        self.link = records.get('Link')
        self.access_count = records.get('AccessCount')
        self.order = records.get('SlideOrder')

    @property
    def formatted_text_md(self):
        return f"{self.order}. [{self.name}]({self.link})"

    @staticmethod
    def get_all_slides(course_id):
        records = query_all(
            'select * from "Slide" where "Course" = %(value)s',
            {"value": course_id})
        return sorted([Slide(record) for record in records], key=lambda x: x.order)
