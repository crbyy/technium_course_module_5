import os
import telebot
from telebot import types
import datetime
from datetime import datetime
import sqlite3

tok = os.getenv("TG_TOKEN")
bot = telebot.TeleBot(tok)

#db
conn = sqlite3.connect('sleepbot.db')
cursor = conn.cursor()

#users
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        name TEXT
)
''')

#sleep_records
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sleep_records(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER REFERENCES users(id),
        sleep_time DATETIME,
        wake_time DATETIME,
        sleep_quality INTEGER
)
''')

#notes
cursor.execute('''
    CREATE TABLE IF NOT EXISTS notes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT,
        sleep_record_id INTEGER REFERENCES sleep_records(id)
)
''')
conn.commit()
conn.close()

temp_data = {}


@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('sleepbot.db')
    cursor = conn.cursor()

    user_id = str(message.from_user.id)
    user_name = str(message.from_user.username)

    cursor.execute('''
        INSERT OR IGNORE INTO users(id, name) VALUES (?, ?)''', (user_id, user_name))
    conn.commit()


    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    sleep_button = types.KeyboardButton('/sleep')
    wake_button = types.KeyboardButton('/wake')
    sleep_quality_button = types.KeyboardButton('/quality')
    notes_button = types.KeyboardButton('/notes')

    markup.add(sleep_button, wake_button,sleep_quality_button, notes_button)

    bot.reply_to(message, "Привет! Я помогу отслеживать тебе твои параметры сна. У меня есть команды /sleep, /wake, "
                          "/quality, /notes", reply_markup=markup)

    conn.close()


@bot.message_handler(commands=['sleep'])
def sleep(message):
    conn = sqlite3.connect('sleepbot.db')
    cursor = conn.cursor()

    user_id = str(message.from_user.id)

    sleeptime = datetime.now()
    strsleeptime = sleeptime.strftime("%H:%M:%S")

    if user_id in temp_data:
        bot.send_message(message.chat.id, "Вы уже уснули. Сначала используйте /wake")
        return

    temp_data[user_id] = sleeptime #Добавляем sleeptime для проверки


    cursor.execute('''
        INSERT OR IGNORE INTO sleep_records(user_id, sleep_time) 
        VALUES (?, ?)''', (user_id, sleeptime))#Добавляем sleeptime  на каждый отдельный id в db
    conn.commit()
    conn.close()

    bot.send_message(message.from_user.id,f'Вы засыпаете в: {strsleeptime}')



@bot.message_handler(commands=['wake'])
def wake(message):
    conn = sqlite3.connect('sleepbot.db')
    cursor = conn.cursor()

    user_id = str(message.from_user.id)

    if user_id not in temp_data: # проверка на двойной wake
        bot.send_message(message.from_user.id, 'Кажется, вы не нажали /sleep')
        return

    waketime = datetime.now()
    sleeptime = temp_data.get(user_id) # Тащим из временного словаря для duration
    strwaketime = waketime.strftime("%H:%M:%S")

    duration = waketime - sleeptime



    cursor.execute('''
        UPDATE sleep_records
        SET wake_time = ?
        WHERE user_id = ?
            AND wake_time IS NULL
        ''', (waketime, user_id))

    conn.commit()
    conn.close()





    hours = duration.seconds // 3600
    minutes = (duration.seconds % 3600) // 60
    seconds = duration.seconds % 60


    bot.send_message(message.from_user.id, f'Вы просыпаетесь в: {strwaketime}, Вы спали: {hours} ч. '
                                           f'{minutes} мин. '
                                           f'{seconds} сек.')
    bot.send_message(message.from_user.id, 'Не забудьте оставить оценку с помощью команды /quality,'
                                           '\nРасскажите как спалось с помощью команды /notes')

    del temp_data[user_id] #Удаление временных данных



@bot.message_handler(commands=['quality'])
def quality(message):
    conn = sqlite3.connect('sleepbot.db')
    cursor = conn.cursor()

    user_id = str(message.from_user.id)
    msg = message.text.split()

    if user_id in temp_data:
        bot.send_message(message.chat.id, "Сначала завершите сон командой /wake")
        return

    if len(msg) != 2:
        bot.send_message(message.chat.id, 'Используйте: /quality <оценка>')
        return

    try:
        quality = int(msg[1]) #оценка
        if quality < 1 or quality > 10:
            bot.send_message(message.chat.id, 'Оценка должна быть от 1 до 10')
            return
    except ValueError:
        bot.send_message(message.chat.id, 'Оценка должна быть числом')
        return

    cursor.execute('''
        UPDATE sleep_records
        SET sleep_quality = ?
        WHERE user_id = ? 
            AND sleep_quality IS NULL
        ''', (quality, user_id))

    conn.commit()
    conn.close()

@bot.message_handler(commands=['notes'])
def notes(message):
    conn = sqlite3.connect('sleepbot.db')
    cursor = conn.cursor()

    user_id = str(message.from_user.id)

    msg = message.text.split(maxsplit=1)

    if len(msg) < 2:
        bot.send_message(message.chat.id, 'Используйте: /notes <текст заметки>')
        return

    note = msg[1].strip()
    if not note:
        bot.send_message(message.chat.id, 'Текст заметки не может быть пустым')
        return

    cursor.execute('''
        SELECT id FROM sleep_records
        WHERE user_id = ? 
            AND wake_time IS NOT NULL 
        ORDER BY id DESC LIMIT 1''', (user_id,))

    row = cursor.fetchone()
    if not row:
        bot.send_message(message.chat.id, 'Сначала завершите сон командами /sleep и /wake')
        return

    sleep_record_id = row[0]

    cursor.execute('''
        INSERT INTO notes (text, sleep_record_id)
        VALUES (?, ?) ''', (note, sleep_record_id))
    conn.commit()




bot.polling(none_stop=True)