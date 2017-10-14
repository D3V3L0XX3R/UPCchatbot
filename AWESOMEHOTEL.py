
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import requests
import json
import time


def starthotel(bot, chat_id,update):
    global update_id
    bot.send_message(chat_id=chat_id, text="Where you wanna go?")
    count=0
    #a=bot.get_updates(allowed_updates="message")
    #print a
    while(update in bot.get_updates() is [] or count<41 ):
        time.sleep(1)
        if update.message:
            print update.message.text
        count+=1
    if count!=11:
        update.message.reply_text(update.message.text)


    r = requests.get('http://partners.api.skyscanner.net/apiservices/browsequotes/v1.0/FR/eur/en-US/bcn/mad/2017-10-15/2017-10-15?apikey=ha129292138013702875479911846997')

    json_data = json.loads(r.text)
    data = r.json()
    #print json_data

    #print type(json_data)
    message = "jars jars"
    print message

