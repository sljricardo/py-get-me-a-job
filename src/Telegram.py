import requests
import os

class Telegram:

    def __init__(self, token, uid):
        self.token = token
        self.id    = uid

    def __endpoint(self, msg):
        return f'https://api.telegram.org/bot{self.token}/sendMessage?chat_id={self.id}&parse_mode=Markdown&text={msg}' 

    def send(self, msgs):
    
        if os.environ.get('ENV') == 'dev':
            return self.__endpoint(msgs)

        if isinstance(msgs, list):
            for msg in msgs:
                requests.get(self.__endpoint(msg))
        else:
            requests.get(self.__endpoint(msgs))


