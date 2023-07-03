from database.set_info_into_table import set_info


def set_photo(photo_info):
    return set_info(string=f'INSERT INTO photo(hotel_id, photo_url) VALUES(?, ?)', values=photo_info)