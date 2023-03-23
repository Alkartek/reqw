import allure
import pytest
from parametrize import results

from page_object.arenda_page import ArenfaForm
from page_object.oreder_page import OrderPage
from page_object.samokat_page import MainPage

class TestOrder:
    @allure.story("tests")
    @allure.feature("test_case")
    @allure.step("test order_form_2")
    @pytest.mark.parametrize('names, second_name, street', results)
    def test_order_second(self, browser, names, second_name, street):

        samokat_order = MainPage(browser)
        samokat_order.to_go()
        samokat_order.click_to_order_1()
        order_form = OrderPage(browser)
        order_form.input_elements(names, second_name, street)
        order_form.click_to_next()
        page_order_second = ArenfaForm(browser)
        page_order_second.from_element()
        page_order_second.form_oder_button()
        page_order_second.last_order_accept()







