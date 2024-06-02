import allure
import requests
import pytest
import json
import configuration
from data import Order


class TestCreateOrder:
    @allure.title('Создание заказа')
    @pytest.mark.parametrize('order_data', [{"color": ["BLACK"]}, {"color": ["GREY"]}, {"color": ["BLACK", "GREY"]}, {"color": [""]}])
    def test_create_order(self, order_data):
        Order.data_order.update(order_data)
        order_data = json.dumps(Order.data_order)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(f'{configuration.CREATE_ORDER_PATH}', data=order_data, headers=headers)
        assert response.status_code == 201 and 'track' in response.text
