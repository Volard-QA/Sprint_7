import requests
import allure

from curl import Url

class TestCreateCourier:
    @allure.title("Проверка успешного создания нового курьера")
    @allure.description("Создаем нового курьера с валидными данными полей Логин, Пароль, Имя в ручке POST /api/v1/courier, проверяем корректность кода и тела ответа")
    def test_create_new_courier(self, new_courier):
        response = new_courier
        response_data = response.json()
        expected_response = {
            'ok': True
        }
        assert response.status_code == 201 and response_data == expected_response

    @allure.title("Проверка невозможности создания курьера с одинаковыми логином, паролем")
    @allure.description("Создаем нового курьера с дублирующими данными полей Логин, Пароль в ручке POST /api/v1/courier, проверяем корректность кода и тела ответа об ошибке")
    def test_create_same_courier_twice(self, courier_methods, generate_courier_data):
        courier_info = generate_courier_data
        login = courier_info["login"]
        password = courier_info["password"]

        duplicate_courier_data = {
            "login": login,
            "password": password
        }
        duplicate_response = requests.post(f'{Url.BASE_URL}{Url.COURIER_URL}', json=duplicate_courier_data)
        duplicate_response_data = duplicate_response.json()['message']
        expected_response = 'Этот логин уже используется'
        assert duplicate_response.status_code == 409 and duplicate_response_data == expected_response

    @allure.title("Проверка невозможности создания курьера без одного из обязательных полей")
    @allure.description("Создаем нового курьера без указания логина в ручке POST /api/v1/courier, проверяем корректность кода и тела ответа об ошибке отсутствия данных обязательного поля")
    def test_create_courier_without_required_field(self):
        payload = {
            "login": "",
            "password": "somepassword",  # Укажите пароль
            "first_name": "Vlad"
        }
        response = requests.post(f'{Url.BASE_URL}{Url.COURIER_URL}', json=payload)
        response_data = response.json()['message']
        expected_response = 'Недостаточно данных для создания учетной записи'
        assert response.status_code == 400 and response_data == expected_response



