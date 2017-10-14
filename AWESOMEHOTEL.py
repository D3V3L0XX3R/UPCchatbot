
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import requests
import json


def startfly(bot, chat_id):
    global update_id
    bot.send_message(chat_id=chat_id, text="Hotel California")
    for update in bot.get_updates(offset=update_id, timeout=10):
    update_id = update.update_id + 1

    if update.message:
      
        update.message.reply_text(update.message.text)

    #r = requests.get('https://github.com/timeline.json')

    #json_data = json.loads(r.text)
    #data = r.json()

    message = "tita loca"
    print message