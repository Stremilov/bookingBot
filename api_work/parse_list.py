from loguru import logger


def parse_list(parse_list: list) -> list:
    """
    Фунцкия для подготовки данных к записи в базу данных.
    """
    hotels = []
    hotel_id, name, star_rating, hotel_address, distance, price_per_day = '', 'нет данных', '', '', '', ''
    for hotel in parse_list:
        try:
            hotel_id = hotel['id']
            name = hotel['name']
            star_rating = hotel['star']
            if star_rating == None:
                star_rating = 0
            hotel_distance = hotel["destinationInfo"]["distanceFromDestination"]["value"]
            if hotel_distance == None:
                hotel_distance = "In the center of city"
            price_per_day = (hotel['price']['lead']['formatted']).lstrip("$")
            hotels.append((hotel_id, name, star_rating, hotel_address, hotel_distance, price_per_day))
        except (TypeError, LookupError) as exc:
            logger.exception(exc)
            continue
    return hotels
