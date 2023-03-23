import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def browser():
    driver = webdriver.Firefox(executable_path='./geckodriver')
    yield driver
    driver.quit()