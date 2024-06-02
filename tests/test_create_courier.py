import allure
import requests
import configuration
from helpers import register_new_courier
from helpers import register_new_courier_without_login
from helpers import register_new_courier_without_password


class TestCreateCourier:

    data = register_new_courier()

    @allure.title('Создание курьера')
    def test_create_courier(self):
        response = requests.post(
            f'{configuration.CREATE_COURIER_PATH}',
            TestCreateCourier.data)
        assert response.status_code == 201 and '{"ok":true}' == response.text

    @allure.title('Нельзя создать двух одинаковых курьеров с одинаковыми логинами')
    def test_courier_was_created(self):
        response = requests.post(
            f'{configuration.CREATE_COURIER_PATH}',
            TestCreateCourier.data)
        assert response.status_code == 409 and 'Этот логин уже используется' in response.text

    @allure.title('Нельзя создать курьера без логина')
    def test_create_courier_without_login(self):
        response = requests.post(
            f'{configuration.CREATE_COURIER_PATH}',
            register_new_courier_without_login())
        assert response.status_code == 400 and 'Недостаточно данных для создания учетной записи' in response.text

    @allure.title('Нельзя создать курьера без пароля')
    def test_create_courier_without_password(self):
        response = requests.post(
            f'{configuration.CREATE_COURIER_PATH}',
            register_new_courier_without_password())
        assert response.status_code == 400 and 'Недостаточно данных для создания учетной записи' in response.text
