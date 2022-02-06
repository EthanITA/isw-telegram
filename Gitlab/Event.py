from telegram.utils.helpers import escape_markdown

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
        self.user_profile_link = f"https://gitlab.com/{self.user_username}"
        self.repo = Repository(payload["project"])
        self.commits: list[Commit] = [Commit(commit) for commit in payload["commits"]]
        self.total_commits = payload["total_commits_count"]
        super().__init__(self._generate_message_md())

    def _generate_message_md(self):
        user_name = escape_markdown(self.user_name, version=2)
        branch = escape_markdown(self.branch, version=2)
        repo_name = escape_markdown(self.repo.name, version=2)
        return f"[{user_name}]({self.user_profile_link}) just pushed {self.total_commits} " \
               f"{'commit' if self.total_commits == 1 else 'commits'}" \
               f" to {branch} in [{repo_name}]({self.repo.url})\n"

    @property
    def formatted_commits_md(self):
        text = "\n\n".join([f"\n{commit.formatted_message_md}" for commit in self.commits][::-1])
        if self.total_commits > len(self.commits):
            text += f"\n\nand *{self.total_commits - len(self.commits)} more commits*"
        return text


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
