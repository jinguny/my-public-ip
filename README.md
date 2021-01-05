# My Public IP

Get public IP and send it via Telegram

## How to use

### Create a Telegram bot

- Create a chat with @BotFather and type `/newbot`.
- Name your bot and get an access token

### Install

```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Create a cron job

```bash
crontab -e

# append this line
@reboot TOKEN=<token> CHAT_ID=<chat_id> <path_to_virtualenv>/bin/python3 <path_to_local_repo>/bot.py
```
