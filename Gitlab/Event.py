from Gitlab.Git import Commit, Repository
from Helper.MessageMD import MessageMD

push = "push"
issue = "issue"
merge_request = "merge_request"
comment = "note"
wiki_page = "wiki_page"


class Push(MessageMD):
    def __init__(self, payload):
        self.branch = payload["ref"].split("/")[-1]
        self.last_commit_id = payload["after"]
        self.before_commit_id = payload["before"]
        self.user_name = payload["user_name"]
        self.user_username = payload["user_username"]
        self.repo = Repository(payload["project"])
        self.commits: list[Commit] = [Commit(commit) for commit in payload["commits"]]
        self.total_commits = payload["total_commits_count"]
        super().__init__(self._generate_message())

    def _generate_message(self):
        return f"{self.user_name} pushed {self.total_commits} {'commit' if self.total_commits == 1 else 'commits'}" \
               f" to {self.branch} in {self.repo.name} ({self.repo.url})\n"

    def get_commits_message_md(self):
        return "\n".join([commit.format_message_md for commit in self.commits])


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
