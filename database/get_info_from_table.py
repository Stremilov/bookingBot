import sqlite3 as sq

from config_data import config


def get_info(string: str):
    """Фунция для получения данных из БД с запросом"""
    with sq.connect(config.db_file) as con:
        cur = con.cursor()
        cur.execute(string)
        return cur.fetchall()
