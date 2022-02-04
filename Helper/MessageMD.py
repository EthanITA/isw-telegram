class MessageMD:
    def __init__(self, message=None):
        self.message_md = str(message)

    @property
    def format_message_md(self):
        return self.message_md
