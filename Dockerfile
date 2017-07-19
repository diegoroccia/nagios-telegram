#from python:3.5
from alpine

RUN apk add --no-cache  python3
RUN pip3 install python-telegram-bot
RUN pip3 install requests
RUN pip3 install ipython

ADD bin/bot.py /

CMD python3 /bot.py 
