from datetime import datetime

from telegram.utils.helpers import escape_markdown

from Helper.MessageMD import MessageMD


class Commit(MessageMD):
    def __init__(self, payload: dict):
        self.commit_id = payload['id']
        self.message = payload['message']
        self.time: datetime = datetime.fromisoformat(payload['timestamp'])
        self.url = payload['url']
        self.author_name = payload['author']['name']
        self.author_email = payload['author']['email']
        self.added: list[str] = payload['added']
        self.modified: list[str] = payload['modified']
        self.removed: list[str] = payload['removed']
        super().__init__(
            self.formatted_message_md +
            "\n\n" + self.formatted_added_md_escaped +
            "\n" + self.formatted_modified_md_escaped +
            "\n" + self.formatted_removed_md_escaped)

    @staticmethod
    def get_short_id(commit_id: str) -> str:
        return commit_id[:7]

    @property
    def formatted_message_md(self):
        mess = escape_markdown(self.message, version=2)
        return f'\\[[{self.get_short_id(self.commit_id)}]({self.url})\\] {mess}'

    @property
    def formatted_added_md_escaped(self):
        return escape_markdown(
            "\n[+]".join(self.added[:5] + [f"... {len(self.added) - 5}"] if len(self.added) > 5 else []),
            version=2)

    @property
    def formatted_modified_md_escaped(self):
        return escape_markdown("\n[~]".join(
            self.modified[:5] + [f"... {len(self.modified) - 5}"] if len(self.modified) > 5 else []),
            version=2)

    @property
    def formatted_removed_md_escaped(self):
        return escape_markdown(
            "\n[-]".join(self.removed[:5] + [f"... {len(self.removed) - 5}"] if len(self.removed) > 5 else []),
            version=2)


class Repository:
    def __init__(self, payload: dict):
        self.name = payload['name']
        self.url = payload['web_url']
        self.description = payload['description']
