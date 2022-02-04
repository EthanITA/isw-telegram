from datetime import datetime

import Helper
from Helper.Taiga import Data
from Taiga import Action
from Taiga.By import By


class Taiga():
    def __init__(self, payload: dict):
        self.action = payload['action']
        self.type = payload['type']
        self.by = By(payload['by'])
        self.date = Helper.convert_utc_rome(datetime.strptime(payload["date"], "%Y-%m-%dT%H:%M:%S.%fZ"))
        self.data = Data(payload['data'])
        if self.action == Action.change:
            self.change = payload['change']

    def format_message_md(self):
        action_text = "did something"
        match self.action:
            case Action.create:
                action_text = self._format_create_md()
            case Action.delete:
                action_text = self._format_delete_md()
            case Action.change:
                action_text = self._format_change_md()
            case Action.test:
                action_text = self._format_test_md()
        formatted_message = f"*[{self.date.strftime('%H:%M:%S')}]* " \
                            f"The user [{self.by.full_name}]({self.by.link}) {action_text} on the board [{self.board}]({board_link}) "

        return formatted_message

    def _format_create_md(self) -> str:
        pass

    def _format_delete_md(self) -> str:
        pass

    def _format_change_md(self) -> str:
        pass

    def _format_test_md(self) -> str:
        pass
