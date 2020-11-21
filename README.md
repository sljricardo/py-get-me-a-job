# Py-get-me-a-job 🔍

Search a job and when you get a match, send me a message

## Installation
#### Create Telegram Bot
1. On Telegram, search @BotFather, and send "/start" message
2. Write "/newbot" message, then follow the instructions, and **save** de **API TOKEN**
3. Search your bot, open and send "/start" to start your bot.
#### Get Your bot ID
1. Open the browser and enter https://api.telegram.org/botYOURTOKEN/getUpdates
    - don't forget to replace "YOURTOKEN" with your token string
2. Look for the id

Now you have the **token** and the **id**, create a .env file in the root and replace by your info
```txt
ENV=prod
SENDER_PROVIDER="Telegram"
TELEGRAM_BOT_TOKEN=yourToken
TELEGRAM_BOT_ID=yourId
```

After replace info run the command:
```bash
$ python py_get_me_a_job/main.py
```

Note: If the offer is already sended, and you want to resend, need to delete **store** file in root of the project