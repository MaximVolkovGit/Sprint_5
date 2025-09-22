from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Person
from urls import Urls
from locators import RegistrationPageLocators, AuthPageLocators ,MainPageLocators, RecoveryPageLocators

class TestLogin:

    def test_enter_button_login(self, driver):
        ''' Проверка входа через кнопку "Войти" на главной странице '''

        driver.get(Urls.MAIN_PAGE_URL)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.enter_button))
        driver.find_element(*MainPageLocators.enter_button).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(AuthPageLocators.login_button))
        driver.find_element(*AuthPageLocators.email_login_input).send_keys(Person.email)
        driver.find_element(*AuthPageLocators.password_login_input).send_keys(Person.password)
        driver.find_element(*AuthPageLocators.login_button).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.order_button))
        assert driver.current_url == Urls.MAIN_PAGE_URL and driver.find_element(
            *MainPageLocators.order_button).text == 'Оформить заказ'
        
    def test_account_button_ligin(self, driver):
        ''' Проверка входа через кнопку "Личный кабинет" на главной странице'''
        
        driver.get(Urls.MAIN_PAGE_URL)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.account_button))
        driver.find_element(*MainPageLocators.account_button).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(AuthPageLocators.login_button))
        driver.find_element(*AuthPageLocators.email_login_input).send_keys(Person.email)
        driver.find_element(*AuthPageLocators.password_login_input).send_keys(Person.password)
        driver.find_element(*AuthPageLocators.login_button).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.order_button))
        assert driver.current_url == Urls.MAIN_PAGE_URL and driver.find_element(
            *MainPageLocators.order_button).text == 'Оформить заказ'

    def test_login_by_registration_form(self, driver):
        '''Проверка входа через кнопку "Войти" на странице регистрации '''

        driver.get(Urls.REG_PAGE_URL)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(RegistrationPageLocators.enter_button))
        driver.find_element(*RegistrationPageLocators.enter_button).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(AuthPageLocators.login_button))
        driver.find_element(*AuthPageLocators.email_login_input).send_keys(Person.email)
        driver.find_element(*AuthPageLocators.password_login_input).send_keys(Person.password)
        driver.find_element(*AuthPageLocators.login_button).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.order_button))
        assert driver.current_url == Urls.MAIN_PAGE_URL and driver.find_element(
            *MainPageLocators.order_button).text == 'Оформить заказ'
        
    def test_login_by_password_recovery(self, driver):
        ''' Проверка входа через кнопку "Войти" в форме восстановления пароля '''
        
        driver.get(Urls.RECOVERY_PASSWORD_URL)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(RecoveryPageLocators.enter_button))
        driver.find_element(*RecoveryPageLocators.enter_button).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(AuthPageLocators.login_button))
        driver.find_element(*AuthPageLocators.email_login_input).send_keys(Person.email)
        driver.find_element(*AuthPageLocators.password_login_input).send_keys(Person.password)
        driver.find_element(*AuthPageLocators.login_button).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.order_button))
        assert driver.current_url == Urls.MAIN_PAGE_URL and driver.find_element(
            *MainPageLocators.order_button).text == 'Оформить заказ'