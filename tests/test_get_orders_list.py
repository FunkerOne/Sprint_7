import allure
import requests
import configuration


class TestGetListOrders:
    @allure.title('В тело ответа возвращается список заказов')
    def test_list_order(self):
        response = requests.get(f'{configuration.GET_ORDERS_LIST_PATH}')
        assert response.status_code == 200 and "orders" in response.json()
