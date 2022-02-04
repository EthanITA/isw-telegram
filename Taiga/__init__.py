from datetime import datetime

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
        action_type_text = None
        match self.type:
            case Type.milestone:
                action_type_text = self.data.milestone.format_message_md
            case Type.userstory:
                action_type_text = self.data.userstory.format_message_md
            case Type.task:
                action_type_text = self.data.task.format_message_md
            case Type.issue:
                action_type_text = self.data.issue.format_message_md
            case Type.wiki:
                action_type_text = self.data.wiki.format_message_md
        formatted_message = f"*[{self.date.strftime('%H:%M:%S')}]*\t" \
                            f"[{self.data.project_name}]({self.data.project_link})/" \
                            f"[{self.by.full_name}]({self.by.link})" \
                            f"\n{action_type_text}"

        return formatted_message if action_type_text is not None else None
