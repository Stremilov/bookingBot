import json

from loguru import logger

from api_work.get_requests_to_api import get_requests
from api_work.parse_list import parse_list
from config_data import config


def request_info_list(id: str, list_param: list) -> list:
    """
    Функция для запроса к API и получения основных данных.
    """
    url: str = "https://hotels4.p.rapidapi.com/properties/v2/list"
    sort_order: str = ''
    arrival_date = list_param[8].split('.')
    if int(arrival_date[0]) < 10:
        arrival_date[0] = arrival_date[0].lstrip("0")
    leave_date = list_param[9].split('.')
    if int(leave_date[0]) < 10:
        leave_date[0] = leave_date[0].lstrip("0")
    distance: str = list_param[6]
    price_min: str = list_param[4]
    price_max: str = list_param[5]
    page_size: str = list_param[2]
    if list_param[3] == 'lowprice':
        sort_order: str = 'PRICE_LOW_TO_HIGH'
    elif list_param[3] == 'highprice':
        sort_order: str = 'PRICE_HIGH_TO_LOW'
    elif list_param[3] == 'bestdeal':
        sort_order: str = 'DISTANCE_FROM_LANDMARK'
        price_min: str = list_param[4]
        price_max: str = list_param[5]

    payload = {
        "currency": "USD",
        "eapid": 1,
        "locale": "en_US",
        "siteId": 300000001,
        "destination": {"regionId": id},
        "checkInDate": {"day": int(arrival_date[0]), "month": int(arrival_date[1]), "year": int(arrival_date[2])},
        "checkOutDate": {"day": 15, "month": 10, "year": 2023},
        "rooms": [{"adults": 1}],
        "resultsStartingIndex": 0,
        "resultsSize": int(page_size),
        "sort": sort_order,
        "filters": {"price": {
            "max": 1000,
            "min": 100
        }}
    }
    try:
        request = get_requests(url=url, headers=config.headers, payload=payload)
        data = json.loads(request.text)
        parsed_info: list = parse_list(parse_list=data['data']['propertySearch']['properties'])
        return parsed_info
    except (LookupError, TypeError) as exc:
        logger.exception(exc)
