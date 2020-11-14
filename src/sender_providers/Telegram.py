import requests
import os

from src.SenderInterface import SenderInterface

class Telegram(SenderInterface):

    def __init__(self):
        self.id    = os.environ.get('TELEGRAM_BOT_ID')
        self.token = os.environ.get('TELEGRAM_BOT_TOKEN')

    def __endpoint(self, msg):
        return f'https://api.telegram.org/bot{self.token}/sendMessage?chat_id={self.id}&parse_mode=Markdown&text={msg}' 

    def send(self, msgs):
        requests.get(self.__endpoint(msgs))


