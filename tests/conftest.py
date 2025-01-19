import pytest
import requests

from curl import Url
from generators import register_new_courier_and_return_login_password
from methods.courier_methods import CourierMethods


@pytest.fixture(scope='function')
def courier_methods():
    return CourierMethods()

@pytest.fixture(scope='function')
def generate_courier_data():
    login_pass = register_new_courier_and_return_login_password()
    login, password, first_name = login_pass
    login_payload = {
        "login": login,
        "password": password
    }
    response = requests.post(f'{Url.BASE_URL}{Url.COURIER_URL}{Url.COURIER_LOGIN_URL}',json=login_payload)
    courier_id = response.json().get("id")
    yield {
        "id": courier_id,
        "login": login,
        "password": password
    }
    requests.delete(f'{Url.BASE_URL}{Url.COURIER_URL}{courier_id}')
