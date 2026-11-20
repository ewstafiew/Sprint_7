# Финальный проект 7 спринта: автотесты API учебного сервиса «Яндекс.Самокат»

## Технологии

- Python 3
- requests — отправка HTTP-запросов к API
- pytest — фреймворк для тестов (параметризация)
- Allure — отчёт о тестировании

## Структура проекта

- `tests/` — тесты, сгруппированные по ручкам:
  - `test_create_courier.py` — ручка «Создать курьера»;
  - `test_login_courier.py` — ручка «Логин курьера»;
  - `test_create_order.py` — ручка «Создать заказ»;
  - `test_orders_list.py` — ручка «Получить список заказов»;
- `helpers.py` — генерация тестовых данных и обёртки над запросами;
- `data.py` — URL ручек и тексты сообщений об ошибках;
- `conftest.py` — фикстуры: создание и удаление тестовых данных;
- `allure_results/` — результаты прогона для Allure-отчёта.

## Запуск тестов

```bash
pip install -r requirements.txt
pytest tests --alluredir=allure_results
```

## Просмотр Allure-отчёта

```bash
allure serve allure_results
```
