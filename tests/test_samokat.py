import allure
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES

from page_object.arenda_page import ArenfaForm
from page_object.oreder_page import OrderPage
from page_object.samokat_page import MainPage
from locat import locs

class TestOpenTabs:
    @allure.story("tests")
    @allure.feature("test_case")
    # @allure.step("test Open Objects QBZ")
    # @pytest.mark.parametrize('num', [1, 2, 3, 4, 5, 6, 7, 8])
    # def test_open_case(self, browser, num):
    #     samokat = MainPage(browser)
    #     samokat.to_go()
    #     samokat.check_open_tab(num)
    #
    #
    #
    #
    # @pytest.mark.parametrize("nums", locs)
    # def test_check_tabs(self, browser, nums):
    #     samokat = MainPage(browser)
    #     samokat.to_go()
    #     samokat.check_open_wind(nums)


    def test_check_classic_method(self, browser):
        samokat = MainPage(browser)
        samokat.to_go()
        samokat.check_open_tabs_1()

    def test_check_classic_method_1(self, browser):
        samokat = MainPage(browser)
        samokat.to_go()
        samokat.check_open_tabs_2()

    def test_check_classic_method_2(self, browser):
        samokat = MainPage(browser)
        samokat.to_go()
        samokat.check_open_tabs_3()

    def test_check_classic_method_3(self, browser):
        samokat = MainPage(browser)
        samokat.to_go()
        samokat.check_open_tabs_4()

    def test_check_classic_method_4(self, browser):
        samokat = MainPage(browser)
        samokat.to_go()
        samokat.check_open_tabs_5()

    def test_check_classic_method_5(self, browser):
        samokat = MainPage(browser)
        samokat.to_go()
        samokat.check_open_tabs_6()

    def test_check_classic_method_7(self, browser):
        samokat = MainPage(browser)
        samokat.to_go()
        samokat.check_open_tabs_7()

    @pytest.mark.parametrize("num", [0, 1, 2, 3, 4, 5, 6, 7, 8])
    def test_for_damir(self, browser, num):
        samokat = MainPage(browser)
        samokat.to_go()
        samokat.remove_cookie()
        samokat.check_open_tables(num)





