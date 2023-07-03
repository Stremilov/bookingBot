import json

from loguru import logger

from api_work.get_requests_to_api import get_requests
from config_data import config
from database.set_photo_into_table import set_photo


def request_photo(id_hotel: str) -> list:
    """
    Функция для запроса к API и получения данных о фотографиях.
    """

    url = "https://hotels4.p.rapidapi.com/properties/v2/detail"
    payload = {
    "currency": "USD",
    "eapid": 1,
    "locale": "en_US",
    "siteId": 300000001,
    "propertyId": id_hotel
    }
    photos = []
    try:
        response = get_requests(url, headers=config.headers, payload=payload)
        data = json.loads(response.text)
        for photo in data['data']['propertyInfo']['propertyGallery']['images']:
            #url = photo['baseUrl'].replace('_{size}', '_z')
            url = photo['image']['url']
            photos.append((id_hotel, url))
            photo_info = id_hotel, url
            set_photo(photo_info)
        return photos
    except TypeError as exc:
        logger.exception(exc)
