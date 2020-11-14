import os

from src.sender_providers.Telegram import Telegram  

class SenderProviders:

    def __init__(self):
        self.providers = {
            "Telegram": Telegram
        }

    def send(self, providers_jobs):
        content_to_send = ''

        for provider in providers_jobs:
            for jobs in provider:
                content_to_send += jobs

        self.providers[os.environ.get('SENDER_PROVIDER')]().send(content_to_send)