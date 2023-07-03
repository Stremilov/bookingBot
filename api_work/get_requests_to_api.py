import requests
from loguru import logger


def get_requests(url: str, headers: str, payload: dict) -> callable:
    """
    Функция для выполнения запроса.
    """
    try:
        response = requests.post(url=url, headers=headers, json=payload, timeout=20)
        if response.status_code == requests.codes.ok:
            return response
    except LookupError as exc:
        logger.exception(exc)
