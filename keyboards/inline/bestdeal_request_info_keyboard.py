from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def bestdeal_request_info_keyboard() -> InlineKeyboardMarkup:
    keyboard_for_answer = InlineKeyboardMarkup()
    keyboard_for_answer.add(InlineKeyboardButton(text='Correct', callback_data='ready'),
                            InlineKeyboardButton(text='Restart', callback_data='restart_ask_for_photos_callback'))
    return keyboard_for_answer
