import pytest
from selenium import webdriver
from urls import Urls
from locators import AuthPageLocators
from data import Person

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def login_driver(driver):
    driver.get(Urls.AUTH_PAGE_URL)
    driver.find_element(*AuthPageLocators.email_login_input).send_keys(Person.email)
    driver.find_element(*AuthPageLocators.password_login_input).send_keys(Person.password)
    driver.find_element(*AuthPageLocators.login_button).click()
    return driver