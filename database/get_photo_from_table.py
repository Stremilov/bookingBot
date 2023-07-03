from database.get_info_from_table import get_info


def get_photo(hotel_id, limit):
    photos = get_info(string=f'SELECT photo_url from photo WHERE hotel_id == {hotel_id} LIMIT {limit}')
    return photos