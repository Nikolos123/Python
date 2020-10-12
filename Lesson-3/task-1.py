# https://github.com/DmitryChitalov/python_algos_gb
# 1/17 9-10 слайд
import hashlib
import time

"""
Задание 1.
Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.


Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""


def timeit(f):
    def tmp(*args, **kwargs):
        time_start = time.time()
        res = f(*args, **kwargs)
        time_end = time.time()
        print('%s  %0.3f ms' % (f.__name__, (time_end - time_start) * 1000.0))
        return res

    return tmp


@timeit
def my_func_dic(d):
    # a = {k: v for (k, v) in d.items() if v % 2 == 0}
    return d.get(700)


@timeit
def my_func_list(c):
    # a = [i for i in c if i % 2 == 0]

    return c.index(700)


c = list(range(1, 5000))
my_func_list(c)

cc = list(range(1, 5000))
ccc = list(range(1, 5000))
cccc = {k: v for (k, v) in zip(cc, ccc)}

my_func_dic(cccc)


# my_func_list  0.423 ms
# my_func_dic  0.536 ms
# Если рассматривать добавления то в список быстрей будет добавлять так как только 1 значения  а в словарь нужно и ключ и значения
# но и то тут скорость не в 2 раза быстрей
# Если мы возьмем поиск через get( у словаря) и index(у списка увидем раздницу) примерно в 3 - 6 раз
# my_func_list  0.012 ms
# my_func_dic  0.002 ms