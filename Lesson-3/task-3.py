import hashlib
import uuid

"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.
Подсказка: примените хеши и множества
рара:
рар
ра
ар
ара
р
а
"""


def func(substrings):
    substrings_hash_salt = {}
    for i in substrings:
        salt = uuid.uuid4().hex
        b = hashlib.sha3_256(salt.encode() + i.encode()).hexdigest() + ':' + salt
        substrings_hash_salt.setdefault(i,b)
        print(f'{i}  {substrings_hash_salt[i]}')
    return substrings_hash_salt


p = input('Введите строку ')

substrings = {p[i:j] for i in range(len(p)) for j in range(i + 1, len(p) + 1) if p != p[i:j]}
print(f'Список подстрок {substrings}')

a = func(substrings)

