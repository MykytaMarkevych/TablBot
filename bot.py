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

@server.route('/' + token, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://polar-journey-94573.herokuapp.com/' + token)
    return "?", 200 
    

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/tel":
        bot.send_message(message.from_user.id, "Введи номер телефона")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Это поиск в табличке людей. /tel - поиск по номеру телефона")
    else:
        t = message.text;
        connection = sqlite3.connect("tabl.db")
        cursor = connection.cursor()
        sql_theme = 'SELECT * FROM tabl WHERE tel=?'
        cursor.execute(sql_theme, (t,))
        theme_notes = cursor.fetchall()
        bot.send_message(message.from_user.id, theme_notes)

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000)) 

       
    
    
