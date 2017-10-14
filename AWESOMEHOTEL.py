
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import requests
import json


def starthotel(bot, chat_id):
    global update_id
    bot.send_message(chat_id=chat_id, text="Hotel California")

    r = requests.get('http://partners.api.skyscanner.net/apiservices/browsequotes/v1.0/FR/eur/en-US/bcn/mad/2017-10-15/2017-10-15?apikey=ha129292138013702875479911846997')

    json_data = json.loads(r.text)
    data = r.json()
    print data

    message = "jars jars"
    print message