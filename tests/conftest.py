import pytest
from api.client_book import booking_base_client

@pytest.fixture(scope='session')
def create_booking():
    """Предварительное создание бронирования и получение id и ключа авторизации"""

    data = {
    "firstname": "Sally",
    "lastname": "Brown",
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2013-02-23",
        "checkout": "2014-10-23"
    },
    "additionalneeds": "Breakfast"
    }
    header = {'Content-Type': 'application/json'}

    create_booking = booking_base_client.create_booking(header, data)

    booking_id = create_booking.json()['bookingid']
    token = booking_base_client.post_api_key()

    return booking_id, token