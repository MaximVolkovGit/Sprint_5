import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import RandomData
from urls import Urls
from locators import RegistrationPageLocators, AuthPageLocators

class TestRegistrationPage:
    
    def test_registration_success(self, driver):
        '''После успешной регистрации открывается страница авторизации'''
        driver.get(Urls.REG_PAGE_URL)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(RegistrationPageLocators.reg_button))
        driver.find_element(*RegistrationPageLocators.name_input).send_keys(RandomData.user_name)
        driver.find_element(*RegistrationPageLocators.email_input).send_keys(RandomData.email)
        driver.find_element(*RegistrationPageLocators.password_input).send_keys(RandomData.password)
        driver.find_element(*RegistrationPageLocators.reg_button).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(AuthPageLocators.login_button))
        assert driver.current_url == Urls.AUTH_PAGE_URL and driver.find_element(*AuthPageLocators.title_text)

    def test_invalid_password_registration(self, driver):
        '''Не проходит регистрация с паролем менее 6 символов'''
        driver.get(Urls.REG_PAGE_URL)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(RegistrationPageLocators.reg_button))
        driver.find_element(*RegistrationPageLocators.name_input).send_keys(RandomData.user_name)
        driver.find_element(*RegistrationPageLocators.email_input).send_keys(RandomData.email)
        driver.find_element(*RegistrationPageLocators.password_input).send_keys('12345')
        driver.find_element(*RegistrationPageLocators.reg_button).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_any_elements_located(AuthPageLocators.incorrect_password_message))
        error_message = driver.find_element(*AuthPageLocators.incorrect_password_message).text
        assert (driver.current_url == Urls.REG_PAGE_URL) and error_message == 'Некорректный пароль'

