# import hashlib
from hashlib import pbkdf2_hmac
from binascii import hexlify

"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш
Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей
ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
"""


def hash_pass(password, salt):
    # return hashlib.sha3_256(salt.encode() + password.encode()).hexdigest() + ':' + salt
    return pbkdf2_hmac(hash_name='sha256',
                       password=password.encode(),
                       salt=salt.encode(),
                       iterations=50000)


def check_pass(password_user, salt, hash_password):
    # password, salt = hash_password.split(':')
    return hash_password == hexlify(pbkdf2_hmac(hash_name='sha256',
                                                password=password_user.encode(),
                                                salt=salt.encode(),
                                                iterations=50000))
    # return password == hashlib.sha3_256(salt.encode() + password_user.encode()).hexdigest()


a = str(input('Введите логин '))
b = str(input('Введите пароль '))

hash_test = hexlify(hash_pass(b, a))
print(f'В базе данных хранится строка {hash_test}')

a = str(input('Введите повторно пароль '))
if check_pass(b, a, hash_test):
    print('ВЫ ввели правильный пароль')
else:
    print('Извините, но пароли не совпадают')
