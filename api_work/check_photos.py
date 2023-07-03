import requests
from loguru import logger


def check_photos(photo: str):
    """
    Функция для проверки url фото.
    """
    try:
        check_photos = requests.get(url=photo, timeout=20)
        if check_photos.status_code == 200:
            return True
    except (TypeError, LookupError) as exc:
        logger.exception(exc)
