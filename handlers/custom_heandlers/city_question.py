import datetime

from loguru import logger
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from api_work.request_for_city import request_for_place
from api_work.request_for_city_places import request_for_city_places
from config_data import config
from loader import bot
from states.steps import UserStates

from config_data.config import DetailedTelegramCalendar, LSTEP


def build_calendar(id_for_build):
    calendar, step = DetailedTelegramCalendar().build()
    bot.send_message(chat_id=id_for_build,
                     text=f"Select {LSTEP[step]}",
                     reply_markup=calendar)


def choose_city_place_markup(city) -> InlineKeyboardMarkup:
    cities = request_for_city_places(city)
    keyboard = InlineKeyboardMarkup()
    for i_city in cities:
        keyboard.add(InlineKeyboardButton(text=i_city['city_name'], callback_data=f'{i_city["destination_id"]}'))
    return keyboard


@bot.message_handler(commands=['lowprice', 'highprice', 'bestdeal'])
def city_question(message: Message):
    bot.send_message(chat_id=message.chat.id, text='Where will we look❓')
    bot.set_state(message.chat.id, state=UserStates.choose_current_place)
    with bot.retrieve_data(chat_id=message.chat.id, user_id=message.from_user.id) as state_data:
        state_data['user_personal_id'] = message.from_user.id
        state_data['command_time'] = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        state_data['command'] = message.text.lstrip('/')


@bot.message_handler(state=UserStates.choose_current_place)
def city(message):
    with bot.retrieve_data(user_id=message.from_user.id) as state_data:
        state_data['city'] = message.text
    bot.send_message(message.from_user.id, 'Refine, please:', reply_markup=choose_city_place_markup(message.text))


@bot.callback_query_handler(func=lambda call: call.data.isdigit())
def callback_data(call):
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='✔Place has been chosen')
    loading = bot.send_message(chat_id=call.message.chat.id, text='Searching...')
    result = request_for_place(gaiaId=call.data)
    if result:
        bot.delete_message(call.message.chat.id, message_id=loading.message_id)
        bot.set_state(call.message.chat.id, state=UserStates.create_dict)
        with bot.retrieve_data(user_id=call.from_user.id) as state_data:
            for hotel in result['data']['propertySearch']['properties']:
                if hotel['regionId'] != "0":
                    state_data['regionId'] = hotel['regionId']
                    break
            if state_data['command'] == 'lowprice' or state_data['command'] == 'highprice':
                bot.set_state(call.message.chat.id, state=UserStates.set_arrival_date)
                build_calendar(id_for_build=call.message.chat.id)
            else:
                bot.set_state(call.message.chat.id, state=UserStates.get_quantity_hotels)
                bot.send_message(call.message.chat.id, text=f'How many hotels to show (max {config.max_hotels})❓')
    else:
        logger.info('No info about city (info)!')
        bot.send_message(chat_id=call.message.chat.id, text='Nothing has been found for your request')
