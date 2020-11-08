import unittest
import os

from src.Telegram import Telegram

class TestSenderProviders(unittest.TestCase):

    def test_telegram_endpoint(self):
        os.environ['ENV'] = 'dev'
        telegram = Telegram("my-token-id", "my-uid")

        self.assertEqual(
            'https://api.telegram.org/botmy-token-id/sendMessage?chat_id=my-uid&parse_mode=Markdown&text=test-endpoint',
            telegram.send("test-endpoint")
        )
    
if __name__ == '__main__':
    unittest.main()