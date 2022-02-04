from Gitlab import Event
from Gitlab.Event import Push, Issue, MergeRequest, Comment, WikiPage


class Gitlab:
    def __init__(self, payload):
        self.payload = payload
        self.object_kind = payload['object_kind']
        self.project_name = payload['project']['name']
        self.project_url = payload['project']['web_url']

    def format_message_md(self):
        match self.object_kind:
            case Event.push:
                return Push(self.payload).format_message_md
            case Event.issue:
                return Issue(self.payload).format_message_md
            case Event.merge_request:
                return MergeRequest(self.payload).format_message_md
            case Event.comment:
                return Comment(self.payload).format_message_md
            case Event.wiki_page:
                return WikiPage(self.payload).format_message_md
            case _:
                return None
