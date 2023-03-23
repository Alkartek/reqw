import pytest
from selenium.webdriver.common.by import By

from base_page import BasePage

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES


class MainLocator:

    LOCATOR_Q_1 = (By.XPATH, '//[@id="accordion__heading-0"]')
    LOCATOR_Q = (By.XPATH, '//[@id="accordion__heading-{}"]')
    LOCATOR_Q_2 = (By.XPATH, '//*[@id="accordion__heading-1"]')
    LOCATOR_Q_3 = (By.XPATH, '//*[@id="accordion__heading-2"]')
    LOCATOR_Q_4 = (By.XPATH, '//*[@id="accordion__heading-3"]')
    LOCATOR_Q_5 = (By.XPATH, '//*[@id="accordion__heading-4"]')
    LOCATOR_Q_6 = (By.XPATH, '//*[@id="accordion__heading-5"]')
    LOCATOR_Q_7 = (By.XPATH, '//*[@id="accordion__heading-6"]')
    LOCATOR_Q_8 = (By.XPATH, '//*[@id="accordion__heading-7"]')
    LOCATOR_ORDER_1 = (By.XPATH, '//button[@class="Button_Button__ra12g"]')
    LOCATOR_ORDER_2 = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')
    LOCATOR_SAMOKAT_LOGO = (By.XPATH, '//a[@class="Header_LogoScooter__3lsAR"]')
    LOCATOR_YA_PAGE = (By.XPATH, '//a[@class="Header_LogoYandex__3TSOI"]')
    LOCATOR_FIEND_YA = (By.XPATH, '//button[@type="submit"]')
    LOCATOR_SAMOKAT_PAGE = (By.XPATH, '//div[@class="Home_Header__iJKdX"]')
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    QWES = (By.XPATH, "//*[text()='Вопросы о важном']")


class MainPage(BasePage):

    def check_open_tables(self, num):

        element = self.find_element(MainLocator.QWES)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        method, path = MainLocator.LOCATOR_Q
        path = path.format(num)
        search_element = self.driver.find_element(method, path)
        search_element.click()
    def check_open_wind(self, nums):
        element = self.find_element(MainLocator.LOCATOR_Q_1)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        search_element = self.find_element(nums)
        search_element.click()


    #Открытие всех ответов на вопросы
    XP = By.XPATH
    def check_open_tab(self, num):
        element = self.find_element(MainLocator.LOCATOR_Q_1)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        path = MainLocator.LOCATOR_Q
        path = path.format(num)
        seach_element = self.find_element(MainPage.XP, path)
        seach_element.click()
    def check_open_tabs_1(self):
        element = self.find_element(MainLocator.LOCATOR_Q_1)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        seach_element = self.find_element(MainLocator.LOCATOR_Q_1)
        seach_element.click()

    def check_open_tabs_2(self):
        element = self.find_element(MainLocator.LOCATOR_Q_1)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

        seach_element_1 = self.find_element(MainLocator.LOCATOR_Q_2)
        seach_element_1.click()

    def check_open_tabs_3(self):
        element = self.find_element(MainLocator.LOCATOR_Q_2)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        seach_element_2 = self.find_element(MainLocator.LOCATOR_Q_3)
        seach_element_2.click()

    def check_open_tabs_4(self):
        element = self.find_element(MainLocator.LOCATOR_Q_3)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        seach_element_3 = self.find_element(MainLocator.LOCATOR_Q_4)
        seach_element_3.click()

    def check_open_tabs_5(self):
        element = self.find_element(MainLocator.LOCATOR_Q_4)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        seach_element_4 = self.find_element(MainLocator.LOCATOR_Q_5)
        seach_element_4.click()

    def check_open_tabs_6(self):
        element = self.find_element(MainLocator.LOCATOR_Q_2)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        seach_element_5 = self.find_element(MainLocator.LOCATOR_Q_6)
        seach_element_5.click()

    def check_open_tabs_7(self):
        element = self.find_element(MainLocator.LOCATOR_Q_2)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        seach_element_6 = self.find_element(MainLocator.LOCATOR_Q_7)
        seach_element_6.click()

    def check_open_tabs_8(self):
        element = self.find_element(MainLocator.LOCATOR_Q_2)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        seach_element_7 = self.find_element(MainLocator.LOCATOR_Q_8)
        seach_element_7.click()
    #Клик по верхней кнопке заказа
    def click_to_order_1(self):
        order_button = self.find_element(MainLocator.LOCATOR_ORDER_1)
        order_button.click()
    #Клик по нижней кнопке заказа
    def click_to_order_2(self):
        order_button_2 = self.find_element(MainLocator.LOCATOR_ORDER_2)
        order_button_2.click()
    #Клик по кнопке самоката в топе
    def click_to_samokat_logo(self):
        samokat_logo = self.find_element(MainLocator.LOCATOR_SAMOKAT_LOGO)
        samokat_logo.click()
    #Клик по лого Яндекса
    def click_to_ya_page(self):
        ya_page_logo = self.find_element(MainLocator.LOCATOR_YA_PAGE)
        ya_page_logo.click()

    def assert_ya_page(self):
        result = self.find_element(MainLocator.LOCATOR_YA_PAGE)
        return result.text()

    def asset_samokat_page(self):
        return self.find_element(MainLocator.LOCATOR_SAMOKAT_LOGO).text()

    def remove_cookie(self):
        cookie_button_element = self.driver.find_element(MainLocator.COOKIE_BUTTON)
        cookie_button_element.click()








