from telegram.ext import Updater,CommandHandler
import requests
import logging
import os
import re
import mk_livestatus


config = { k.replace("BOT_",""): os.environ[k] for k in os.environ if  k.find("BOT_") == 0}

from local_settings import *

updater = Updater(config["BOTKEY"])
dispatcher = updater.dispatcher

def problemlist(bot, update):                                               
     s = mk_livestatus.Socket("/srv/livesocket")
     problems = s.services.columns("host_name","description","plugin_output").filter("state = 2").call()
     for problem in problems:
          print( "* {host_name} > {description}\n{plugin_output}".format(**problem) )
          bot.send_message(chat_id=update.message.chat_id, text="* {host_name} > {description}\n{plugin_output}".format(**problem) )

start_handler = CommandHandler('problems', problemlist)
dispatcher.add_handler(start_handler)
updater.start_polling()  
