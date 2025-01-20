import requests
from curl import Url

class CourierMethods:
    @staticmethod
    def create_courier(courier_data):
        return requests.post(f'{Url.BASE_URL}{Url.COURIER_URL}', json=courier_data)

    @staticmethod
    def delete_courier(courier_id):
        return requests.delete(f'{Url.BASE_URL}{Url.COURIER_URL}/{courier_id}')
