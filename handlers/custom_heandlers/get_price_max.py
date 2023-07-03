from telebot.types import Message

from loader import bot
from states.steps import UserStates


@bot.message_handler(state=UserStates.price_max)
def get_price_max(message: Message):
    """
    Функция сохраняет максимльную цену за сутки в отеле.
    """
    if 1 > int(message.text):
        bot.send_message(chat_id=message.chat.id, text="Error!")
        return
    elif not message.text.isdigit():
        bot.send_message(chat_id=message.chat.id, text="Error!")
        return
    else:
        bot.set_state(message.chat.id, state=UserStates.distance)
        with bot.retrieve_data(user_id=message.from_user.id) as state_data:
            state_data['price_max'] = message.text
        bot.send_message(chat_id=message.chat.id, text='📌Enter the maximum distance from the center (miles)')
