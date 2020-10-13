import uuid
import hashlib

"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"
Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш


Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
cash_dic_url = {}


def cash_usrl(url):
    salt = uuid.uuid4().hex
    b = hashlib.sha3_256(salt.encode() + url.encode()).hexdigest() + ':' + salt
    if url not in cash_dic_url:
        cash_dic_url.setdefault(url, b)
        print(f'Адрес {url} добавлен и его хэш = {cash_dic_url[url]}')
    else:
        print(f'Адрес {url} уже существует его хэш = {cash_dic_url[url]}')
    return cash_dic_url


ans = ''
while ans != '0':
    print('Для выхода введите 0')
    ans = str(input('Введите адрес '))
    if ans == '0':
        print('Мы вышли из программы')
        break
    cash_usrl(ans)
