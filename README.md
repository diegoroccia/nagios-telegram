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

these configurations can also be passed to the script using environment variables, calling them `BOT_<configitem>`
```
export "BOTKEY"="sdfsdfsdfsdfsdf"
export "NAGIOSUSER"="sdfsdfsdfsdfsdfd"
export "NAGIOSPWD"="rsdfsdfsd"
export "NAGIOSURL"="sdfsdf" 
```

## Running the bot

Launch `python bot.py`

a Dockerfile is also provided:

```
docker build -t nagios-telegram .

docker run -d -t nagios-telegram \
           -e  "BOTKEY"="sdfsdfsdfsdfsdf" \
           -e  "NAGIOSUSER"="sdfsdfsdfsdfsdfd" \
           -e  "NAGIOSPWD"="rsdfsdfsd" \
           -e  "NAGIOSURL"="sdfsdf" 
```
