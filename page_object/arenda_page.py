from selenium.webdriver.common.by import By


from selenium.webdriver.support.wait import WebDriverWait

from base_page import BasePage


#Локаторы страницы Аредны
class ArendaLocator:
    LOCATOR_CALENDAR = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    LOCATOR_TIME_ORDER = (By.XPATH, '//div[@class="Dropdown-placeholder"]')
    LOCATOR_COLOR = (By.XPATH, '//input[@id="black"]')
    LOCATOR_COMMENT = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    LOCATOR_ORDER_BUTTON = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')
    LOCATOR_ASSERT_ORDER = (By.XPATH, '//div[@class="Order_ModalHeader__3FDaJ"]')
    LOCATOR_ASSERT_YES = (By.XPATH, '//div[@class="Order_Modal__YZ-d3"]/div[@class="Order_Buttons__1xGrp"]/button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')
    LOCATOR_RESULT_OREDER = (By.XPATH, '//div[@class="Order_ModalHeader__3FDaJ"]')
    LOCATOR_CHOOSE_DATE = (By.XPATH, '//div[@aria-label="Choose среда, 8-е марта 2023 г."]')
    LOCATOR_CHOOSE_TIME = (By.XPATH, "//div[contains(text(),'четверо')]")
    LOCATOR_WAIT = (By.XPATH, '//div[@class="Order_Header__BZXOb"]')
    LOCATOR_RESULT_COMPLITE = (By.XPATH, '//button[contains(text(),"Посмотреть статус")]')

#Тестовый класс для страницы аренды
class ArenfaForm(BasePage):
    #Форма заполнения аренды
    def from_element(self):

        calendar_form = self.find_element(ArendaLocator.LOCATOR_CALENDAR)
        calendar_form.click()
        date_choose = self.find_element(ArendaLocator.LOCATOR_CHOOSE_DATE)
        date_choose.click()
        time_use = self.find_element(ArendaLocator.LOCATOR_TIME_ORDER)
        time_use.click()
        time_choose = self.find_element(ArendaLocator.LOCATOR_CHOOSE_TIME)
        time_choose.click()
        color_use = self.find_element(ArendaLocator.LOCATOR_COLOR)
        color_use.click()
        coment = self.find_element(ArendaLocator.LOCATOR_COMMENT)
        coment.send_keys('-')

    #Клик по кнопек формы заказа
    def form_oder_button(self):
        order_button = self.find_element(ArendaLocator.LOCATOR_ORDER_BUTTON)
        order_button.click()
        button_assert = self.find_element(ArendaLocator.LOCATOR_ASSERT_YES)
        button_assert.click()

    #Экран подтверждения заказа
    def order_status(self):
        result_order = self.find_element(ArendaLocator.LOCATOR_RESULT_OREDER)
        result_order_text = result_order.text()
        return result_order_text
    #Кнопка подтвержения заказа
    def last_order_accept(self):
        order_button = self.find_element(ArendaLocator.LOCATOR_RESULT_COMPLITE)
        order_button.click()