class MessageMD:
    def __init__(self, *formatted_messages_md: str):
        self.formatted_messages_md: tuple[str] = formatted_messages_md
