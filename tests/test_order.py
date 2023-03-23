import allure
import pytest

from page_object.arenda_page import ArenfaForm
from page_object.oreder_page import OrderPage
from page_object.samokat_page import MainPage
from parametrize import results

class TestOrder:
    @allure.story("tests")
    @allure.feature("test_case")
    @allure.step("test order_form")
    # @pytest.mark.parametrize("name", names)
    # @pytest.mark.parametrize("second", second_name)
    # @pytest.mark.parametrize("str", street)
    @pytest.mark.parametrize("name, second, str", results)
    def test_order(self, browser,name, second, str):

        samokat_order = MainPage(browser)
        samokat_order.to_go()
        samokat_order.click_to_order_1()
        order_form = OrderPage(browser)
        order_form.input_elements(name, second, str)
        order_form.click_to_next()
        page_order_second = ArenfaForm(browser)
        page_order_second.from_element()
        page_order_second.form_oder_button()
        page_order_second.last_order_accept()
