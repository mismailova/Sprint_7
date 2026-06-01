import allure
import data
from methods.courier_methods import CourierMethods

class TestLoginCourier:

    @allure.title('Успешная авторизация курьера')
    @allure.description('При авторизации курьера возвращается код 200 ОК и id')

    def test_login_courier_success(self, courier):
        _, courier_data, courier_id = courier
        login_data = {
            "login": courier_data['login'],
            "password": courier_data['password']
        }
        response = CourierMethods().login_courier(login_data)

        assert response.status_code == 200 and response.json()['id'] == courier_id, (
            f"Ожидался статус 200 и id {courier_id}, "
            f"получено: статус {response.status_code}, тело {response.json()}"
        )

    @allure.title('Ошибка при отсутствии логина в теле')
    @allure.description('При авторизации курьера без логина ошибка 400 и текст ошибки')

    def test_login_courier_without_login_error(self, courier):
        _, courier_data, _ = courier
        login_data = {
            "password": courier_data['password']
        }
        response = CourierMethods().login_courier(login_data)

        assert response.status_code == 400 and response.json() == data.LOGIN_WITHOUT_LOGIN_RESPONSE, (
            f"Ожидался статус 400 и тело {data.LOGIN_WITHOUT_LOGIN_RESPONSE}, "
            f"получено: статус {response.status_code}, тело {response.json()}"
        )

    @allure.title('Ошибка при отсутствии пароля в теле')
    @allure.description('При авторизации курьера без пароля ошибка 504')

    def test_login_courier_without_password_error(self, courier):
        _, courier_data, _ = courier
        login_data = {
            "login": courier_data['login']
        }
        response = CourierMethods().login_courier(login_data)

        assert response.status_code == 504, (
            f"Ожидался статус 504"
            f"получено: статус {response.status_code}"
        )

    @allure.title('Ошибка при авторизации несуществующим курьером')
    @allure.description('При авторизации несуществующим курьером ошибка 404 и тест ошибки')

    def test_login_non_existent_courier_error(self):
        courier = CourierMethods()
        response = courier.login_courier(data.NON_EXISTENT_COURIER)

        assert response.status_code == 404 and response.json() == data.LOGIN_NON_EXISTENT_COURIER_RESPONSE, (
            f"Ожидался статус 400 и тело {data.LOGIN_NON_EXISTENT_COURIER_RESPONSE}, "
            f"получено: статус {response.status_code}, тело {response.json()}"
        )
