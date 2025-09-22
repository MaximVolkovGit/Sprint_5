from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import Urls
from locators import PersonalAccountLocators, AuthPageLocators, MainPageLocators

class TestGoToPersonalAccount:
    
    def test_transition_to_account_by_personal_account_button(self, login_driver):
        ''' Проверка перехода с главной страницы в аккаунт по клику на кнопку «Личный кабинет» '''
        
        driver = login_driver
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.account_button))
        driver.find_element(*MainPageLocators.account_button).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(PersonalAccountLocators.profile_button))
        assert driver.current_url == Urls.ACCOUNT_PAGE_URL

    def test_move_constructor_by_constructor_button(self, login_driver):
        ''' Проверка перехода из личного кабинета в конструктор по клику на кнопку «Конструктор» '''

        driver = login_driver
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.account_button))
        driver.find_element(*MainPageLocators.account_button).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.constructor_button))
        driver.find_element(*MainPageLocators.constructor_button).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.order_button))
        assert driver.current_url == Urls.MAIN_PAGE_URL and (driver.find_element(*MainPageLocators.order_button).is_displayed())

    def test_test_move_constructor_by_logo(self, login_driver):
        ''' Проверка перехода из личного кабинета в конструктор по клику на логотип Stellar Burgers '''

        driver = login_driver
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.account_button))
        driver.find_element(*MainPageLocators.account_button).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(PersonalAccountLocators.profile_button))
        driver.find_element(*PersonalAccountLocators.logo_SB).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.order_button))
        assert (driver.current_url == Urls.MAIN_PAGE_URL) and (driver.find_element(*MainPageLocators.order_button).is_displayed())

    def test_exit_of_account_by_exit_button(self, login_driver):
        ''' Проверка выхода из из личного кабинета по кнопке «Выйти» в личном кабинете '''

        driver = login_driver
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.account_button))
        driver.find_element(*MainPageLocators.account_button).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(PersonalAccountLocators.exit_button))
        driver.find_element(*PersonalAccountLocators.exit_button).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(AuthPageLocators.title_text))
        assert (driver.current_url == Urls.AUTH_PAGE_URL) and (driver.find_element(*AuthPageLocators.login_button).is_displayed())
