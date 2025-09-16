from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import Urls
from locators import MainPageLocators

class TestConstructor:
    
    def test_move_to_buns(self, driver):
        """ Проверка перехода к разделу 'Булки' """

        driver.get(Urls.MAIN_PAGE_URL)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.sauces_button))
        driver.find_element(*MainPageLocators.sauces_button).click()
        driver.find_element(*MainPageLocators.buns_button).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.bun_list))
        assert driver.find_element(*MainPageLocators.bun_list).is_displayed() and driver.find_element(
            *MainPageLocators.buns).text == 'Булки'

    def test_move_to_sauces(self, driver):
        """ Проверка перехода к разделу 'Соусы' """

        driver.get(Urls.MAIN_PAGE_URL)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.sauces_button))
        driver.find_element(*MainPageLocators.sauces_button).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.sauces_list))
        assert driver.find_element(*MainPageLocators.sauces_list).is_displayed() and driver.find_element(
            *MainPageLocators.sauces).text == 'Соусы'
        
    def test_move_to_toppings(self, driver):
        """ Проверка перехода к разделу 'Начинки' """

        driver.get(Urls.MAIN_PAGE_URL)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.toppings_button))
        driver.find_element(*MainPageLocators.toppings_button).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.topping_list))
        assert driver.find_element(*MainPageLocators.topping_list).is_displayed() and driver.find_element(
            *MainPageLocators.toppings).text == 'Начинки'
