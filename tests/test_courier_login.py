import requests
import allure

from curl import Url

class TestLoginCourier:
    @allure.title("Проверка успешной авторизации курьера с корректными логином и паролем")
    @allure.description("Создаем нового курьера и производим его авторизацию в ручке POST /api/v1/courier/login, проверяем корректность кода и тела ответа об успешной авторизации")
    def test_successful_login(self, courier_methods, generate_courier_data):
        courier_data = generate_courier_data
        login_payload = {
            "login": courier_data["login"],
            "password": courier_data["password"]
        }
        response = requests.post(f'{Url.BASE_URL}{Url.COURIER_URL}{Url.COURIER_LOGIN_URL}', json=login_payload)
        response_data = response.json()
        assert response.status_code == 200 and response_data["id"] == courier_data["id"]

    @allure.title("Проверка невозможности авторизации курьера при отсутствии данных в одном из обязательных полей")
    @allure.description("Создаем нового курьера и производим его авторизацию в ручке POST /api/v1/courier/login без указания пароля, проверяем корректность кода и тела ответа об ошибке авторизации без логина или пароля")
    def test_login_without_required_field(self, courier_methods, generate_courier_data):
        courier_data = generate_courier_data
        login_payload = {
            "login": courier_data["login"],
            "password": ''
        }
        response = requests.post(f'{Url.BASE_URL}{Url.COURIER_URL}{Url.COURIER_LOGIN_URL}', json=login_payload)
        response_data = response.json()['message']
        expected_response = 'Недостаточно данных для входа'
        assert response.status_code == 400 and response_data == expected_response

    @allure.title("Проверка невозможности авторизации курьера с логином, несуществующим в БД")
    @allure.description("Создаем нового курьера и производим его авторизацию в ручке POST /api/v1/courier/login с указанием логина, отсутствующего в БД, проверяем корректность кода и тела ответа об ошибке авторизации с несуществующей парой логин-пароль")
    def test_login_with_unexisted_login(self, courier_methods, generate_courier_data):
        courier_data = generate_courier_data
        login_payload = {
            "login": "nonexistent_login",
            "password": courier_data["password"]
        }
        response = requests.post(f'{Url.BASE_URL}{Url.COURIER_URL}{Url.COURIER_LOGIN_URL}', json=login_payload)
        response_data = response.json()['message']
        expected_response = 'Учетная запись не найдена'
        assert response.status_code == 404 and response_data == expected_response
