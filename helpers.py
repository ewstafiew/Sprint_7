import random
import string

import allure
import requests

from data import (CREATE_COURIER_URL, CREATE_ORDER_URL, DELETE_COURIER_URL,
                  LOGIN_COURIER_URL)

REQUEST_TIMEOUT = 60


@allure.step('Генерируем случайную строку из {length} букв нижнего регистра')
def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


@allure.step('Генерируем данные нового курьера')
def generate_courier_data():
    return {
        'login': generate_random_string(10),
        'password': generate_random_string(10),
        'firstName': generate_random_string(10),
    }


@allure.step('Отправляем запрос на создание курьера')
def create_courier(courier_data):
    return requests.post(CREATE_COURIER_URL, json=courier_data, timeout=REQUEST_TIMEOUT)


@allure.step('Отправляем запрос на авторизацию курьера')
def login_courier(login, password):
    return requests.post(
        LOGIN_COURIER_URL, json={'login': login, 'password': password},
        timeout=REQUEST_TIMEOUT)


@allure.step('Удаляем курьера с id {courier_id}')
def delete_courier(courier_id):
    return requests.delete(f'{DELETE_COURIER_URL}/{courier_id}', timeout=REQUEST_TIMEOUT)


@allure.step('Генерируем данные нового заказа')
def generate_order_data(color=None):
    order_data = {
        'firstName': 'Тест',
        'lastName': 'Тестов',
        'address': 'Москва, Тестовая улица, 1',
        'metroStation': '4',
        'phone': '+79001112233',
        'rentTime': 2,
        'deliveryDate': '2026-12-01',
        'comment': 'Тестовый заказ',
    }
    if color is not None:
        order_data['color'] = color
    return order_data


@allure.step('Отправляем запрос на создание заказа')
def create_order(order_data):
    return requests.post(CREATE_ORDER_URL, json=order_data, timeout=REQUEST_TIMEOUT)
