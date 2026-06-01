from helpers import generate_random_string

# Данные для создания курьера
def generate_courier_data():
    return {
        "login": generate_random_string(10),
        "password": generate_random_string(10),
        "firstname": generate_random_string(10)
    }

# Данные для создания курьера без пароля
def generate_courier_no_password():
    return {
        "login": generate_random_string(10),
        "firstname": generate_random_string(10)
    }

# Данные для создания курьера без логина
def generate_courier_no_login():
    return {
        "password": generate_random_string(10),
        "firstname": generate_random_string(10)
    }

# Данные для создания заказа c черным цветом
ORDER_DATA_BLACK_COLOR = {
    "firstName": "Алексей",
    "lastName": "Иванов",
    "address": "ул. Ленина, д. 25",
    "metroStation": 7,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2026-09-09",
    "comment": "Оставить у двери",
    "color": [
        "BLACK"
    ]
}

# Данные для создания заказа c серым цветом
ORDER_DATA_GREY_COLOR = {
    "firstName": "Алексей",
    "lastName": "Иванов",
    "address": "ул. Ленина, д. 25",
    "metroStation": 7,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2026-09-09",
    "comment": "Оставить у двери",
    "color": [
        "GREY"
    ]
}

# Данные для создания заказа c двумя цветами
ORDER_DATA_BOTH_COLOR = {
    "firstName": "Алексей",
    "lastName": "Иванов",
    "address": "ул. Ленина, д. 25",
    "metroStation": 7,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2026-09-09",
    "comment": "Оставить у двери",
    "color": [
        "GREY",
        "BLACK"
    ]
}

# Данные для создания заказа c без цвета
ORDER_DATA_WITHOUT_COLOR = {
    "firstName": "Алексей",
    "lastName": "Иванов",
    "address": "ул. Ленина, д. 25",
    "metroStation": 7,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2026-09-09",
    "comment": "Оставить у двери"
}

# Коды ответов

DUPLICATE_COURIER_RESPONSE = {
    "code": 409,
    "message": "Этот логин уже используется. Попробуйте другой."
}

CREATE_COURIER_RESPONSE = {"ok": True}

CREATE_COURIER_WITHOUT_REQUIRED_PARAMS = {
    "code": 400,
    "message": "Недостаточно данных для создания учетной записи"
}

LOGIN_WITHOUT_LOGIN_RESPONSE = {
    "code": 400,
    "message": "Недостаточно данных для входа"
}
NON_EXISTENT_COURIER = {
    "login": 'usernonexistent',
    "password": 'usernonexistent'
}

LOGIN_NON_EXISTENT_COURIER_RESPONSE = {
    "code": 404,
    "message": "Учетная запись не найдена"
}

ORDER_LIST_DETAILS = {
    "courierId": 750912,
    "nearestStation": 4,
    "limit": 5,
    "page": 0
    }

