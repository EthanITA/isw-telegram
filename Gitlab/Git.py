from datetime import datetime

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
            "\n\n" + self.formatted_added_md +
            "\n" + self.formatted_modified_md +
            "\n" + self.formatted_removed_md)

    @staticmethod
    def get_short_id(commit_id: str) -> str:
        return commit_id[:7]

    @property
    def formatted_message_md(self):
        return f'\\[[{self.get_short_id(self.commit_id)}]({self.url})\\] {self.message}'

    @property
    def formatted_added_md(self):
        return "\n\\[+\\]".join(self.added[:5] + [f"... {len(self.added) - 5}"] if len(self.added) > 5 else [])

    @property
    def formatted_modified_md(self):
        return "\n\\[~\\]".join(
            self.modified[:5] + [f"... {len(self.modified) - 5}"] if len(self.modified) > 5 else [])

    @property
    def formatted_removed_md(self):
        return "\n\\[-\\]".join(self.removed[:5] + [f"... {len(self.removed) - 5}"] if len(self.removed) > 5 else [])


class Repository:
    def __init__(self, payload: dict):
        self.name = payload['name']
        self.url = payload['web_url']
        self.description = payload['description']
