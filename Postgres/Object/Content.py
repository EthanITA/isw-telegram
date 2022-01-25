import Postgres


class Content:
    def __init__(self, records: dict = None):
        self.id: int = records.get('Id')
        self.name: str = records.get('ContentName')
        self.order: int = records.get('ContentOrder')
        self.course: int = records.get('Course')

    @staticmethod
    def get_contents(course_id) -> list:
        records = Postgres.query_all('SELECT * FROM "Content" where "Course"=%(value)s', {'value': course_id})
        return sorted([Content(content) for content in records], key=lambda x: x.order)

    @staticmethod
    def get_formatted_contents(course_id) -> str:
        contents = Content.get_contents(course_id)
        return '\n'.join([f'{content.order}. {content.name}' for content in contents])
