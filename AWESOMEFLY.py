
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import requests



def startfly(bot, chat_id):
    bot.send_message(chat_id=chat_id, text="PENISCLE")
    message = "tita loca"
    print message