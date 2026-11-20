import allure
import pytest

from data import (MESSAGE_ACCOUNT_NOT_FOUND,
                  MESSAGE_NOT_ENOUGH_DATA_FOR_LOGIN)
from helpers import login_courier


@allure.feature('Логин курьера')
class TestLoginCourier:

    @allure.title('Курьер может авторизоваться: запрос возвращает 200 и id курьера')
    @allure.description('Создаём курьера, авторизуемся с корректными логином и паролем '
                        'и проверяем код ответа и наличие id в теле ответа')
    def test_login_courier_with_valid_credentials_returns_200_and_id(self, courier):
        credentials = courier['data']
        response = login_courier(credentials['login'], credentials['password'])

        assert response.status_code == 200
        assert 'id' in response.json()

    @allure.title('При отсутствии обязательного поля «{missing_field}» возвращается 400 и ошибка')
    @allure.description('Отправляем запрос на авторизацию без одного из обязательных '
                        'полей и проверяем код ответа и сообщение об ошибке')
    @pytest.mark.parametrize('missing_field', ['login', 'password'])
    def test_login_courier_without_required_field_returns_400_and_error_message(
            self, courier, missing_field):
        credentials = courier['data'].copy()
        del credentials[missing_field]
        response = login_courier(credentials.get('login', ''), credentials.get('password', ''))

        assert response.status_code == 400
        assert response.json()['message'] == MESSAGE_NOT_ENOUGH_DATA_FOR_LOGIN

    @allure.title('При неверном пароле возвращается 404 и текст ошибки')
    @allure.description('Создаём курьера, авторизуемся с неверным паролем и проверяем '
                        'код ответа и сообщение об ошибке')
    def test_login_courier_with_wrong_password_returns_404_and_error_message(self, courier):
        credentials = courier['data']
        response = login_courier(credentials['login'], 'wrong_password')

        assert response.status_code == 404
        assert response.json()['message'] == MESSAGE_ACCOUNT_NOT_FOUND

    @allure.title('Авторизация под несуществующим пользователем возвращает 404 и ошибку')
    @allure.description('Авторизуемся с логином, которого нет в системе, и проверяем '
                        'код ответа и сообщение об ошибке')
    def test_login_courier_with_nonexistent_login_returns_404_and_error_message(self):
        response = login_courier('nonexistent_login_qa', 'some_password')

        assert response.status_code == 404
        assert response.json()['message'] == MESSAGE_ACCOUNT_NOT_FOUND
