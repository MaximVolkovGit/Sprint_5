from selenium.webdriver.common.by import By

class RegistrationPageLocators():
    """Локаторы страницы регистрации (https://stellarburgers.nomoreparties.site/register) """
    
    reg_button = (By.XPATH, "//button[text()='Зарегистрироваться']") # Кнопка "Зарегистрироваться"
    name_input = (By.XPATH, "//label[text()='Имя']/../input")  # Поле ввода Имени
    email_input = (By.XPATH, "//label[text()='Email']/../input")  #  Поле ввода майла
    password_input = (By.XPATH, "//input[@type='password']")  #  Поле ввода пароля
    enter_button = (By.XPATH, "//a[text()='Войти']")  #  Кнопка "Войти"


class AuthPageLocators():
    """Локаторы страницы входа https://stellarburgers.nomoreparties.site/login """

    title_text = (By.XPATH, "//h2[text()='Вход']")  #  Заголовок страницы входа
    email_login_input = (By.XPATH, "//input[@name='name']") #  Поле ввода майла
    password_login_input = (By.XPATH, "//input[@name='Пароль']")  #  Поле ввода пароля
    login_button = (By.XPATH, "//button[text()='Войти']")  #  Кнопка "Войти"
    incorrect_password_message = (By.XPATH, "//p[text()='Некорректный пароль']")  #  Текст сообщения о некорректном пароле
    

class MainPageLocators():
    """Локаторы главной страницы """

    enter_button = (By.XPATH, "//button[text()='Войти в аккаунт']")  #  Кнопка входа в аккаунт
    order_button = (By.XPATH, "//button[text()='Оформить заказ']") #  Кнопка "Оформить заказ"
    account_button = (By.XPATH, "//p[text()='Личный Кабинет']")  #  Кнопка "Личный кабинет"

class RecoveryPageLocators():
    """ Локаторы страницы восстановления пароля"""

    enter_button = (By.XPATH, "//a[text()='Войти']")   #  Кнопка "Войти"
