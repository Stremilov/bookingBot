from telebot import types

from api_work.start_getting_data import start
from database.get_photo_from_table import get_photo
from database.set_history import set_history
from loader import bot
from states.steps import UserStates


def form_media_group(photos: list, text: str) -> list:
    """Функция для формирования медиагруппы"""
    media: list = []
    for photo in photos:
        media.append(types.InputMediaPhoto(media=photo[0], caption=text))
    return media


@bot.callback_query_handler(func=lambda call: call.data == 'ready')
def work_func(call):
    """
    Основная функция, обрарабатывающая ответы пользователя.
    Формирует запросы к API и БД.
    """
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='✔Confirmed')
    bot.set_state(call.message.chat.id, state=UserStates.create_dict)
    with bot.retrieve_data(user_id=call.from_user.id) as state_data:
        user_personal_id = state_data['user_personal_id']
        city = state_data['city']
        arrival_date = state_data['arrival_date']
        leave_date = state_data['leave_date']
        period = state_data['period']
        quantity_photos = state_data['quantity_photos']
        quantity_hotels = state_data['quantity_hotels']
        command = state_data['command']
        command_time = state_data['command_time']
        price_min = state_data.get('price_min', '')
        price_max = state_data.get('price_max', '')
        distance = state_data.get('distance', '')
        destination_id = state_data['regionId']
    loaging = bot.send_message(chat_id=call.message.chat.id, text='Searching...')
    hotels, photos = start(
        list_par=[city, quantity_photos, quantity_hotels, command, price_min, price_max, distance,
                  destination_id, arrival_date, leave_date])
    if hotels is None or len(hotels) == 0:
        bot.send_message(chat_id=call.message.chat.id, text='No results')
    else:
        bot.delete_message(call.message.chat.id, message_id=loaging.message_id)
        for i_hotel in hotels:
            history = (user_personal_id, command_time, city, arrival_date, leave_date, round(int(period) * float(i_hotel[5])), command, i_hotel[1], i_hotel[3], round(float(i_hotel[5])), i_hotel[2])
            set_history(history=history)
            text: str = f'\n🏨{i_hotel[1]}' \
                        f'\n🌐Url: https://hotels.com/ho{i_hotel[0]}' \
                        f'\n💳Price per peroid of {int(period)} days: {round(int(period) * float(i_hotel[5]))}$' \
                        f'\n💳Price per day: {round(float(i_hotel[5]))}$' \
                        f'\n📌Distance from center: {i_hotel[4]} mile'
            got_photos: list = get_photo(hotel_id=i_hotel[0], limit=quantity_photos)
            if got_photos:
                media = form_media_group(photos=got_photos, text=text)
                if len(media) != 0:
                    bot.send_media_group(chat_id=call.message.chat.id, media=media)
            bot.send_message(chat_id=call.message.chat.id, text=text, disable_web_page_preview=True)
