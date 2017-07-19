#!python3
from telegram.ext import Updater,CommandHandler
import requests
import logging
import os
import re

configuration = { k.replace("BOT_",""): os.environ[k] for k in os.environ if  k.find("BOT_") == 0}

print (configuration)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

updater = Updater("440051803:AAFwKlpWQntxw0V96EtXsUU7czdwIuhyrsE")
dispatcher = updater.dispatcher

def problemlist(bot, update):                                               
     print("received")
     bot.send_message(chat_id=update.message.chat_id, text="let me check...")
     r = requests.get("https://{NAGIOSUSER}:{NAGIOSPWD}@{NAGIOSURL}/nagios/cgi-bin/statusjson.cgi?query=servicelist&servicestatus=critical".format(**configuration))
     for host in r.json()['data']['servicelist']:
         for service in r.json()['data']['servicelist'][host]:
             bot.send_message(chat_id=update.message.chat_id, text="{} > {}".format(host,service))

start_handler = CommandHandler('problems', problemlist)
dispatcher.add_handler(start_handler)

updater.start_polling()  
