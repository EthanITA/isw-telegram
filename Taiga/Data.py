from Taiga import By, Type


class Data:
    def __init__(self, data: dict, type: str, change):
        self.link = data["permalink"]
        self.project_link = data["project"]["permalink"]
        self.project_name = data["project"]["name"]
        self.owner = By(data["owner"])
        match type:
            case Type.milestone:
                self.milestone = Type.Milestone(data, change)
            case Type.userstory:
                self.userstory = Type.UserStory(data, change)
            case Type.task:
                self.task = Type.Task(data, change)
            case Type.issue:
                self.issue = Type.Issue(data, change)
            case Type.wiki:
                self.wiki = Type.Wiki(data, change)



