import config
import telebot
from telebot import types
import re

bot = telebot.TeleBot(config.token)

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Привет', 'Пока', 'хех', 'отправь картинку')

# отправка картинки
def send_img(message):
    f = open('sl.jpg', 'rb')
    bot.send_photo(message.chat.id, f, None)

# отправка клавиатуры в воздухе
def send_inline_murkup(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти на Яндекс", url="https://ya.ru")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Привет, создатель! Нажми на кнопку и перейди в поисковик.", reply_markup=keyboard)

# отправка клавиатуры
@bot.message_handler(commands=['start'], content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

# обработка клавы
@bot.message_handler(content_types=['text'])
def send_text(message):
    print(message)
    if message.text.lower() == 'привет':
        send_inline_murkup(message)
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif message.text.lower() == 'хех':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBE0RgYyKvsRyRvQFLX0lso3v8n3Ap3gACPQADJHFiGmptpaX1U366HgQ', reply_markup=keyboard1)
    elif message.text.lower() == 'отправь картинку':
        send_img(message=message)
    else:
        bot.send_message(message.chat.id, 'Я не знаю такой команды', reply_markup=keyboard1)


@bot.inline_handler(func=lambda query: len(query.query) > 0)
def query_text(query):
    print(query) # здесь лежит инфа о запросе
    kb = types.InlineKeyboardMarkup()
    # Добавляем колбэк-кнопку с содержимым "test"
    kb.add(types.InlineKeyboardButton(text="Нажми меня", callback_data="test", url="https://ya.ru"))
    results = []
    single_msg = types.InlineQueryResultCachedSticker(id=1, sticker_file_id='CAACAgIAAxkBAAEBE0RgYyKvsRyRvQFLX0lso3v8n3Ap3gACPQADJHFiGmptpaX1U366HgQ',
                                                      reply_markup=kb, input_message_content=types.InputTextMessageContent(message_text="Я тоже тебя люблю"))
    single_msg1 = types.InlineQueryResultCachedSticker(id=2,
                                                      sticker_file_id='CAACAgIAAxkBAAEBE05gYy7DOILjJKL1NkqxRzgx6oIaHQACtwIAAm0w5w-aSTnJZzzxAx4E',
                                                      reply_markup=kb,
                                                      input_message_content=types.InputTextMessageContent(
                                                          message_text="Я скучаю"))
    single_msg2 = types.InlineQueryResultCachedSticker(id=3,
                                                      sticker_file_id='CAACAgIAAxkBAAEBE0tgYy6rI_eTFD2tp4LiftvQS-HXRAACjRIAAujW4hIjixrmy5Za0R4E',
                                                      reply_markup=kb,
                                                      input_message_content=types.InputTextMessageContent(
                                                          message_text="Дождь"))
    results.append(single_msg)
    results.append(single_msg1)
    results.append(single_msg2)
    bot.answer_inline_query(query.id, results)



if __name__ == '__main__':
     bot.infinity_polling()
