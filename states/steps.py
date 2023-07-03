from telebot.handler_backends import State, StatesGroup


class UserStates(StatesGroup):
    create_dict = State()
    choose_current_place = State()
    set_arrival_date = State()
    set_leave_date = State()
    get_quantity_hotels = State()
    quantity_hotels = State()
    ask_photos = State()
    get_photos = State()
    quantity_photos = State()
    price_min = State()
    price_max = State()
    distance = State()
