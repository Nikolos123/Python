"""
Задание 4.
Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.
Сделайте профилировку каждого алгоритма через timeit
Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""

import timeit

array = [2, 5, 5, 3, 1, 3, 4, 5, 1]


def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]

    return decorate


@memoize
def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


@memoize
def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)
    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


@memoize
def func_3():
    a = [array.count(i) for i in array]
    max_1 = max(a)
    elem = array[a.index(max_1)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_1} раз(а)'


print(func_1())
print(func_2())
print(func_3())

print(timeit.timeit("func_1()", setup="from __main__ import func_1", number=100000), "milleseconds")
print(timeit.timeit("func_2()", setup="from __main__ import func_2", number=100000), "milleseconds")
print(timeit.timeit("func_3()", setup="from __main__ import func_3", number=100000), "milleseconds")

# Третья версия быстрей получилась через генераторные вырожения + memoization ( даже если memoization добавить к выше стоящим функция результат будет хуже)
# Как мы видим верхний вариант вообще практически не изменился а там где были списки мы увидили приток а за счет генераторного вырожения мы улучшили функцию
# 0.13551701699907426 milleseconds
# 0.16544496900314698 milleseconds
# 0.008733570997719653 milleseconds

# 0.01375451400235761 milleseconds
# 0.009378078000736423 milleseconds
# 0.008300045003124978 milleseconds
