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
		'''update.message.text = None
		update.message.reply_text('My name is Skyblue!\nWhat is your name?')
		while update.message.text == None:
			pass
		user_data['name'] = update.message.text'''
		user_data['count'] = 1
		keyboard = [[InlineKeyboardButton("Flight  ✈️", callback_data='1'),
								 InlineKeyboardButton("Hotel 🏨", callback_data='2')],

								[InlineKeyboardButton("Rent a car 🚙", callback_data='3')]]

		reply_markup = InlineKeyboardMarkup(keyboard)

		#update.message.reply_text('Hi ' + user_data['name'] + '! What would you need?', reply_markup=reply_markup)
		update.message.reply_text('Hi! What would you need?', reply_markup=reply_markup)

def cancel(bot, update, user_data):
	del user_data

def button(bot, update, user_data):
		query = update.callback_query
		user_data['start'] = query.data
		user_data['count'] = 2
		if query.data == "1":
				bot.edit_message_text(text="Flight  ✈️",
														chat_id=query.message.chat_id,
														message_id=query.message.message_id)

		elif query.data == "2":
			bot.edit_message_text(text="Hotel 🏨",
														chat_id=query.message.chat_id,
														message_id=query.message.message_id)
		elif query.data == "3":
			#bot.edit_message_text(text="How much money have you at maximum?", chat_id=query.message.chat_id, message_id=query.message.message_id)
			bot.send_message(chat_id=query.message.chat_id, text='How much money have you at maximum?')
			#AWESOMECAR.startcar(query)
		elif query.data == "a" or query.data == "b":
			user_data['location'] = query.data
			bot.send_message(chat_id=query.message.chat_id, text=user_data)
			user_data['count'] = 4

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
		user_data['count']
		if user_data['count'] == 1:
			update.message.reply_text("Well")
		elif user_data['count'] == 2:
			if user_data['start'] == "3":
				user_data['count'] = 3
				user_data['money'] = update.message.text		
				update.message.reply_text("How much days you want to rent?")	
		elif user_data['count'] == 3:
			if user_data['start'] == "3":
				
				keyboard = [[InlineKeyboardButton("Car Hire",callback_data = 'a' ),InlineKeyboardButton("Aiport Transfers",callback_data='b')]]
				reply_markup = InlineKeyboardMarkup(keyboard)
				update.message.reply_text('Choose your option',reply_markup=reply_markup)


	except: 
		update.message.reply_text("Please, write /start to awake me")
		
# Create the Updater and pass it your bot's token.
updater = Updater("383425697:AAH4OZM2RhjZTuHM_yBkt4ili9FKIuAMO3c")

updater.dispatcher.add_handler(CommandHandler('start', start, pass_user_data=True))
updater.dispatcher.add_handler(CommandHandler('cancel', cancel, pass_user_data=True))
updater.dispatcher.add_handler(CallbackQueryHandler(button, pass_user_data=True))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_error_handler(error)
updater.dispatcher.add_handler(MessageHandler(Filters.text, echo, pass_user_data=True))

# Start the Bot
updater.start_polling()

# Run the bot until the user presses Ctrl-C or the process receives SIGINT,
# SIGTERM or SIGABRT
updater.idle()
