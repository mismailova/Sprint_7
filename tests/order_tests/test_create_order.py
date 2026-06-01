import allure
import pytest
import data
from methods.order_methods import OrderMethods


class TestCreateOrder:

    @allure.title('Успешное создание заказа с разными вариантами выбора цветов')
    @allure.description('Создается новый заказ - в теле возвращается track')
    @pytest.mark.parametrize('order_data', [
        data.ORDER_DATA_BLACK_COLOR,
        data.ORDER_DATA_GREY_COLOR,
        data.ORDER_DATA_BOTH_COLOR,
        data.ORDER_DATA_WITHOUT_COLOR
    ])

    def test_create_order(self, order_data):
        order = OrderMethods()
        response = order.create_order(order_data)

        assert response.status_code == 201 and 'track' in response.json(), (
            f"Ожидался статус 201 и track в теле ответа, "
            f"получено: статус {response.status_code}, тело {response.json()}"
        )
