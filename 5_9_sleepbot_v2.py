import os
from json import JSONDecodeError

import telebot
from mypy.util import json_dumps
from telebot import types
import datetime
from datetime import datetime, timedelta
import json


tok = os.getenv("TG_TOKEN")
bot = telebot.TeleBot(tok)

def load_data():
    try:
        with open ('sleepbot_data.json', 'r', encoding='utf_8') as f:
            return json.load(f)
    except JSONDecodeError:
        return {}

def save_data():
    with open('sleepbot_data.json', 'w', encoding = 'utf-8') as f:
        json.dump(user_data, f, indent=4, ensure_ascii = False)



user_data = load_data()
temp_data = {}


@bot.message_handler(commands=['start'])
def start(message):

    user_id = str(message.from_user.id)
    if user_id not in user_data:
        user_data[user_id] = []


    bot.reply_to(message, "Привет! Я помогу отслеживать тебе твои параметры сна. У меня есть команды /sleep, /wake")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    button1 = types.KeyboardButton('/sleep')
    button2 = types.KeyboardButton('/wake')

    markup.add(button1, button2)
    reply_markup=markup


@bot.message_handler(commands=['sleep'])
def sleep(message):
    user_id = str(message.from_user.id)

    sleeptime = datetime.now()
    strsleeptime = sleeptime.strftime("%H:%M:%S")


    temp_data[user_id] = sleeptime     #Добавляем sleeptime временно на каждый отдельный id

    bot.send_message(message.from_user.id,f'Вы засыпаете в: {strsleeptime}')


@bot.message_handler(commands=['wake'])
def wake(message):

    user_id = str(message.from_user.id)

    if user_id not in temp_data:
        bot.send_message(message.from_user.id, 'Кажется, вы не нажали /sleep')
        return

    waketime = datetime.now()
    sleeptime = temp_data.get(user_id) # Тащим из временного словаря для duration
    strsleeptime = sleeptime.strftime("%H:%M:%S")
    strwaketime = waketime.strftime("%H:%M:%S")

    duration = waketime - sleeptime
    strduration = str(duration)


    user_data[user_id].append({
            'sleep_time': strsleeptime,
            'wake_time': strwaketime,
            'duration': strduration
     })

    hours = duration.seconds // 3600
    minutes = (duration.seconds % 3600) // 60
    seconds = duration.seconds % 60


    bot.send_message(message.from_user.id, f'Вы просыпаетесь в: {strwaketime}, Вы спали: {hours} ч. '
                                           f'{minutes} мин. '
                                           f'{seconds} сек.')

    save_data()

    del temp_data[user_id]

bot.polling(none_stop=True)