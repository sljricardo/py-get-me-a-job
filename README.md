# Py-get-me-a-job 🔍

Search a job and when you get a match, send me a message

## Installation
#### Create Telegram Bot
1. On Telegram, search @BotFather, and send "/start" message
2. Write "/newbot" message, then follow the instructions, and **save** de **API TOKEN**
3. Search your bot, open and send "/start" to start your bot.
#### Get Your bot ID
1. Open the browser and enter https://api.telegram.org/botYOURTOKEN/getUpdates
2. Look for the id

Now you have the **token** and the **id**, create a .env file in the root and replace by your info
```txt
BOT_TOKEN=yourToken
BOT_ID=yourID
ENV=prod
```