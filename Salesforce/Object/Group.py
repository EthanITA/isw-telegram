from Salesforce.Object.Course import Course


class Group:
    def __init__(self, _id,
                 group_name,
                 course: Course = None,
                 description=None,
                 tg_chat_id=None,
                 tg_link=None):
        self.id = _id
        self.group_name = group_name
        self.course: Course = course
        self.description = description
        self.tg_chat_id = tg_chat_id
        self.tg_link = tg_link
