from selenium.webdriver.common.by import By

class RegistrationPageLocators():
    """Локаторы страницы регистрации (https://stellarburgers.nomoreparties.site/register) """
    
    reg_button = (By.XPATH, "//button[text()='Зарегистрироваться']")
    name_input = (By.XPATH, "//label[text()='Имя']/../input")
    email_input = (By.XPATH, "//label[text()='Email']/../input")
    password_input = (By.XPATH, "//input[@type='password']")


class AuthPageLocators():
    """Локаторы страницы входа https://stellarburgers.nomoreparties.site/login """

    login_button = (By.XPATH, "//button[text()='Войти']")
    title_text = (By.XPATH, ".//h2[text()='Вход']")
    incorrect_password_message = (By.XPATH, "//p[text()='Некорректный пароль']")

