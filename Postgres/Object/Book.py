import Postgres


class Book:
    def __init__(self, records: dict = None):
        self.id: int = records.get('Id')
        self.name: str = records.get('BookName')
        self.order: int = records.get('BookOrder')
        self.course: int = records.get('Course')

    @staticmethod
    def get_all_books(course_id):
        records = Postgres.query_all('SELECT * FROM "Book" where "Course"=%(value)s', {'value': course_id})
        return sorted([Book(book) for book in records], key=lambda x: x.order)
