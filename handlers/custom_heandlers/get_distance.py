from telebot.types import Message

from keyboards.inline.ask_for_photo_keyboard import ask_for_photo_keyboard
from loader import bot
from states.steps import UserStates


@bot.message_handler(state=UserStates.distance)
def get_distance(message: Message):
    """
    Функия сохраняет макимальное расстояние от отеля до центра.
    """
    if 1 > float(message.text):
        bot.send_message(chat_id=message.chat.id,
                         text="Error!")
        return
    elif not message.text.isdigit():
        bot.send_message(chat_id=message.chat.id, text="Error!")
        return
    else:
        bot.set_state(message.chat.id, state=UserStates.create_dict)
        with bot.retrieve_data(user_id=message.from_user.id) as state_data:
            state_data['distance'] = message.text
        keyboard = ask_for_photo_keyboard()
        bot.send_message(message.chat.id, text='Show photos?', reply_markup=keyboard)
