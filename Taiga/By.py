class By:
    def __init__(self, user: dict):
        self.link = user["permalink"]
        self.username = user["username"]
        self.full_name = user["full_name"]

