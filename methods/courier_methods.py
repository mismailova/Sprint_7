import allure
import requests
import urls

class CourierMethods:

    @allure.step('Создать курьера')
    def create_courier(self, courier_data):
        response = requests.post(urls.BASE_URL + urls.COURIER_URL, json=courier_data)
        return response

    @allure.step('Авторизоваться за курьера в системе')
    def login_courier(self, login_data):
        response = requests.post(urls.BASE_URL + urls.COURIER_URL + 'login', json=login_data)
        return response

    @allure.step('Удалить курьера')
    def delete_courier(self, courier_id):
        response = requests.delete(f'{urls.BASE_URL}{urls.COURIER_URL}/{courier_id}')
        return response
