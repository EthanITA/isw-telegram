from telegram.utils.helpers import escape_markdown

from Helper.MessageMD import MessageMD
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
            diff = f"{change['from']} --> {change['to']}"
            text += f"{name}\n\t {diff}\n"
        return text
    else:
        return ""


class FormatAction:
    def __init__(self, action, create, delete, change):
        self.action = action
        self.create = create
        self.delete = delete
        self.change = change

    def message(self) -> str | None:
        match self.action:
            case Action.create:
                return self.create
            case Action.delete:
                return self.delete
            case Action.change:
                return self.change
            case _:
                return None


class Milestone(MessageMD):
    def __init__(self, payload, action, changes=None):
        self.link = payload["permalink"]
        self.name = payload["name"]
        self.slug = payload["slug"]
        self.estimated_start = payload["estimated_start"]
        self.estimated_finish = payload["estimated_finish"]
        self.disponibility = payload["disponibility"]
        super().__init__(FormatAction(action,
                                       self._create_message_md,
                                       self._delete_message_md,
                                       self._change_message_md).message(),
                         get_changes(changes))

    @property
    def _create_message_md(self):
        return f"created {self._milestone_text_md}"

    @property
    def _delete_message_md(self):
        return f"deleted {self._milestone_text_md}"

    @property
    def _change_message_md(self):
        return f"changed {self._milestone_text_md}"

    @property
    def _milestone_text_md(self):
        return f"the milestone [{self.name}]({self.link})"


class UserStory(MessageMD):
    def __init__(self, payload, action, changes=None):
        self.tags: list[str] = payload["tags"]
        self.link = payload["permalink"]
        self.points: list[dict] = payload["points"]
        self.status = payload["status"]["name"]
        self.subject = payload["subject"]
        self.description = payload["description"]
        self.milestone = Milestone(payload["milestone"], action) if payload.get("milestone") else None
        super().__init__(FormatAction(action,
                                       self._create_message_md,
                                       self._delete_message_md,
                                       self._change_message_md).message(),
                         get_changes(changes))

    @property
    def _create_message_md(self):
        return f"created {self._userstory_text_md}"

    @property
    def _delete_message_md(self):
        return f"deleted {self._userstory_text_md}"

    @property
    def _change_message_md(self):
        return f"changed {self._userstory_text_md}"

    @property
    def _userstory_text_md(self):
        status_escaped_md = escape_markdown(f"[{self.status}]", 2)
        mess = f"the user story [{status_escaped_md} {self.subject}]({self.link})"
        if self.milestone:
            mess = f"{mess} with milestone [{self.milestone.name}]({self.milestone.link})"
        return mess


class Task(MessageMD):
    def __init__(self, payload, action, changes=None):
        self.tags: list[str] = payload["tags"]
        self.link = payload["permalink"]
        self.status = payload["status"]["name"]
        self.subject = payload["subject"]
        self.description = payload["description"]
        self.milestone = Milestone(payload["milestone"], action) if payload.get("milestone") else None
        self.userstory = UserStory(payload["user_story"], action) if payload.get("user_story") else None
        self.us_order = payload["us_order"]

        super().__init__(FormatAction(action,
                                       self._create_message_md,
                                       self._delete_message_md,
                                       self._change_message_md).message(),
                         get_changes(changes))

    @property
    def _create_message_md(self):
        return f"created {self._task_text_md}"

    @property
    def _delete_message_md(self):
        return f"deleted {self._task_text_md}"

    @property
    def _change_message_md(self):
        return f"changed {self._task_text_md}"

    @property
    def _task_text_md(self):
        status_escape_md = escape_markdown(f"[{self.status}]", 2)
        mess = f"the task [{status_escape_md} {self.subject}]({self.link})"
        if self.userstory:
            mess = f"{mess} in user story [{self.userstory.subject}]({self.userstory.link})"
        if self.milestone:
            mess = f"{mess} with milestone [{self.milestone.name}]({self.milestone.link})"
        return mess


class Issue(MessageMD):
    def __init__(self, payload, action, changes=None):
        self.tags: list[str] = payload["tags"]
        self.link = payload["permalink"]
        self.status = payload["status"]["name"]
        self.subject = payload["subject"]
        self.description = payload["description"]
        self.milestone = Milestone(payload["milestone"], action) if payload.get("milestone") else None
        self.type = payload["type"]["name"]
        self.priority = payload["priority"]["name"]
        self.severity = payload["severity"]["name"]
        super().__init__(FormatAction(action,
                                       self._create_message_md,
                                       self._delete_message_md,
                                       self._change_message_md).message(),
                         get_changes(changes))

    @property
    def _create_message_md(self):
        return f"created {self._issue_text_md}"

    @property
    def _delete_message_md(self):
        return f"deleted {self._issue_text_md}"

    @property
    def _change_message_md(self):
        return f"changed {self._issue_text_md}"

    @property
    def _issue_text_md(self):
        text_escape_md = escape_markdown(f"[{self.status}][{self.type}]", 2)
        mess = f"the issue [{text_escape_md} {self.subject}]({self.link})" \
               f"with priority *{self.priority}* and severity {self.severity}*"
        if self.milestone:
            mess = f"{mess} with milestone [{self.milestone.name}]({self.milestone.link})"
        return mess

class Wiki(MessageMD):
    def __init__(self, payload, action, changes=None):
        self.link = payload["permalink"]
        self.slug = payload["slug"]
        self.content = payload["content"]
        super().__init__(FormatAction(action,
                                       self._create_message_md,
                                       self._delete_message_md,
                                       self._change_message_md).message(),
                         get_changes(changes))

    @property
    def _create_message_md(self):
        return f"created the wiki page [{self.slug}]({self.link}) with the following content:\n\n{self.content}"

    @property
    def _delete_message_md(self):
        return f"deleted the wiki page [{self.slug}]({self.link})"

    @property
    def _change_message_md(self):
        return f"updated the wiki page [{self.slug}]({self.link})"
