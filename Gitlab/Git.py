from datetime import datetime

from telegram.utils.helpers import escape_markdown

from Helper.MessageMD import MessageMD


class Commit(MessageMD):
    def __init__(self, payload: dict):
        self.commit_id = payload['id']
        self.short_message = payload["message"].split("\n")[0].strip()
        self.time: datetime = datetime.fromisoformat(payload['timestamp'])
        self.url = payload['url']
        self.author_name = payload['author']['name']
        self.author_email = payload['author']['email']
        self.added: list[str] = payload['added']
        self.modified: list[str] = payload['modified']
        self.removed: list[str] = payload['removed']
        super().__init__(
            self._formatted_message_md +
            "\n```" +
            self.formatted_added_md_escaped +
            "\n" + self.formatted_modified_md_escaped +
            "\n" + self.formatted_removed_md_escaped +
            "```")

    @staticmethod
    def get_short_id(commit_id: str) -> str:
        return commit_id[:7]

    @property
    def _formatted_message_md(self):
        mess = escape_markdown(self.short_message, version=2)
        return f'\\[[{self.get_short_id(self.commit_id)}]({self.url})\\] {mess}'

    @property
    def formatted_added_md_escaped(self):
        text = "\n".join([f"  [+] {commit}" for commit in self.added[:5]])
        if len(self.added) > 5:
            text += f"\nand {len(self.added) - 5} more"
        return escape_markdown(text, version=2)

    @property
    def formatted_modified_md_escaped(self):
        text = "\n".join([f"  [~] {commit}" for commit in self.modified[:5]])
        if len(self.modified) > 5:
            text += f"\nand {len(self.modified) - 5} more"
        return escape_markdown(text, version=2)

    @property
    def formatted_removed_md_escaped(self):
        text = "\n".join([f"  [-] {commit}" for commit in self.removed[:5]])
        if len(self.removed) > 5:
            text += f"\nand {len(self.removed) - 5} more"
        return escape_markdown(text, version=2)


class Repository:
    def __init__(self, payload: dict):
        self.name = payload['name']
        self.url = payload['web_url']
        self.description = payload['description']
