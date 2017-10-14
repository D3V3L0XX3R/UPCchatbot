#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Basic example for a bot that uses inline keyboards.
# This program is dedicated to the public domain under the CC0 license.

import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import AWESOMECAR

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def start(bot, update):
    keyboard = [[InlineKeyboardButton("Flight  ✈️", callback_data='1'),
                 InlineKeyboardButton("Hotel 🏨", callback_data='2')],

                [InlineKeyboardButton("Rent a car 🚙", callback_data='3')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Hi! What would you need?', reply_markup=reply_markup)


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
      bot.send_message(chat_id=chat_id, text=AWESOMECAR.startcar())

    else:
      bot.edit_message_text(text="RILLY NIGGA",
                            chat_id=query.message.chat_id,
                            message_id=query.message.message_id)


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
updater.idle()
