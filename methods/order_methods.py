import allure
import requests
import urls

class OrderMethods:

    @allure.step('Создать заказ')
    def create_order(self, order_data):
        response = requests.post(urls.BASE_URL + urls.ORDER_URL, json=order_data)
        return response

    @allure.step('Получить список заказов по параметрам')
    def get_order_list_by_params(self, params=None):
        response = requests.get(urls.BASE_URL + urls.ORDER_URL, params=params)
        return response

    @allure.step('Получить список заказов без параметров')
    def get_order_list_without_params(self):
        response = requests.get(urls.BASE_URL + urls.ORDER_URL)
        return response
