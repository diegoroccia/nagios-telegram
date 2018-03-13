from telegram.ext import Updater,CommandHandler
import requests
import logging
import os
import re
import mk_livestatus


config = dict(filter(lambda x : x[0].startswith("BOT_"), os.environ.items()))

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
