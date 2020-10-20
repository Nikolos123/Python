import collections
import timeit

"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)
"""

my_dict = collections.defaultdict(str)
my_dict.setdefault('-')
my_dict.setdefault('+')
my_dict.setdefault('*')

my_dict1 = {'-','+','*'}


a = int(input("Введите первое число в шестнадцатиричной системы счисления "), 16)

b = int(input("Введите второе число в шестнадцатиричной системы счисления "), 16)
c = input('Выберите метод / - + * ')
def func1():
    if c in my_dict:
        if c == '+':
            print(hex(a + b)[2:].upper())
        elif c =='-':
            print(hex(a-b)[2:].upper())
        elif c =='*':
            print(hex(a*b)[2:].upper())
        else:
            print('что-то пошло не так')

def func2():
    if c in my_dict1:
        if c == '+':
            print(hex(a + b)[2:].upper())
        elif c =='-':
            print(hex(a-b)[2:].upper())
        elif c =='*':
            print(hex(a*b)[2:].upper())
        else:
            print('что-то пошло не так')

print(timeit.timeit("func1", setup="from __main__ import func1", number=100000), "milleseconds")
print(timeit.timeit("func2", setup="from __main__ import func2", number=100000), "milleseconds")

# Если верить цифрам то 2 идентичных алгоритма но используем мы с вами модуль колекции и обычный словарь то обычный отрабатывает чуток быстрей
# 0.0012503999999999849 milleseconds
# 0.0012407000000003165 milleseconds