
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import requests
import json


def starthotel(bot, chat_id):
    global update_id
    bot.send_message(chat_id=chat_id, text="Hotel California")
    for update in bot.get_updates(offset=update_id, timeout=10):
    update_id = update.update_id + 1

    if update.message:
      
        update.message.reply_text(update.message.text)

    r = requests.get('http://partners.api.skyscanner.net/apiservices/browsequotes/v1.0/FR/eur/en-US/es/us/anytime/anytime?apikey=ha129292138013702875479911846997')

    json_data = json.loads(r.text)
    data = r.json()
    print data

    message = "jars jars"
    print message