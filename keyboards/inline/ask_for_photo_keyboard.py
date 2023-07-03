from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def ask_for_photo_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text='Yes', callback_data='yes'),
                 InlineKeyboardButton(text='No', callback_data='restart_ask_for_photos_callback'))
    return keyboard
