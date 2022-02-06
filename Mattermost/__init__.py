from datetime import datetime

from Helper.MessageMD import MessageMD


class Mattermost(MessageMD):
    def __init__(self, payload: dict):
        self.channel_name = payload['channel_name']
        self.team_domain = payload['team_domain']
        self.text = payload['text']
        self.user_name = payload['user_name']
        self.trigger_word = payload['trigger_word']
        self.date = datetime.fromtimestamp(payload['timestamp']/1000)
        super().__init__(self._gen_message())

    def _gen_message(self):
        return f'[{self.date.time()}] {self.user_name}@{self.team_domain}/{self.channel_name} says:\n' \
               f'{self.text}'
