#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Basic example for a bot that uses inline keyboards.
# This program is dedicated to the public domain under the CC0 license.

import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
import AWESOMECAR

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
										level=logging.INFO)
logger = logging.getLogger(__name__)
def start(bot, update, user_data):
		user_data['started'] = 1;
		keyboard = [[InlineKeyboardButton("Flight  ✈️", callback_data='1'),
								 InlineKeyboardButton("Hotel 🏨", callback_data='2')],

								[InlineKeyboardButton("Rent a car 🚙", callback_data='3')]]

		reply_markup = InlineKeyboardMarkup(keyboard)

		update.message.reply_text('Hi! What would you need?', reply_markup=reply_markup)

def cancel(bot, update, user_data):
	user_data.clear();

def button(bot, update):
		query = update.callback_query

		if query.data == "1":
				bot.edit_message_text(text="Flight  ✈️",
														chat_id=query.message.chat_id,
														message_id=query.message.message_id)

		elif query.data == "2":
			bot.edit_message_text(text="Hotel 🏨",
														chat_id=query.message.chat_id,
														message_id=query.message.message_id)
		elif query.data == "3":
			bot.edit_message_text(text="Rent a car 🚙",
														chat_id=query.message.chat_id,
														message_id=query.message.message_id)
			#bot.send_message(chat_id=query.message.chat_id, text=AWESOMECAR.startcar())
			#AWESOMECAR.startcar(query)

		else:
			bot.edit_message_text(text="RILLY NIGGA",
														chat_id=query.message.chat_id,
														message_id=query.message.message_id)


def help(bot, update):
		update.message.reply_text("This bot can help you to plan your desired trip in just few clicks!! Use /start to begin.")


def error(bot, update, error):
		logging.warning('Update "%s" caused error "%s"' % (update, error))

def echo(bot, update, user_data):
	try:
		user_data['started']
		update.message.reply_text("Well")
	except:
		titatova = update.message.text
		update.message.reply_text(titatova)
		print titatova
		
# Create the Updater and pass it your bot's token.
updater = Updater("383425697:AAH4OZM2RhjZTuHM_yBkt4ili9FKIuAMO3c")

updater.dispatcher.add_handler(CommandHandler('start', start, pass_user_data=True))
updater.dispatcher.add_handler(CommandHandler('cancel', cancel, pass_user_data=True))
updater.dispatcher.add_handler(CallbackQueryHandler(button))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_error_handler(error)
updater.dispatcher.add_handler(MessageHandler(Filters.text, echo, pass_user_data=True))

# Start the Bot
updater.start_polling()

# Run the bot until the user presses Ctrl-C or the process receives SIGINT,
# SIGTERM or SIGABRT
updater.idle()
