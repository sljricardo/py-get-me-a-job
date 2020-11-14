import unittest
import os

from sender_providers.Telegram import Telegram


class TestSenderProviders(unittest.TestCase):

    def test_telegram_endpoint(self):
        token = os.environ.get('TELEGRAM_BOT_TOKEN')
        uid = os.environ.get('TELEGRAM_BOT_ID')

        self.assertEqual(
            f'https://api.telegram.org/bot{token}/sendMessage?chat_id={uid}&parse_mode=Markdown&text=test-endpoint',
            Telegram()._Telegram__endpoint("test-endpoint")
        )


if __name__ == '__main__':
    unittest.main()
