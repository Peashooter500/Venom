import telebot
import keyboards
import fsm

BOT_TOKEN = '7964698487:AAGWCD_WRTwxD-8fXtywrR5jGQkDwcETxWw'
stater = fsm.FSM()
bot = telebot.TeleBot(BOT_TOKEN)


def handle_default_state(message):
    if message.text == "Фото":
        stater.set_state(message.chat.id, fsm.IMAGE_STATE)
        bot.send_message(message.chat.id, text="Опиши фото(на английском)",reply_markup=keyboards.back)
    elif message.text == "Текст":
        stater.set_state(message.chat.id, fsm.TEXT_STATE)
        bot.send_message(message.chat.id, text="Напиши что-нибудь",reply_markup=keyboards.back)
    else:
        return_to_menu(message.chat.id)

def handle_image_state(message):
    if message.text == "Меню":
        return_to_menu(message.chat.id)
    else:
        bot.send_message(message.chat.id, text="Скоро буду генерировать фото ...",)

def handle_text_state(message):
    if message.text == "Меню":
        return_to_menu(message.chat.id)
    else:
        bot.send_message(message.chat.id, text="Скоро буду генерировать текст ...",)
def return_to_menu(chat_id):
    stater.set_state(chat_id, fsm.DEFAULT_STATE)
    bot.send_message(chat_id, text="Главное меню",reply_markup=keyboards.start)

@bot.message_handler(func=lambda message: True)
def echo(message):
    state = stater.get_state(message.chat.id)
    msg_text = message.text
    if state == fsm.DEFAULT_STATE :
        handle_default_state(message)
    elif state == fsm.IMAGE_STATE:  
        handle_image_state(message)
    elif state == fsm.TEXT_STATE:
        handle_text_state(message)
    else:
        return_to_menu(message.chat.id)

bot.polling()