from selenium.webdriver.common.by import By

from base_page import BasePage


class OrderLocator:
    LOCATOR_NAME = (By.XPATH, '//input[@placeholder="* Имя"]')
    LOCATOR_SECOND_NAME = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    LOCATOR_ADRESS = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    LOCATOR_METRO = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    LOCATOR_NUMBER = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    LOCATOR_NEXT_STEP = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')
    LOCATOR_STANTION = (By.XPATH, '//li[@data-index="1"]')



class OrderPage(BasePage):
    def input_elements(self, ima, familia, street):
        name = self.find_element(OrderLocator.LOCATOR_NAME)
        name.send_keys(ima)
        second_name = self.find_element(OrderLocator.LOCATOR_SECOND_NAME)
        second_name.send_keys(familia)
        adress = self.find_element(OrderLocator.LOCATOR_ADRESS)
        adress.send_keys(street)
        metro = self.find_element(OrderLocator.LOCATOR_METRO)
        metro.click()
        stantion = self.find_element(OrderLocator.LOCATOR_STANTION)
        stantion.click()
        number = self.find_element(OrderLocator.LOCATOR_NUMBER)
        number.send_keys("98729321230")

    def click_to_next(self):
        button_next = self.find_element(OrderLocator.LOCATOR_NEXT_STEP)
        button_next.click()







