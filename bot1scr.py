# -*- coding: utf-8 -*-

import telebot
import random
import time
import os
from telebot import types
import parse_horo
import parse_value

bot = telebot.TeleBot('1226621771:AAH5KfIqUe3qhmF1eJMPFVC678xx8_kFy_g')



@bot.message_handler(commands=['start','help'])
def start_message(message):

    bot.send_message(message.chat.id, 'Здравствуй. Для того, что бы воспользоваться моими функциями - напиши "Гороскоп" или "Курс" ')


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # Если нажали на одну из 12 кнопок — выводим гороскоп
    if call.data == "1":
        num_sign = int(call.data)
        msg = parse_horo.get_horoscope_text(num_sign)
        bot.send_message(call.message.chat.id, msg)
    elif call.data == "2":
        num_sign = int(call.data)
        msg = parse_horo.get_horoscope_text(num_sign)
        bot.send_message(call.message.chat.id, msg)

    elif call.data == "3":
        num_sign = int(call.data)
        msg = parse_horo.get_horoscope_text(num_sign)
        bot.send_message(call.message.chat.id, msg)

    elif call.data == "4":
        num_sign = int(call.data)
        msg = parse_horo.get_horoscope_text(num_sign)
        bot.send_message(call.message.chat.id, msg)

    elif call.data == "5":
         num_sign = int(call.data)
         msg = parse_horo.get_horoscope_text(num_sign)
         bot.send_message(call.message.chat.id, msg)

    elif call.data == "6":
        num_sign = int(call.data)
        msg = parse_horo.get_horoscope_text(num_sign)
        bot.send_message(call.message.chat.id, msg)

    elif call.data == "7":
        num_sign = int(call.data)
        msg = parse_horo.get_horoscope_text(num_sign)
        bot.send_message(call.message.chat.id, msg)

    elif call.data == "8":
        num_sign = int(call.data)
        msg = parse_horo.get_horoscope_text(num_sign)
        bot.send_message(call.message.chat.id, msg)

    elif call.data == "9":
        num_sign = int(call.data)
        msg = parse_horo.get_horoscope_text(num_sign)
        bot.send_message(call.message.chat.id, msg)

    elif call.data == "10":
        num_sign = int(call.data)
        msg = parse_horo.get_horoscope_text(num_sign)
        bot.send_message(call.message.chat.id, msg)

    elif call.data == "11":
        num_sign = int(call.data)
        msg = parse_horo.get_horoscope_text(num_sign)
        bot.send_message(call.message.chat.id, msg)

    elif call.data == "12":
        num_sign = int(call.data)
        msg = parse_horo.get_horoscope_text(num_sign)
        bot.send_message(call.message.chat.id, msg)

    elif call.data == "eur":
        value_name = call.data
        bot.send_message(call.message.chat.id, parse_value.parse_data_value(value_name))

    elif call.data == "usd":
        value_name = call.data
        bot.send_message(call.message.chat.id, parse_value.parse_data_value(value_name))



@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == "гороскоп":

        bot.send_message(message.from_user.id, "Сейчас я расскажу тебе гороскоп на сегодня.")
        # Готовим кнопки
        keyboard_horo = types.InlineKeyboardMarkup()

        # По очереди готовим текст и обработчик для каждого знака зодиака

        key_oven = types.InlineKeyboardButton(text='Овен', callback_data='1')
        keyboard_horo.add(key_oven)  # И добавляем кнопку на экран

        key_telec = types.InlineKeyboardButton(text='Телец', callback_data='2')
        keyboard_horo.add(key_telec)

        key_bliznecy = types.InlineKeyboardButton(text='Близнецы', callback_data='3')
        keyboard_horo.add(key_bliznecy)

        key_rak = types.InlineKeyboardButton(text='Рак', callback_data='4')
        keyboard_horo.add(key_rak)

        key_lev = types.InlineKeyboardButton(text='Лев', callback_data='5')
        keyboard_horo.add(key_lev)

        key_deva = types.InlineKeyboardButton(text='Дева', callback_data='6')
        keyboard_horo.add(key_deva)

        key_vesy = types.InlineKeyboardButton(text='Весы', callback_data='7')
        keyboard_horo.add(key_vesy)

        key_scorpion = types.InlineKeyboardButton(text='Скорпион', callback_data='8')
        keyboard_horo.add(key_scorpion)

        key_strelec = types.InlineKeyboardButton(text='Стрелец', callback_data='9')
        keyboard_horo.add(key_strelec)

        key_kozerog = types.InlineKeyboardButton(text='Козерог', callback_data='10')
        keyboard_horo.add(key_kozerog)

        key_vodoley = types.InlineKeyboardButton(text='Водолей', callback_data='11')
        keyboard_horo.add(key_vodoley)

        key_ryby = types.InlineKeyboardButton(text='Рыбы', callback_data='12')
        keyboard_horo.add(key_ryby)

        # Показываем все кнопки сразу и пишем сообщение о выборе

        bot.send_message(message.from_user.id, text='Выбери свой знак зодиака', reply_markup=keyboard_horo)

    elif message.text.lower() == 'курс':
        bot.send_message(message.from_user.id, "Какая из валют тебя интересует?")

        keyboard_value = types.InlineKeyboardMarkup()

        key_eur = types.InlineKeyboardButton(text='Евро', callback_data='eur')
        keyboard_value.add(key_eur)

        key_usd = types.InlineKeyboardButton(text='Доллар', callback_data='usd')
        keyboard_value.add(key_usd)

        bot.send_message(message.from_user.id, text='Нажми на интересующую тебя валюту', reply_markup=keyboard_value)



    elif message.text == "/help":

        bot.send_message(message.from_user.id, "Воспользуйся моими функциями! Пиши - привет.")

    else:

        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


'''@bot.message_handler(content_types=["text"])
def repeat_messages(message): 
    bot.send_message(message.chat.id, message.text)

@bot.message_handler(commands=['test'])
def find_file_ids(message):
    for file in os.listdir(path="music"):
        if file.split('.')[-1] == 'ogg':
            f = open('music/'+file, 'rb')
            msg = bot.send_voice(message.chat.id, f, None)
            # А теперь отправим вслед за файлом его file_id
            bot.send_message(message.chat.id, msg.voice.file_id, reply_to_message_id=msg.message_id)
        time.sleep(3)'''

if __name__ == '__main__':
    bot.infinity_polling()
