import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands = ['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Hi lol')
    markup.add(item1)

    bot.send_message(message.chat.id, 'Hi red monkey'.format(message.from_user), reply_markup = markup)


bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop = True)
