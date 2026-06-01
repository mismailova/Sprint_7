import pytest
from data import generate_courier_data
from methods.courier_methods import CourierMethods

@pytest.fixture()
def courier():
    courier_data = generate_courier_data()
    response = CourierMethods().create_courier(courier_data)
    login_response = CourierMethods().login_courier({
        "login": courier_data['login'],
        "password": courier_data['password']
    })
    courier_id = login_response.json()['id']
    yield response, courier_data, courier_id
    CourierMethods().delete_courier(courier_id)

@pytest.fixture()
def delete_courier():
    created_courier_data = []
    yield created_courier_data
    for courier_data in created_courier_data:
        login_response = CourierMethods().login_courier({
            "login": courier_data["login"],
            "password": courier_data["password"]
        })
        courier_id = login_response.json()["id"]
        CourierMethods().delete_courier(courier_id)
