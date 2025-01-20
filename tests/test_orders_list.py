import allure
import requests

from curl import Url


class TestOrdersList:
    @allure.title("Проверка успешного успешного возврата списка доступных заказов в ручке GET /api/v1/orders")
    @allure.description("Делаем запрос списка заказов в ручке GET /api/v1/orders, проверяем корректность кода и тела ответа со списком заказов")
    def test_list_of_orders_body(self):
        params = {
            "limit": 10,
            "page": 0
        }
        response = requests.get(f'{Url.BASE_URL}{Url.ORDERS_URL}', params = params)
        response_data = response.json()
        assert response.status_code == 200 and "orders" in response_data and isinstance(response_data["orders"], list) and len(response_data["orders"]) > 0