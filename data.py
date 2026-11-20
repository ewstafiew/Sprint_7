# URL учебного сервиса «Яндекс.Самокат» и ручек API
BASE_URL = 'https://qa-scooter.education-services.ru'
CREATE_COURIER_URL = f'{BASE_URL}/api/v1/courier'
LOGIN_COURIER_URL = f'{BASE_URL}/api/v1/courier/login'
DELETE_COURIER_URL = f'{BASE_URL}/api/v1/courier'
CREATE_ORDER_URL = f'{BASE_URL}/api/v1/orders'
GET_ORDERS_URL = f'{BASE_URL}/api/v1/orders'
CANCEL_ORDER_URL = f'{BASE_URL}/api/v1/orders/cancel'

# Ожидаемые тексты сообщений об ошибках
MESSAGE_NOT_ENOUGH_DATA_FOR_CREATE = 'Недостаточно данных для создания учетной записи'
MESSAGE_LOGIN_ALREADY_USED = 'Этот логин уже используется. Попробуйте другой.'
MESSAGE_NOT_ENOUGH_DATA_FOR_LOGIN = 'Недостаточно данных для входа'
MESSAGE_ACCOUNT_NOT_FOUND = 'Учетная запись не найдена'
