from telebot.types import Message

from database.get_history import get_history
from loader import bot


@bot.message_handler(commands=['history'])
def show_history(message: Message):
    data = get_history(message.from_user.id)
    if len(data) != 0:
        for i_hotel in data:
            bot.send_message(chat_id=message.chat.id, text='❓Request:\n'
                                                           f'⌛Searched time: {i_hotel[0]}\n'
                                                           f'🏙️City: {i_hotel[1]}\n'
                                                           f'⚙Command: {i_hotel[5]}\n'
                                                           f'Arrival_date: {i_hotel[2]}\n'
                                                           f'Leave_date: {i_hotel[3]}\n'
                                                           f'\n✔Result:\n'
                                                           f'🏠Hotel name: {i_hotel[6]}\n'
                                                           f'📍Hotel adress: {i_hotel[7]}\n'
                                                           f'Price per period: {i_hotel[4]}\n'
                                                           f'💸Price per day: {i_hotel[8]}\n')

    else:
        bot.send_message(chat_id=message.chat.id, text='🔎History is clear')