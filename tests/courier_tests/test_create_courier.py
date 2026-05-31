import allure
import pytest
import data
from methods.courier_methods import CourierMethods


class TestCreateCourier:

    @allure.title('Успешное создание курьера')
    @allure.description('Создается новый курьер при отправке валидного тела запроса')

    def test_create_courier_success(self, courier):
        response, _, _ = courier

        assert response.status_code == 201 and response.json() == data.CREATE_COURIER_RESPONSE, (
            f"Ожидался статус 201 и тело {data.CREATE_COURIER_RESPONSE}, "
            f"получено: статус {response.status_code}, тело {response.json()}"
    )

    @allure.title('Ошибка при создании курьера с существующими данными')
    @allure.description('При создании курьера с существующими данными код 409 и текст ошибки')

    def test_duplicate_create_courier_error(self, courier):
        _, courier_data, _ = courier
        response = CourierMethods().create_courier(courier_data)

        assert response.status_code == 409 and response.json() == data.DUPLICATE_COURIER_RESPONSE, (
            f"Ожидался статус 409 и тело {data.DUPLICATE_COURIER_RESPONSE}, "
            f"получено: статус {response.status_code}, тело {response.json()}"
        )

    @allure.title('Ошибка при отсутствии логина/пароля в теле')
    @allure.description('При создании курьера без логина/пароля ошибка 400 и текст ошибки')
    @pytest.mark.parametrize('courier_data',[data.generate_courier_no_login(), data.generate_courier_no_password()])

    def test_create_courier_without_required_params(self, courier_data):
        courier = CourierMethods()
        response = courier.create_courier(courier_data)

        assert response.status_code == 400 and response.json() == data.CREATE_COURIER_WITHOUT_REQUIRED_PARAMS, (
            f"Ожидался статус 400 и тело {data.CREATE_COURIER_WITHOUT_REQUIRED_PARAMS}, "
            f"получено: статус {response.status_code}, тело {response.json()}"
        )
