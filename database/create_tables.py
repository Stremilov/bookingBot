import sqlite3 as sq

from config_data import config


def create_tables() -> None:
    """Функция для создания БД и создания таблиц"""

    with sq.connect(config.db_file) as con:
        cur = con.cursor()
        cur.execute("""DROP TABLE IF EXISTS history""")

        cur.execute("""CREATE TABLE IF NOT EXISTS history(
        user_personal_id INTEGER,
        command_time TEXT,
        city TEXT,
        arrival_date TEXT,
        leave_date TEXT,
        price_per_period TEXT,
        command TEXT,
        hotel_name TEXT,
        hotel_adress TEXT,
        price_per_day TEXT,
        hotel_star_raiting TEXT)
        """)

        cur.execute("""CREATE TABLE IF NOT EXISTS photo(
        hotel_id TEXT,
        photo_url TEXT)
        """)