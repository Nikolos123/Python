"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from collections import OrderedDict
import timeit


def func1():
    a = range(1, 100)
    aa = dict()
    for i in a:
        aa[i] = i


def func2():
    a = range(1, 100)
    aa = dict()
    for i in a:
        aa[i] = i
    return aa.get(55)


# def func3():
#     pass
#
#
# def func4():
#     pass


def func11():
    a = range(1, 10)

    aa = OrderedDict()
    for i in a:
        aa[i] = i


def func22():
    a = range(1, 100)
    aa = OrderedDict()
    for i in a:
        aa[i] = i

    return aa.get(55)


#
# def func33():
#     pass
#
#
# def func44():
#     pass


print(timeit.timeit("func1", setup="from __main__ import func1", number=100000), "milleseconds")
print(timeit.timeit("func2", setup="from __main__ import func2", number=100000), "milleseconds")
# print(timeit.timeit("func3", setup="from __main__ import func3", number=100000), "milleseconds")
# print(timeit.timeit("func4", setup="from __main__ import func4", number=100000), "milleseconds")

print('=' * 100)

print(timeit.timeit("func11", setup="from __main__ import func11", number=100000), "milleseconds")
print(timeit.timeit("func22", setup="from __main__ import func22", number=100000), "milleseconds")
# print(timeit.timeit("func33", setup="from __main__ import func33", number=100000), "milleseconds")
# print(timeit.timeit("func44", setup="from __main__ import func44", number=100000), "milleseconds")


# Если выбрать все замеры то цифры меняются и оба метода что через ордер что через dict работает в целом одинакого


# 0.0012453999999999972 milleseconds
# 0.0012427999999999988 milleseconds
# ====================================================================================================
# 0.0012488000000000013 milleseconds
# 0.0012519000000000002 milleseconds
