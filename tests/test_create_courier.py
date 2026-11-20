import allure
import pytest

from data import (MESSAGE_LOGIN_ALREADY_USED,
                  MESSAGE_NOT_ENOUGH_DATA_FOR_CREATE)
from helpers import create_courier


@allure.feature('Создание курьера')
class TestCreateCourier:

    @allure.title('Курьера можно создать: код 201 и тело ответа ok: true')
    @allure.description('Создаём курьера со всеми обязательными полями и проверяем '
                        'код ответа и тело ответа')
    def test_create_courier_with_all_required_fields_returns_201_and_ok_true(self, courier):
        response = courier['create_response']

        assert response.status_code == 201
        assert response.json() == {'ok': True}

    @allure.title('Нельзя создать двух курьеров с одинаковым логином: 409 и текст ошибки')
    @allure.description('Создаём курьера, затем повторно отправляем запрос с тем же '
                        'логином и проверяем код ответа и сообщение об ошибке')
    def test_create_courier_with_existing_login_returns_409_and_error_message(self, courier):
        response = create_courier(courier['data'])

        assert response.status_code == 409
        assert response.json()['message'] == MESSAGE_LOGIN_ALREADY_USED

    @allure.title('При отсутствии обязательного поля «{missing_field}» возвращается 400 и ошибка')
    @allure.description('Отправляем запрос на создание курьера без одного из обязательных '
                        'полей login или password и проверяем код ответа '
                        'и сообщение об ошибке')
    @pytest.mark.parametrize('missing_field', ['login', 'password'])
    def test_create_courier_without_required_field_returns_400_and_error_message(
            self, courier_credentials, missing_field):
        courier_data = courier_credentials.copy()
        del courier_data[missing_field]
        response = create_courier(courier_data)

        assert response.status_code == 400
        assert response.json()['message'] == MESSAGE_NOT_ENOUGH_DATA_FOR_CREATE

    @allure.title('Поле firstName необязательно: без него курьер создаётся с кодом 201')
    @allure.description('Проверено вручную: сервис не требует поле firstName для '
                        'создания курьера, поэтому без него запрос успешен')
    def test_create_courier_without_first_name_returns_201(self, courier_credentials):
        courier_data = courier_credentials.copy()
        del courier_data['firstName']
        response = create_courier(courier_data)

        assert response.status_code == 201
        assert response.json() == {'ok': True}
