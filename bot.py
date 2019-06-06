# -*- coding: utf-8 -*-
from config import *
import telebot
"""import utils
from SQLighter import SQLighter
import random
import os
from flask import Flask, request
import datetime"""


bot = telebot.TeleBot(token)
bot.polling(none_stop=True, interval=0)
"""
server = Flask(__name__)
now = datetime.datetime.now


class randomrow:
    def __init__(self,rownum):
        self.rownum = rownum
    def rand(self):
        return random.randint(1,201) #жуткий костыль

@server.route('/' + token, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://enigmatic-river-40567.herokuapp.com/' + token)
    return "?", 200 
    
@bot.message_handler(commands=['start'])
def start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    user_markup.row('Почати')
    bot.send_message(message.chat.id, 'Щоб ввести номер телефону оберіть /search')

@bot.message_handler(commands=['search'])
def game(message):
    bot.send_message(message.chat.id, 'номер без 0')
    answer = utils.get_answer_for_user(message.chat.id)
    db_worker = SQLighter(database_name)
    rows = db_worker.select_single(answer) 
    bot.send_message(message.chat.id, rows)
    db_worker.close()
"""
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
"""
@bot.message_handler(func=lambda message: True, content_types=['text'])
def check_answer(message):
    answer = utils.get_answer_for_user(message.chat.id)
    if not answer:
        bot.send_message(message.chat.id, 'Щоб почати наступне питання, оберіть команду /test')
    else:
        keyboard_hider = telebot.types.ReplyKeyboardRemove()
        if message.text == answer:
            bot.send_message(message.chat.id, "Так! Далі - /test", reply_markup=keyboard_hider)
        else:
            bot.send_message(message.chat.id, "Ні, правильна відповідь: %s. Далі - /test" %answer, reply_markup=keyboard_hider)
        utils.finish_user_game(message.chat.id)
          
if __name__ == '__main__':
    func()
    
    server.run(host="0.0.0.0", port=os.environ.get('PORT', 80)) 
    utils.count_rows() 
    random.seed() """
       
    
    
