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
        super().__init__(self._generate_message_md(), self._generate_commits_md())

    def _generate_message_md(self):
        user_name = escape_markdown(self.user_name, version=2)
        branch = escape_markdown(self.branch, version=2)
        repo_name = escape_markdown(self.repo.name, version=2)
        return f"[{user_name}]({self.user_profile_link}) just pushed {self.total_commits} " \
               f"{'commit' if self.total_commits == 1 else 'commits'}" \
               f" to {branch} in [{repo_name}]({self.repo.url})\n"

    def _generate_commits_md(self):
        text = "\n\n".join([f"\n{commit.formatted_message_md}" for commit in self.commits][::-1])
        if self.total_commits > len(self.commits):
            text += f"\n\nand *{self.total_commits - len(self.commits)} more commits*"
        return text


class Issue(MessageMD):
    OPEN_ACTION = "open"
    CLOSE_ACTION = "close"
    REOPEN_ACTION = "reopen"
    UPDATE_ACTION = "update"

    def __init__(self, payload):
        self.repo = Repository(payload["project"])
        self.issue_event = payload["object_attributes"]["action"]
        self.issue_status = payload["object_attributes"]["state"]
        self.issue_title = payload["object_attributes"]["title"]
        self.issue_description = payload["object_attributes"]["description"]
        self.issue_url = payload["object_attributes"]["url"]
        self.user_name = payload["user"]["name"]
        self.user_username = payload["user"]["username"]
        self.user_profile_link = f"https://gitlab.com/{self.user_username}"
        super().__init__(self._gen_message_md())

    @property
    def _open_message(self):
        return f"opened a new issue"

    @property
    def _close_message(self):
        return f"closed the issue"

    @property
    def _reopen_message(self):
        return f"reopened the issue"

    @property
    def _update_message(self):
        return f"updated the issue"

    def _gen_message_md(self):
        text = ""
        match self.issue_event.lower():
            case self.OPEN_ACTION:
                text = self._open_message
            case self.CLOSE_ACTION:
                text = self._close_message
            case self.REOPEN_ACTION:
                text = self._reopen_message
            case self.UPDATE_ACTION:
                text = self._update_message

        return f"[{self.user_name}]({self.user_profile_link}) {text} [{self.issue_title}]({self.issue_url})"


class WikiPage(MessageMD):
    CREATE_ACTION = "create"
    UPDATE_ACTION = "update"
    DELETE_ACTION = "delete"

    def __init__(self, payload):
        self.repo = Repository(payload["project"])
        self.wiki_event = payload["object_attributes"]["action"]
        self.wiki_title = payload["object_attributes"]["title"]
        self.wiki_url = payload["object_attributes"]["url"]
        self.user_name = payload["user"]["name"]
        self.user_username = payload["user"]["username"]
        self.user_profile_link = f"https://gitlab.com/{self.user_username}"
        super().__init__(self._gen_message_md())

    @property
    def _create_message(self):
        return f"created a new wiki page"

    @property
    def _update_message(self):
        return f"updated the wiki page"

    @property
    def _delete_message(self):
        return f"deleted the wiki page"

    def _gen_message_md(self):
        text = ""
        match self.wiki_event.lower():
            case self.CREATE_ACTION:
                text = self._create_message
            case self.UPDATE_ACTION:
                text = self._update_message
            case self.DELETE_ACTION:
                text = self._delete_message

        return f"[{self.user_name}]({self.user_profile_link}) {text} [{self.wiki_title}]({self.wiki_url})"
