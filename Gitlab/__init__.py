from Gitlab import Event
from Gitlab.Event import Push, Issue, MergeRequest, Comment, WikiPage


class Gitlab:
    def __init__(self, payload):
        self.payload = payload
        self.event_type = payload['object_kind']
        self.project_name = payload['project']['name']
        self.project_url = payload['project']['web_url']

    def get_event(self) -> Push | Issue | MergeRequest | Comment | WikiPage | None:
        match self.event_type:
            case Event.push:
                return Push(self.payload)
            case Event.issue:
                return Issue(self.payload)
            case Event.merge_request:
                return MergeRequest(self.payload)
            case Event.comment:
                return Comment(self.payload)
            case Event.wiki_page:
                return WikiPage(self.payload)
            case _:
                return None
