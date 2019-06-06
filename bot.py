# -*- coding: utf-8 -*-
from config import *
import telebot
import utils
from SQLighter import SQLighter
import random
import os
from flask import Flask, request
import datetime


bot = telebot.TeleBot(token)

server = Flask(__name__)
now = datetime.datetime.now


"""class randomrow:
    def __init__(self,rownum):
        self.rownum = rownum
    def rand(self):
        return random.randint(1,201) #жуткий костыль
"""
@server.route('/' + token, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://polar-journey-94573.herokuapp.com/' + token)
    return "?", 200 
    
"""@bot.message_handler(commands=['start'])
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
    if message.text == "/tel":
        bot.send_message(message.from_user.id, "Введи номер телефона")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Это поиск в табличке людей. /tel - поиск по номеру телефона")
    else:
        t = message.text;
        bot.send_message(message.from_user.id, "Выполнить поиск по этому телефон - %s" %t)
        db_worker = SQLighter(database_name)
        rows = db_worker.select_single(t)
        with db_worker.connection:
            operation = 'SELECT * FROM questions WHERE tel = t'
            for result in cursor.execute(operation, multi=True):
                if result.with_rows:
                    bot.send_message(message.chat.id, "По этому телефону '{}':".format(result.statement))
                    bot.send_message(message.chat.id, (result.fetchall())
              else:
                    bot.send_message(message.chat.id, "Number of rows affected by statement '{}': {}".format(result.statement, result.rowcount))
        
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
 """         
if __name__ == '__main__':
    server.run(host="0.0.0.0", port=os.environ.get('PORT', 80)) 

       
    
    
