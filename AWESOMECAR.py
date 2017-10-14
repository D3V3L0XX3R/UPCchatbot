#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Basic example for a bot that uses inline keyboards.
# This program is dedicated to the public domain under the CC0 license.

import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)

'''logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
					level=logging.INFO)'''


def startcar(bot, chat_id, update):
	update.message.reply_text(
		'How much money is your maximum?',
		reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
	if update.message.text < '50':
		bot.edit_message_text(text="Oh sorry, you are so poor", chat_id=query.message.chat_id, message_id=query.message.message_id)
	else:
		bot.edit_message_text(text="Well", chat_id=query.message.chat_id, message_id=query.message.message_id)
	#bot.send_message(chat_id=query.message.chat_id, text=AWESOMECAR.startcar())


'''def button(bot, update):
	pass


def help(bot, update):
	update.message.reply_text("This bot can help you to plan your desired trip in just few clicks!! Use /start to begin.")


def error(bot, update, error):
	logging.warning('Update "%s" caused error "%s"' % (update, error))


# Create the Updater and pass it your bot's token.
updater = Updater("383425697:AAH4OZM2RhjZTuHM_yBkt4ili9FKIuAMO3c")

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(button))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_error_handler(error)

# Start the Bot
updater.start_polling()

# Run the bot until the user presses Ctrl-C or the process receives SIGINT,
# SIGTERM or SIGABRT
updater.idle()'''
