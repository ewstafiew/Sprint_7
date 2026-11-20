import allure
import requests

from data import GET_ORDERS_URL
from helpers import REQUEST_TIMEOUT


@allure.feature('Список заказов')
class TestOrdersList:

    @allure.title('Запрос списка заказов возвращает 200 и список заказов')
    @allure.description('Отправляем запрос на получение списка заказов и проверяем '
                        'код ответа и наличие списка orders в теле ответа')
    def test_get_orders_list_returns_200_and_list_of_orders(self):
        response = requests.get(GET_ORDERS_URL, timeout=REQUEST_TIMEOUT)

        assert response.status_code == 200
        assert 'orders' in response.json()
        assert isinstance(response.json()['orders'], list)
