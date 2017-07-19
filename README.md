# Nagios/Telegram_Bot connector

this project aims to provide a connector between nagios and telegram using the Bot API

## Requirements

* nagios + mk_livestatus
* python3, with the following libraries
  * python-telegram-bot
  * python-mk-livestatus

## Preliminary steps

* Create a new bot on telegram. [Guide Here](https://core.telegram.org/bots#creating-a-new-bot)
* Create a local_settings.py file with the following content:
```
config = { "BOTKEY": "sdfsdfsdfsdfsdf" }
```

these configurations can also be passed to the script using environment variables, calling them `BOT_<configitem>`
```
export "BOTKEY"="sdfsdfsdfsdfsdf"
```

## Running the bot

### Manually

Launch `python bot.py`

### with Docker

#### Dockerfile

a Dockerfile is also provided:

```
docker build -t nagios-telegram .

docker run -d -t nagios-telegram \
           -e  "BOTKEY"="sdfsdfsdfsdfsdf" \
           -v /path/to/mklive/socket:/srv/livesocket
```

#### Docker-compose
you will need to change the docker-compose.yaml file to change the socket path

```
docker-compose up -d
```
