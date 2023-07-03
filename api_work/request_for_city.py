import json

from loguru import logger

from api_work.get_requests_to_api import get_requests
from config_data import config


def request_for_place(gaiaId: str) -> str:
    """
    Функция для запроса к API и получения данных о городе.
    """
    url: str = "https://hotels4.p.rapidapi.com/properties/v2/list"
    payload = {
        "currency": "USD",
        "eapid": 1,
        "locale": "en_US",
        "siteId": 300000001,
        "destination": {"regionId": gaiaId},
        "checkInDate": {
            "day": 1,
            "month": 1,
            "year": 2023
        },
        "checkOutDate": {
            "day": 1,
            "month": 1,
            "year": 2024
        },
        "rooms": [
            {
                "adults": 1
            }
        ],
        "resultsStartingIndex": 0,
        "resultsSize": 200,
        "sort": "PRICE_LOW_TO_HIGH",
        "filters": {"price": {
            "max": 1000,
            "min": 100
        }}
    }
    try:
        request = get_requests(url=url, headers=config.headers, payload=payload)
        data = json.loads(request.text)
        return data
    except LookupError as exc:
        logger.exception(exc)
