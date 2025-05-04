import telebot

start = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
button_picture = telebot.types.KeyboardButton(text="Фото")
button_text = telebot.types.KeyboardButton(text="Текст")
start.add(button_picture, button_text)

back = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
button_back = telebot.types.KeyboardButton(text="Меню")
back.add(button_back)