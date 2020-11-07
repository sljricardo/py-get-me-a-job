import requests

class Telegram:

    def __init__(self, token, uid):
        self.token = token
        self.id    = uid

    def __endpoint(self, msg):
        return f'https://api.telegram.org/bot{self.token}/sendMessage?chat_id={self.id}&parse_mode=Markdown&text={msg}' 

    def send(self, msg):
        content = self.__endpoint(msg)
        requests.get(content)
        pass


