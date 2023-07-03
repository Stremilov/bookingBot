from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def lowprice_highprice_keyboard_if_no_photo() -> InlineKeyboardMarkup:
    keyboard_for_answer = InlineKeyboardMarkup()
    keyboard_for_answer.add(InlineKeyboardButton(text='Yes', callback_data='ready'),
                            InlineKeyboardButton(text='No', callback_data='restart_ask_for_photos_callback'))
    return keyboard_for_answer