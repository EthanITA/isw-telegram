class MessageMD:
    def __init__(self, message_md=None, changes_md=None):
        self.message_md = message_md
        self.changes_md = changes_md

    @property
    def format_message_md(self):
        return self.message_md

    @property
    def format_changes_md(self):
        return self.changes_md
