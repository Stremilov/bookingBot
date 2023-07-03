from telebot.types import Message

import config_data.config
from keyboards.inline.ask_for_photo_keyboard import ask_for_photo_keyboard
from keyboards.inline.bestdeal_keyboard_if_no_photo import \
    bestdeal_keyboard_if_no_photo
from keyboards.inline.bestdeal_request_info_keyboard import \
    bestdeal_request_info_keyboard
from keyboards.inline.lowprice_highprice_keyboard_if_no_photo import \
    lowprice_highprice_keyboard_if_no_photo
from keyboards.inline.lowprice_highprice_request_info_keyboard import \
    lowprice_highprice_request_info_keyboard
from keyboards.inline.question_keyboard_for_photo import \
    question_keyboard_for_photo
from loader import bot
from states.steps import UserStates


@bot.message_handler(state=UserStates.ask_photos)
def ask_for_photos(message: Message):
    bot.set_state(message.chat.id, state=UserStates.create_dict)
    with bot.retrieve_data(user_id=message.from_user.id) as state_data:
        if state_data['command'] == 'lowprice' or state_data['command'] == 'highprice':
            state_data['quantity_hotels'] = message.text
            keyboard = ask_for_photo_keyboard()
            bot.send_message(message.chat.id, text='Show photos❓', reply_markup=keyboard)
        else:
            keyboard = ask_for_photo_keyboard()
            bot.send_message(message.chat.id, text='Show photos❓', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'yes' or call.data == 'no' or call.data == 'restart_ask_for_photos_callback')
def ask_for_photos_callback(call):
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='✔Sucsessfully')
    if call.data == 'yes':
            bot.send_message(call.message.chat.id,
                             text=f'How many photos to show (max {config_data.config.max_photos})❓')
            bot.set_state(call.message.chat.id, state=UserStates.quantity_photos)
    else:
        bot.set_state(call.message.chat.id, state=UserStates.create_dict)
        with bot.retrieve_data(user_id=call.from_user.id) as state_data:
            if state_data['command'] == 'bestdeal':
                state_data['quantity_photos'] = '0'
                keyboard = bestdeal_keyboard_if_no_photo()
                bot.send_message(chat_id=call.message.chat.id,
                                 text='❓ Your request:\n'
                                      f'🏙️ City: {state_data["city"]}\n'
                                      f'🖼 Photos to show: {state_data["quantity_photos"]}\n'
                                      f'💲Min price per day: {state_data["price_min"]}\n'
                                      f'💲Max price per day: {state_data["price_max"]}\n'
                                      f'🚗Distance from center: {state_data["distance"]}\n'
                                      f'⚙ Chosen command: {state_data["command"]}',
                                 reply_markup=keyboard)
            else:
                state_data['quantity_photos'] = '0'
                keyboard_for_answer = lowprice_highprice_keyboard_if_no_photo()
                bot.send_message(chat_id=call.message.chat.id,
                                 text='❓ Your request:\n'
                                      f'🏙️ City: {state_data["city"]}\n'
                                      f'🖼 Photos to show: {state_data["quantity_photos"]}\n'
                                      f'⚙ Chosen command: {state_data["command"]}',
                                 reply_markup=keyboard_for_answer)


@bot.message_handler(state=UserStates.quantity_photos)
def register_quantity_photo(message):
    bot.set_state(message.chat.id, state=UserStates.create_dict)
    with bot.retrieve_data(user_id=message.from_user.id) as state_data:
        state_data['quantity_photos'] = message.text
        keyboard_for_answer = question_keyboard_for_photo()
        bot.send_message(chat_id=message.chat.id,
                         text=f'🖼 Photos to show: {state_data["quantity_photos"]}\n'
                              'All correct❓',
                         reply_markup=keyboard_for_answer)


@bot.callback_query_handler(func=lambda call: call.data == 'ready_to_get_photo')
def get_photos(call):
    """
    Функция сохраняет данные о кол-ве отелей для вывода пользователю.
    """
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='✔Confirmed')
    if call.data == 'ready_to_get_photo':
        with bot.retrieve_data(user_id=call.from_user.id) as state_data:
            if state_data['command'] == 'bestdeal':
                keyboard_for_answer = bestdeal_request_info_keyboard()
                bot.send_message(chat_id=call.message.chat.id,
                                 text='❓ Your request:\n'
                                      f'🏙️ City: {state_data["city"]}\n'
                                      f'🏠 Hotels to show: {state_data["quantity_hotels"]}\n'
                                      f'🖼 Photos to show: {state_data["quantity_photos"]}\n'
                                      f'💸Minimal price per day: {state_data["price_min"]}\n'
                                      f'💸Maximum price per day: {state_data["price_max"]}\n'
                                      f'📍Distance from center {state_data["distance"]}\n'
                                      f'⚙ Chosen command: {state_data["command"]}',
                                 reply_markup=keyboard_for_answer)
            else:
                keyboard_for_answer = lowprice_highprice_request_info_keyboard()
                bot.send_message(call.message.chat.id,
                                 text='❓ Your request:\n'
                                      f'🏙️ City: {state_data["city"]}\n'
                                      f'🏠 Hotels to show: {state_data["quantity_hotels"]}\n'
                                      f'🖼 Photos to show: {state_data["quantity_photos"]}\n'
                                      f'⚙ Chosen command: {state_data["command"]}',
                                 reply_markup=keyboard_for_answer)
