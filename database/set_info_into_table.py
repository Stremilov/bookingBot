import sqlite3 as sq

from loguru import logger

from config_data import config


def set_info(string, values):
    """Функция для записи данных в БД"""
    with sq.connect(config.db_file) as con:
        cur = con.cursor()
        try:
            if values:
                cur.execute(string, values)
            else:
                cur.execute(string)
            return True
        except ProcessLookupError as exc:
            logger.exception(exc)