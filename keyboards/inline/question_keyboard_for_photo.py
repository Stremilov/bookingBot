from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def question_keyboard_for_photo():
    keyboard_for_answer = InlineKeyboardMarkup()
    keyboard_for_answer.add(InlineKeyboardButton(text='Correct', callback_data='ready_to_get_photo'),
                            InlineKeyboardButton(text='Restart', callback_data='restart_ask_for_photos_callback'))
    return keyboard_for_answer
