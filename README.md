# Nagios/Telegram_Bot connector

this project aims to provide a connector between nagios and telegram using the Bot API

## Requirements

* nagios >= 4.0.7 (they introduced Json endpoints)
* python3, with the following libraries
  * requests
  * python-telegram-bot

## Preliminary steps

* Create a new bot on telegram. [Guide Here](https://core.telegram.org/bots#creating-a-new-bot)
* Create a local_settings.py file with the following content:
```
config = {
  "BOTKEY": "sdfsdfsdfsdfsdf",
  "NAGIOSUSER": "sdfsdfsdfsdfsdfd",
  "NAGIOSPWD": "rsdfsdfsd",
  "NAGIOSURL": "sdfsdf" 
}
```
