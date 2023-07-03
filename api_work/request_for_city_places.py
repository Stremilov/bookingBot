import json
import re

import requests
from loguru import logger

from config_data.config import headers


def request_for_city_places(city: str) -> list:
    """
    Функция для запроса к API и получения данных о городе.
    """
    url: str = 'https://hotels4.p.rapidapi.com/locations/v2/search'
    querystring: dict = {"query": city, "locale": "en_US", "currency": "USD"}
    try:
        response = requests.request('GET', url, headers=headers, params=querystring)

        pattern: str = r'(?<=CITY_GROUP",).+?[\]]'
        find = re.search(pattern, response.text)
        if find:
            suggestions = json.loads(f"{{{find[0]}}}")

        cities = list()
        for dest_id in suggestions['entities']:
            clear_destination = dest_id['name']
            cities.append({'city_name': clear_destination,
                                'destination_id': dest_id['geoId']})
        return cities
    except (TypeError, LookupError) as exc:
        logger.exception(exc)
