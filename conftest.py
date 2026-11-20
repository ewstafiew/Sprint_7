import allure
import pytest

from helpers import (create_courier, delete_courier, generate_courier_data,
                     login_courier)


@pytest.fixture
def courier_credentials():
    """Генерирует уникальные данные курьера.
    После теста удаляет курьера, если он был создан."""
    credentials = generate_courier_data()
    yield credentials

    # удаляем курьера, если он был создан в тесте
    with allure.step('Удаляем тестового курьера после теста'):
        response = login_courier(credentials['login'], credentials['password'])
        if response.status_code == 200:
            delete_courier(response.json()['id'])


@pytest.fixture
def courier(courier_credentials):
    """Создаёт курьера перед тестом, после теста удаляет его.
    Возвращает словарь с данными курьера и ответом на запрос создания."""
    create_response = create_courier(courier_credentials)
    yield {'data': courier_credentials, 'create_response': create_response}
