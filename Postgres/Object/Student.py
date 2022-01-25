class Student:
    def __init__(self, records):
        self.id = records.get('Id')
        self.first_name = records.get('FirstName')
        self.last_name = records.get('LastName')
        self.course = records.get('Course')
        self.telegram_user_id = records.get('Telegram UserID')
        self.telegram_username = records.get('Telegram Username')
