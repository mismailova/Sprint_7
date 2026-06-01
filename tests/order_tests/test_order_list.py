import allure
import data
from methods.order_methods import OrderMethods


class TestOrderList:

    @allure.title('Получение списка заказов с параметрами')
    @allure.description('Проверяет наличие в списке заказа курьера')

    def test_get_order_list_by_params(self):
        order_list = OrderMethods()
        response = order_list.get_order_list_by_params(data.ORDER_LIST_DETAILS)
        response_body = response.json()
        orders = response_body['orders']

        assert (response.status_code == 200 and any(
            order['courierId'] == data.ORDER_LIST_DETAILS['courierId'] for order in orders
        )), (
            f"Ожидался статус 200 и заказ с courierId {data.ORDER_LIST_DETAILS['courierId']}, "
            f"получено: статус {response.status_code}, тело {response_body}"
        )

    @allure.title('Получение списка заказов без параметров')
    @allure.description('Проверяет, что список возвращает массив с заказами')

    def test_get_order_list_without_params(self):
        order_list = OrderMethods()
        response = order_list.get_order_list_by_params()
        response_body = response.json()
        orders = response_body['orders']

        assert response.status_code == 200 and len(orders) >= 1, (
            f"Ожидался статус 200 и не пустой список заказов, "
            f"получено: статус {response.status_code}, количество заказов: {len(orders)}"
        )
