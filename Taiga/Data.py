from Taiga import By, Type


class Data:
    def __init__(self, data: dict, type: str):
        self.link = data["permalink"]
        self.project_link = data["project"]["permalink"]
        self.project_name = data["project"]["name"]
        self.owner = By(data["owner"])
        self.name = data["name"]
        match type:
            case Type.milestone:
                self.milestone = Type.Milestone(data)
            case Type.userstory:
                self.user_story = Type.UserStory(data)
            case Type.task:
                self.task = Type.Task(data)
            case Type.issue:
                self.issue = Type.Issue(data)
            case Type.wiki:
                self.wiki = Type.Wiki(data)



