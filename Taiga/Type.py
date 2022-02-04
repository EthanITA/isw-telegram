from Taiga import Action

milestone = "milestone"
userstory = "userstory"
task = "task"
issue = "issue"
wiki = "wikipage"
test = "test"


def get_changes(changes):
    if changes is not None:
        text = ""
        for name, change in changes["diff"].items():
            text += f"*{name}*\n\t {change['from']} --> {change['to']}\n"
        return text
    else:
        return ""

class FormatAction:
    def __init__(self, action, create, delete, change):
        self.action = action
        self.create = create
        self.delete = delete
        self.change = change

    @property
    def message(self):
        match self.action:
            case Action.create:
                return self.create
            case Action.delete:
                return self.delete
            case Action.change:
                return self.change


class Milestone:
    def __init__(self, payload, changes=None):
        self.link = payload["permalink"]
        self.name = payload["name"]
        self.slug = payload["slug"]
        self.estimated_start = payload["estimated_start"]
        self.estimated_finish = payload["estimated_finish"]
        self.disponibility = payload["disponibility"]
        self.changes = changes

    @property
    def _create_message_md(self):
        return f"The milestone [{self.name}]({self.link}) has been created"

    @property
    def _delete_message_md(self):
        return f"The milestone [{self.name}]({self.link}) has been deleted"

    @property
    def _change_message_md(self):
        text = f"The milestone [{self.name}]({self.link}) has been changed\n\n"
        return text + get_changes(self.changes)

    def format_message_md(self, action):
        return FormatAction(action,
                            self._create_message_md,
                            self._delete_message_md,
                            self._change_message_md).message


class UserStory:
    def __init__(self, payload, changes=None):
        self.tags: list[str] = payload["tags"]
        self.link = payload["permalink"]
        self.points: list[dict] = payload["points"]
        self.status = payload["status"]["name"]
        self.subject = payload["subject"]
        self.description = payload["description"]
        self.changes = changes
        self.milestone = Milestone(payload["milestone"]) if payload.get("milestone") else None

    @property
    def _create_message_md(self):
        mess = f"*[{self.status}]* The user story [{self.subject}]({self.link}) has been created"
        if self.milestone:
            mess = f"{mess} with milestone [{self.milestone.name}]({self.milestone.link})"
        return mess

    @property
    def _delete_message_md(self):
        mess = f"*[{self.status}]* The user story [{self.subject}]({self.link}) has been deleted"
        if self.milestone:
            mess = f"{mess} with milestone [{self.milestone.name}]({self.milestone.link})"
        return mess

    @property
    def _change_message_md(self):
        mil = f" with milestone [{self.milestone.name}]({self.milestone.link})" if self.milestone else ""
        text = f"*[{self.status}]* The user story [{self.subject}]({self.link}){mil} has been changed\n\n"
        return text + get_changes(self.changes)

    def format_message_md(self, action):
        return FormatAction(action,
                            self._create_message_md,
                            self._delete_message_md,
                            self._change_message_md).message


class Task:
    def __init__(self, payload, changes=None):
        self.tags: list[str] = payload["tags"]
        self.link = payload["permalink"]
        self.status = payload["status"]["name"]
        self.subject = payload["subject"]
        self.description = payload["description"]
        self.changes = changes

        self.milestone = Milestone(payload["milestone"]) if payload.get("milestone") else None
        self.userstory = UserStory(payload["user_story"]) if payload.get("user_story") else None
        self.us_order = payload["us_order"]

    @property
    def _create_message_md(self):
        mess = f"*[{self.status}]* The task [{self.subject}]({self.link}) has been created"
        if self.userstory:
            mess = f"{mess} in user story [{self.userstory.subject}]({self.userstory.link})"
        if self.milestone:
            mess = f"{mess} with milestone [{self.milestone.name}]({self.milestone.link})"
        return mess

    @property
    def _delete_message_md(self):
        mess = f"*[{self.status}]* The task [{self.subject}]({self.link}) has been deleted"
        if self.userstory:
            mess = f"{mess} in user story [{self.userstory.subject}]({self.userstory.link})"
        if self.milestone:
            mess = f"{mess} with milestone [{self.milestone.name}]({self.milestone.link})"
        return mess

    @property
    def _change_message_md(self):
        us = f" in user story [{self.userstory.subject}]({self.userstory.link})" if self.userstory else ""
        mil = f" with milestone [{self.milestone.name}]({self.milestone.link})" if self.milestone else ""
        text = f"*[{self.status}]* The task [{self.subject}]({self.link}) has been changed{us}{mil}\n\n"
        return text + get_changes(self.changes)

    def format_message_md(self, action):
        return FormatAction(action,
                            self._create_message_md,
                            self._delete_message_md,
                            self._change_message_md).message


class Issue:
    def __init__(self, payload, changes=None):
        self.tags: list[str] = payload["tags"]
        self.link = payload["permalink"]
        self.status = payload["status"]["name"]
        self.subject = payload["subject"]
        self.description = payload["description"]
        self.milestone = Milestone(payload["milestone"]) if payload.get("milestone") else None
        self.type = payload["type"]["name"]
        self.priority = payload["priority"]["name"]
        self.severity = payload["severity"]["name"]
        self.changes = changes

    @property
    def _create_message_md(self):
        mess = f"*[{self.status}][{self.type}]* The issue [{self.subject}]({self.link}) has been created " \
               f"with priority *{self.priority}* and severity {self.severity}*"
        if self.milestone:
            mess = f"{mess} with milestone [{self.milestone.name}]({self.milestone.link})"
        return mess

    @property
    def _delete_message_md(self):
        mess = f"*[{self.status}][{self.type}]* The issue [{self.subject}]({self.link}) has been deleted " \
               f"with priority *{self.priority}* and severity {self.severity}*"
        if self.milestone:
            mess = f"{mess} with milestone [{self.milestone.name}]({self.milestone.link})"
        return mess

    @property
    def _change_message_md(self):
        mil = f" with milestone [{self.milestone.name}]({self.milestone.link})" if self.milestone else ""
        text = f"*[{self.status}][{self.type}]* The issue [{self.subject}]({self.link}) has been changed{mil}\n\n"
        return text + get_changes(self.changes)

    def format_message_md(self, action):
        return FormatAction(action,
                            self._create_message_md,
                            self._delete_message_md,
                            self._change_message_md).message


class Wiki:
    def __init__(self, payload, changes=None):
        self.link = payload["permalink"]
        self.slug = payload["slug"]
        self.content = payload["content"]
        self.changes = changes

    @property
    def _create_message_md(self):
        return f"The wiki page [{self.slug}]({self.link}) has been created with the following content:\n\n{self.content}"

    @property
    def _delete_message_md(self):
        return f"The wiki page [{self.slug}]({self.link}) has been deleted with the following content:\n\n{self.content}"

    @property
    def _change_message_md(self):
        text = f"The wiki page [{self.slug}]({self.link}) has been changed\n\n"
        return text + get_changes(self.changes)

    def format_message_md(self, action):
        return FormatAction(action,
                            self._create_message_md,
                            self._delete_message_md,
                            self._change_message_md).message
