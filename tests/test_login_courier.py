import allure
import requests
import pytest
import configuration
from data import Couriers


class TestLoginCourier:
    @allure.title('Успешная авторизация существующего курьера')
    def test_courier_log_in(self):
        response = requests.post(
            f'{configuration.LOGIN_COURIER_PATH}',
            data=Couriers.data_exist)
        assert response.status_code == 200 and 'id' in response.text

    @allure.title('Ошибка при авторизации если курьер не зарегистрирован')
    def test_courier_log_negative(self):
        response = requests.post(
            f'{configuration.LOGIN_COURIER_PATH}',
            data=Couriers.data_non_exist)
        assert response.status_code == 404 and 'Учетная запись не найдена' in response.text

    @allure.title('Ошибка при авторизации если не заполнить поле логин или пароль')
    @pytest.mark.parametrize('data_without_login_or_password', [Couriers.data_without_login, Couriers.data_without_password])
    def test_courier_log_not_all_data(self, data_without_login_or_password):
        response = requests.post(
            f'{configuration.LOGIN_COURIER_PATH}',
            data=data_without_login_or_password)
        assert response.status_code == 400 and 'Недостаточно данных для входа' in response.text
