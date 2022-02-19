from datetime import datetime

from telegram.utils.helpers import escape_markdown


class Commit:
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

    @property
    def formatted_message_md(self):
        return f"{self._formatted_message_md}\n" \
               f"```{self.formatted_added_md_escaped}\n" \
               f"{self.formatted_modified_md_escaped}" \
               f"\n{self.formatted_removed_md_escaped}```"

    @staticmethod
    def get_short_id(commit_id: str) -> str:
        return commit_id[:7]

    @property
    def _formatted_message_md(self):
        mess = escape_markdown(self.short_message, version=2)
        return f'\\[[{self.get_short_id(self.commit_id)}]({self.url})\\] {mess}'

    def _get_formatted_changes(self, changes: list[str], prepend="") -> str:
        n_changes = 5
        text = "\n".join([f"  {prepend} {commit}" for commit in changes[:n_changes]])
        if len(changes) > n_changes:
            text += f"\nand {len(changes) - n_changes} more"
        return escape_markdown(text, version=2)

    @property
    def formatted_added_md_escaped(self):
        return self._get_formatted_changes(self.added, prepend="[+]")

    @property
    def formatted_modified_md_escaped(self):
        return self._get_formatted_changes(self.modified, prepend="[~]")

    @property
    def formatted_removed_md_escaped(self):
        return self._get_formatted_changes(self.removed, prepend="[-]")


class Repository:
    def __init__(self, payload: dict):
        self.name = payload['name']
        self.url = payload['web_url']
        self.description = payload['description']
