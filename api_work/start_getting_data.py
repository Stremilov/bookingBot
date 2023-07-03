from api_work.request_info_list import request_info_list
from api_work.request_photos import request_photo


def start(list_par: list) -> tuple:
    """
    Основная функция.
    """
    photos: list = []
    hotels: list = request_info_list(id=list_par[7], list_param=list_par)
    if hotels is not None:
         for hotel in hotels:
            if list_par[1] == '0':
                break
            request_p = request_photo(id_hotel=hotel[0])
            if request_p is not None:
                photos.extend(request_p)
         return hotels, photos
