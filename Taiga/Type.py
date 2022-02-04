milestone = "milestone"
userstory = "userstory"
task = "task"
issue = "issue"
wiki = "wikipage"
test = "test"


class Milestone:
    def __init__(self, payload):
        self.link = payload["permalink"]
        self.name = payload["name"]
        self.slug = payload["slug"]
        self.estimated_start = payload["estimated_start"]
        self.estimated_finish = payload["estimated_finish"]
        self.closed = payload["is_closed"]
        self.disponibility = payload["disponibility"]


class UserStory:
    def __init__(self, payload):
        self.tags: list[str] = payload["tags"]
        self.link = payload["permalink"]
        self.points: list[dict] = payload["points"]
        self.status = payload["status"]["name"]
        self.subject = payload["subject"]
        self.description = payload["description"]
        if payload.get("milestone"):
            self.milestone = Milestone(payload["milestone"])


class Task:
    def __init__(self, payload):
        self.tags: list[str] = payload["tags"]
        self.link = payload["permalink"]
        self.status = payload["status"]["name"]
        self.subject = payload["subject"]
        self.description = payload["description"]
        if payload.get("milestone"):
            self.milestone = Milestone(payload["milestone"])
        if payload.get("user_story"):
            self.user_story = UserStory(payload["user_story"])
        self.us_order = payload["us_order"]


class Issue:
    def __init__(self, payload):
        self.tags: list[str] = payload["tags"]
        self.link = payload["permalink"]
        self.status = payload["status"]["name"]
        self.subject = payload["subject"]
        self.description = payload["description"]
        if payload.get("milestone"):
            self.milestone = Milestone(payload["milestone"])
        self.type = payload["type"]["name"]
        self.priority = payload["priority"]["name"]
        self.severity = payload["severity"]["name"]


class Wiki:
    def __init__(self, payload):
        self.link = payload["permalink"]
        self.slug = payload["slug"]
        self.content = payload["content"]
