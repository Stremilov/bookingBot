import os

from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP

from dotenv import find_dotenv, load_dotenv

if not find_dotenv():
    exit('Переменные окружения не загружены т.к отсутствует файл ..env')
else:
    load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
RAPID_API_KEY = os.getenv('RAPID_API_KEY')
headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": RAPID_API_KEY,
    "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
}

DEFAULT_COMMANDS = (
    ('start', "Start bot"),
    ('help', "Output help"),
    ('lowprice', "Top cheap hotels"),
    ('highprice', "Top expensive hotels"),
    ('bestdeal', "Hotels with prices in the range"),
    ('history', "History"),
)

db_file = "/Users/levstremilov/PycharmProjects/bot_base.db"
max_hotels = 5
max_photos = 5

LSTEP = {'y': 'year', 'm': 'month', 'd': 'day'}
