import telebot

BOT_TOKEN = '7964698487:AAGWCD_WRTwxD-8fXtywrR5jGQkDwcETxWw'
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.send_message(message.chat.id, message.text)

bot.polling()