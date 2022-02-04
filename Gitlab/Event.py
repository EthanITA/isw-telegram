from Helper.MessageMD import MessageMD

push = "push"
issue = "issue"
merge_request = "merge_request"
comment = "note"
wiki_page = "wiki_page"


class Push(MessageMD):
    def __init__(self, payload):
        super().__init__()


class MergeRequest(MessageMD):
    def __init__(self, payload):
        super().__init__()


class Issue(MessageMD):
    def __init__(self, payload):
        super().__init__()


class Comment(MessageMD):
    def __init__(self, payload):
        super().__init__()


class WikiPage(MessageMD):
    def __init__(self, payload):
        super().__init__()
