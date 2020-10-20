from collections import defaultdict
import timeit

"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235
Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34
Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога
Предприятия, с прибылью ниже среднего значения: Копыта
"""


def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]

    return decorate


my_dict = defaultdict(int)
ans = int(input("Введите количество предприятий для расчета прибыли: "))
while ans > 0:
    ans -= 1
    print(
        "Пример ввода информации по предприятию: Копыта через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): 235 345634 55 235")
    company = input("Введите название предприятия: ")
    a = company.split(" ")
    my_dict[str(a[0])] = sum([int(i) for i in a[1:]]) / 12

print(f'Средняя годовая прибыль всех предприятий: {sum(my_dict.values())} ')

def func1():
    mini_int = 0
    maxi = ''
    maxi_int = 0
    mini = ''
    for k, v in my_dict.items():
        if v > maxi_int:
            mini_int = maxi_int
            mini = maxi
            maxi_int = v
            maxi = k
        elif v < maxi_int:
            mini_int = v
            mini = k

    print(f'Предприятия, с прибылью ниже среднего значения: {mini} ')

    print(f'Предприятия, с прибылью выше среднего значения: {maxi} ')

def func2():
    maxi = defaultdict(int)
    mini = defaultdict(int)

    for k, v in my_dict.items():
        if len(maxi) == 0:
            maxi[k] = v
        elif sum(maxi.values()) < v:
            if len(mini) > 0:
                mini.clear()
            mini = maxi.copy()
            maxi.clear()
            maxi[k] = v
        elif sum(mini.values()) > v:
            mini.clear()
            mini[k] = v

    print(f'Предприятия, с прибылью ниже среднего значения: {next(iter(maxi))} ')
    #
    print(f'Предприятия, с прибылью выше среднего значения: {next(iter(mini))} ')


print(timeit.timeit("func1", setup="from __main__ import func1", number=100000), "milleseconds")
print(timeit.timeit("func2", setup="from __main__ import func2", number=100000), "milleseconds")

#Так как оба варианта используют словари то время практически одинаково но 2 немного быстрей получается из за более лаконичного подхода