import telebot
import keyboards
BOT_TOKEN = '7964698487:AAGWCD_WRTwxD-8fXtywrR5jGQkDwcETxWw'
bot = telebot.TeleBot(BOT_TOKEN)
@bot.message_handler(func=lambda message: True)
def echo(message):
    msg_text = message.text
    if msg_text == "Фото":
        bot.send_message(message.chat.id, text="Опиши фото(на английском)",reply_markup=keyboards.back)
    elif msg_text == "Текст":
        bot.send_message(message.chat.id, text="Напиши что-нибудь",reply_markup=keyboards.back)
    elif msg_text == "Меню":
        bot.send_message(message.chat.id, text="Главное меню",reply_markup=keyboards.start)
    else:
        bot.send_message(message.chat.id, text="Ещё раз",reply_markup=keyboards.start)

bot.polling()