from art import tprint
from loguru import logger
from telebot.custom_filters import StateFilter

import handlers
from loader import bot
from utils.set_bot_commands import set_default_commands
from database.create_tables import create_tables

if __name__ == '__main__':
    tprint("bot by lev", font="block", chr_ignore=True)
    logger.add('debug_file', format='{time} {level} {message}', level='DEBUG', rotation='6:00', compression='zip')
    create_tables()
    set_default_commands(bot)
    bot.add_custom_filter(StateFilter(bot))
    bot.infinity_polling()
