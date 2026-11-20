import allure
import pytest

from helpers import create_order, generate_order_data


@allure.feature('Создание заказа')
class TestCreateOrder:

    @allure.title('Заказ можно создать с цветом {color}: запрос возвращает 201 и track')
    @allure.description('Создаём заказ с разными вариантами цвета самоката: один цвет, '
                        'оба цвета или без цвета, и проверяем код ответа и наличие '
                        'номера заказа track в теле ответа')
    @pytest.mark.parametrize('color', [
        pytest.param(['BLACK'], id='цвет BLACK'),
        pytest.param(['GREY'], id='цвет GREY'),
        pytest.param(['BLACK', 'GREY'], id='оба цвета'),
        pytest.param(None, id='без цвета'),
    ])
    def test_create_order_with_colors_returns_201_and_track(self, color):
        order_data = generate_order_data(color)
        response = create_order(order_data)

        assert response.status_code == 201
        assert 'track' in response.json()
