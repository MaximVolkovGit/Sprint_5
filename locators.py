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
    constructor_button = (By.XPATH, "//p[text()='Конструктор']")  #  Кнопка "Конструктор"
    assemble_burger_button = (By.XPATH, "//h1[text()='Соберите бургер']")  # Надпись "Соберите бургер"
    buns_button = (By.XPATH, ".//span[text() = 'Булки']") #Кнопка переключения на булки
    sauces_button = (By.XPATH, ".//span[text() = 'Соусы']") #Кнопка переключения на соусы
    toppings_button = (By.XPATH, ".//span[text() = 'Начинки']") #Кнопка переключения на начинки
    bun_list = (By.XPATH, "(.//ul[@class = 'BurgerIngredients_ingredients__list__2A-mT'])[1]") #  Список булок на главной странице
    sauces_list = (By.XPATH, "(.//ul[@class = 'BurgerIngredients_ingredients__list__2A-mT'])[2]") # Список соусов на главной странице
    topping_list = (By.XPATH, "(.//ul[@class = 'BurgerIngredients_ingredients__list__2A-mT'])[3]") #  Список начинок на главной странице
    buns = (By.XPATH, ".//h2[text() = 'Булки']") # Раздел "Булки" в списке
    sauces = (By.XPATH, ".//h2[text() = 'Соусы']") # Раздел "Соусы" в списке
    toppings = (By.XPATH, ".//h2[text() = 'Начинки']") # Раздел "Начинки" в списке


class RecoveryPageLocators():
    """ Локаторы страницы восстановления пароля"""

    enter_button = (By.XPATH, "//a[text()='Войти']")   #  Кнопка "Войти"

class PersonalAccountLocators():
    ''' Локаторы личного кабинета '''

    exit_button = (By.XPATH, "//button[text()='Выход']") #  Кнопка выхода из аккаунта
    profile_button = (By.XPATH, "//a[text()='Профиль']")  # Кнопка "Профиль"
    logo_SB = (By.XPATH, "//div[@class = 'AppHeader_header__logo__2D0X2']")  #  Логотип Stellar Burgers
