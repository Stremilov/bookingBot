from loader import bot
from config_data.config import DetailedTelegramCalendar, LSTEP
from states.steps import UserStates
import datetime


@bot.callback_query_handler(func=DetailedTelegramCalendar.func())
def cal(call):
    result, key, step = DetailedTelegramCalendar(min_date=datetime.date.today()).process(call.data)
    if not result and key:
        bot.edit_message_text(f"Select {LSTEP[step]}",
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=key)
    elif result:
        bot.edit_message_text(f"You selected {result}",
                              call.message.chat.id,
                              call.message.message_id)
        bot.set_state(call.message.chat.id, state=UserStates.set_leave_date)
        with bot.retrieve_data(user_id=call.from_user.id) as state_data:
            state_data['arrival_date'] = result.strftime('%d.%m.%Y')
        bot.send_message(chat_id=call.message.chat.id, text='For how many days❓')