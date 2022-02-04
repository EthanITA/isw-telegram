from Taiga import By, Type


class Data:
    def __init__(self, data: dict, type: str, change, action: dict):
        self.link = data["permalink"]
        self.project_link = data["project"]["permalink"]
        self.project_name = data["project"]["name"]
        self.owner = By(data["owner"])
        match type:
            case Type.milestone:
                self.milestone = Type.Milestone(data, action, change)
            case Type.userstory:
                self.userstory = Type.UserStory(data, action, change)
            case Type.task:
                self.task = Type.Task(data, action, change)
            case Type.issue:
                self.issue = Type.Issue(data, action, change)
            case Type.wiki:
                self.wiki = Type.Wiki(data, action, change)
