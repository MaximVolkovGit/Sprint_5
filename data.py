from random import randint

class Person:
    user_name = 'Максим'
    email = f'maxim_volkov_31_951@ya.ru'
    password = f'12345Qwe'

class RandomData:
    user_name = 'Тест'
    email = f'test_user{randint(0, 999)}@ya.ru'
    password = f'{randint(1000, 9999)}Qwe'