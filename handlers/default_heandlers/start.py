from loader import bot


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(chat_id=message.chat.id, text='Hey!\nIf you wanna get bot commands enter /help')
