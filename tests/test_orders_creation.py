import allure
import pytest
import requests

import data
from curl import Url


class TestOrderCreation:

    @allure.title("Проверка успешного создания заказа с валидными данными в обязательных полях")
    @allure.description("Создаем заказы с валидными наборами данных в полях заказа в ручке POST /api/v1/orders проверяем корректность кода и тела ответа об успешном создании заказа")
    @pytest.mark.parametrize(
        "first_name, last_name, address, metro_station, phone, rent_time, delivery_date, comment, color", data.OrdersInList.orders_in_list)
    def test_successful_orders_creation(self, first_name, last_name, address, metro_station, phone, rent_time, delivery_date, comment, color):
        order_body = {
            "firstName": first_name,
            "lastName": last_name,
            "address": address,
            "metroStation": metro_station,
            "phone": phone,
            "rentTime": rent_time,
            "deliveryDate": delivery_date,
            "comment": comment,
            "color": color
        }
        response = requests.post(f'{Url.BASE_URL}{Url.ORDERS_URL}', json=order_body)
        expected_response = response.json()
        assert response.status_code == 201 and "track" in expected_response
