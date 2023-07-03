from database.set_info_into_table import set_info


def set_history(history):
    """Функция для записи данных в таблицу history"""
    return set_info(string=
                    f'INSERT INTO history(user_personal_id, command_time, city, arrival_date, leave_date,'
                    f' price_per_period, command, hotel_name, hotel_adress, price_per_day, hotel_star_raiting)'
                    f' VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                    values=history)
