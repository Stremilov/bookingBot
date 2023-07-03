from telebot.types import Message

from loader import bot
from states.steps import UserStates

from config_data.config import DetailedTelegramCalendar, LSTEP


def build_calendar(id_for_build):
    calendar, step = DetailedTelegramCalendar().build()
    bot.send_message(chat_id=id_for_build,
                     text=f"Select {LSTEP[step]}",
                     reply_markup=calendar)

@bot.message_handler(state=UserStates.get_quantity_hotels)
def get_quantity_hotels(message: Message):
    bot.set_state(message.chat.id, state=UserStates.price_min)
    with bot.retrieve_data(user_id=message.from_user.id) as state_data:
        state_data['quantity_hotels'] = message.text
        build_calendar(id_for_build=message.chat.id)


@bot.message_handler(state=UserStates.price_min)
def get_price_min(message: Message):
    """
    Функция сохраняет минимальную цену за сутки в отеле.
    """
    if 1 > int(message.text):
        bot.send_message(chat_id=message.chat.id, text="Error!")
        return
    elif not message.text.isdigit():
        bot.send_message(chat_id=message.chat.id, text="Error!")
        return
    else:
        if message.text == '0':
            bot.set_state(message.chat.id, state=UserStates.price_max)
            with bot.retrieve_data(user_id=message.from_user.id) as state_data:
                state_data['price_min'] = '1'
        else:
            price_min = message.text
            bot.set_state(message.chat.id, state=UserStates.price_max)
            with bot.retrieve_data(user_id=message.from_user.id) as state_data:
                state_data['price_min'] = price_min
            bot.send_message(chat_id=message.chat.id, text='💰Enter the maximum price per day ($)')
