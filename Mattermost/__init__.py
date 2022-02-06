from datetime import datetime

from telegram.utils.helpers import escape_markdown

from Helper.MessageMD import MessageMD


class Mattermost(MessageMD):
    def __init__(self, payload: dict):
        self.channel_name = payload['channel_name']
        self.team_domain = payload['team_domain']
        self.text = payload['text']
        self.user_name = payload['user_name']
        self.trigger_word = payload['trigger_word']
        self.date = datetime.fromtimestamp(payload['timestamp'] / 1000)
        super().__init__(self._gen_message())

    def _gen_message(self):
        return escape_markdown(f'[{str(self.date.time())[:8]}] {self.user_name}@{self.channel_name} says:\n\n',
                               version=2) + \
               f'```\n{escape_markdown(self.text, version=2)}```'
