import Postgres


class Content:
    def __init__(self, records: dict = None):
        self.id: int = records.get('Id')
        self.name: str = records.get('ContentName')
        self.order: int = records.get('ContentOrder')
        self.course: int = records.get('Course')

    @staticmethod
    def get_all_contents(course_id) -> list:
        records = Postgres.query_all('SELECT * FROM "Content" where "Course"=%(value)s', {'value': course_id})
        return sorted([Content(content) for content in records], key=lambda x: x.order)

    @property
    def formatted_text(self) -> str:
        return f'{self.order}. {self.name}'
