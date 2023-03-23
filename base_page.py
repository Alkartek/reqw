from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://qa-scooter.praktikum-services.ru/'

    def to_go(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator, time=100):
        return WebDriverWait(self.driver, time).until(ES.presence_of_element_located(locator), message=f'Not found {locator}')

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ES.presence_of_all_elements_located(locator), message=f'Not found {locator}')

