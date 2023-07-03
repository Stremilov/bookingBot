from database.get_info_from_table import get_info


def get_history(user_personal_id):
    """Фунцкия для получения данных из таблицы history"""
    history = get_info(string=
                       f'SELECT command_time, city, arrival_date, leave_date, price_per_period, command, hotel_name, hotel_adress, '
                       f'price_per_day, hotel_star_raiting FROM history where user_personal_id={user_personal_id}')
    return history
