#from python:3.5
from alpine

RUN apk add --no-cache  python3
RUN pip3 install python-telegram-bot
RUN pip3 install python-mk-livestatus
RUN pip3 install requests

ADD srv /srv

CMD python3 /srv/bot.py 
