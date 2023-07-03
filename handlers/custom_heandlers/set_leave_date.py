from loader import bot
from states.steps import UserStates
import datetime
from config_data import config


@bot.message_handler(state=UserStates.set_leave_date)
def set_leave_date(message):
    bot.set_state(message.chat.id, state=UserStates.ask_photos)
    with bot.retrieve_data(user_id=message.from_user.id) as state_data:
        state_data['period'] = message.text
        state_data['leave_date'] = f"{(datetime.datetime.strptime(state_data['arrival_date'], '%d.%m.%Y') + datetime.timedelta(days=int(message.text))).strftime('%d.%m.%Y')}"
        if state_data['command'] == 'lowprice' or state_data['command'] == 'highprice':
            bot.send_message(chat_id=message.chat.id, text=f'How many hotels to show (max {config.max_hotels})❓')
        else:
            bot.set_state(message.chat.id, state=UserStates.price_min)
            bot.send_message(message.chat.id, text='💰Enter the minimum price per day (minimum 100$)')