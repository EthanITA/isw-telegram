from datetime import datetime

from telegram.utils.helpers import escape_markdown

import Helper
from Taiga import Action, Type
from Taiga.By import By
from Taiga.Data import Data


class Taiga:
    def __init__(self, payload: dict):
        self.action = payload['action']
        self.type = payload['type']
        self.by = By(payload['by'])
        self.date = Helper.convert_utc_rome(datetime.strptime(payload["date"], "%Y-%m-%dT%H:%M:%S.%fZ"))
        if self.action == Action.change:
            self.change = payload['change']
        else:
            self.change = None
        self.data = Data(payload['data'], self.type, self.change, self.action)

    def format_message_md(self):
        action_type_text, changes_text = None, None
        match self.type:
            case Type.milestone:
                action_type_text, changes_text = self.data.milestone.formatted_messages_md
            case Type.userstory:
                action_type_text, changes_text = self.data.userstory.formatted_messages_md
            case Type.task:
                action_type_text, changes_text = self.data.task.formatted_messages_md
            case Type.issue:
                action_type_text, changes_text = self.data.issue.formatted_messages_md
            case Type.wiki:
                action_type_text, changes_text = self.data.wiki.formatted_messages_md

        time_escaped_md = escape_markdown(f"[{self.date.strftime('%H:%M:%S')}]", version=2)
        formatted_message = f"{time_escaped_md}" \
                            f"\\[[{self.data.project_name}]({self.data.project_link})\\]\n" \
                            f"[{self.by.full_name}]({self.by.link})" \
                            f" {action_type_text} "
        if action_type_text is not None:
            return formatted_message, changes_text
        else:
            return None, None
