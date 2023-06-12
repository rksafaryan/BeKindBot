import os

import telebot

from model import check_rudeness

BOT_TOKEN = 'secret'

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, check_rudeness(message.text))


bot.infinity_polling()
