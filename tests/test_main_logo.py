import allure

import conftest
from page_object.arenda_page import ArenfaForm
from page_object.oreder_page import OrderPage
from page_object.samokat_page import MainPage


class TestMainLogo:
    @allure.story("tests")
    @allure.feature("test_case")
    @allure.step("test_to_go_in_logo")
    def test_main_logo(self, browser):

        samokat_page = MainPage(browser)
        samokat_page.to_go()
        samokat_page.click_to_order_1()
        samokat_page.click_to_samokat_logo()
        samokat_page.click_to_ya_page()








