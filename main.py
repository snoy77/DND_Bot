import telebot
from telebot import types

import random as rand

import BotStatusPrinter as BSP
import telegainfo as TI

#----------------Инициализация бота----------------
BSP.stopForDebug(0, 'Подключение к боту...')
bot = telebot.TeleBot(TI.token)
BSP.stopForDebug(0, 'Подключение к боту... УСПЕШНО')

#----------------Определение событий----------------
BSP.stopForDebug(0, 'Инициализация функций...')

@bot.message_handler(commands=['d4', 'd6', 'd10', 'd20'])
def diceDrop(message):
    BSP.stopForDebug(0, 'diceDrop начало', 0)

    chat_id = message.chat.id
    message_text = message.text
    message_data = message.date

    BSP.printStatusBot(message_data, chat_id, message_text, 0)
    dice_index = int(message_text.replace('/d', ''))
    dice_result = rand.randint(1, dice_index)

    goint_message = str(dice_result) + '\nНу да...'

    bot.send_message(chat_id, goint_message)
    #bot.send_message(chat_id, 'Мне похуй')
    BSP.printStatusBot(message_data, chat_id, goint_message, 1)

    BSP.stopForDebug(0, 'diceDrop Конец', 0)


@bot.message_handler(commands=['start', 'clr'])
def startCommand(message):
    BSP.stopForDebug(0, "startCommand начало", 0)

    chat_id = message.chat.id
    message_text = message.text
    message_data = message.date

    BSP.printStatusBot(message_data, chat_id, message_text, 0)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard_buttons = []

    if message_text == '/clr':
        keyboard = types.ReplyKeyboardRemove()
        goint_message = 'Убираю клаву...'
    elif message_text == '/start':

        goint_message = 'Начинаем игру!'
        button_d4 = types.KeyboardButton('/d4')
        button_d6 = types.KeyboardButton('/d6')
        button_d10 = types.KeyboardButton('/d10')
        button_d20 = types.KeyboardButton('/d20')

        button_clr = types.KeyboardButton('/clr')

        keyboard.add(button_d4)
        keyboard.add(button_d6)
        keyboard.add(button_d10)
        keyboard.add(button_d20)
        keyboard.add(button_clr)

    bot.send_message(chat_id, goint_message, reply_markup = keyboard)
    BSP.printStatusBot(message_data, chat_id, goint_message, 1)
    BSP.stopForDebug(0, "startCommand Конец", 0)

@bot.message_handler(content_types=['text'])
def message_going(message):
    BSP.stopForDebug(0, "message_going начало", 0)

    chat_id = message.chat.id
    message_text = message.text
    message_data = message.date

    BSP.printStatusBot(message_data, chat_id, message_text, 0)
    #BSP.stopForDebug(0, "message_going - Попытка отправки ответа...", 0)

    if message_text.lower() == 'github' or message_text.lower() == "гитхаб":
        going_message = "[Гитхаб этого бота:](https://github.com/snoy77/DND_Bot)"
        bot.send_message(chat_id, going_message, parse_mode='Markdown')
    elif message_text.lower() == 'живой?' or message_text.lower() == 'жив?' or message_text.lower() == 'ты жив?':
        going_message = "Агась"
        bot.send_message(chat_id, going_message)
        bot.send_sticker(chat_id, 'CAACAgEAAxkBAAPkYn5t2aAkAAGiipkFKzpGvXz4bsUcAAJaAAPArAgjmrw81VndF8IkBA')
    else:
        going_message = 'Не понял, разъясни почётче...'
        bot.send_message(chat_id, going_message)

    BSP.printStatusBot(message_data, chat_id, going_message, 1)

    BSP.stopForDebug(0, "message_going Конец", 0)

BSP.stopForDebug(0, 'Инициализация функций... УСПЕШНО', 1)


#----------------Запуск бота----------------
print('Работа бота...\n')
bot.polling(none_stop=True, interval=0)
print('\n\nРабота бота ЗАВЕРШЕНА')

BSP.stopForDebug(1)
