"""
Задание 1.
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
Сделайте замеры времени выполнения кода с помощью модуля timeit
Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры
Добавьте аналитику: что вы сделали и почему
"""

import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr1 = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr1


a = list(range(1, 100))
b = func_1(a)

print(timeit.timeit("func_1(a)", setup="from __main__ import func_1, a", number=100000), "milleseconds")
print(timeit.timeit("func_2(a)", setup="from __main__ import func_2, a", number=100000), "milleseconds")

# Время  замера
# func 0.6123506759977317 milleseconds
# func2 0.5176595420052763 milleseconds

#Аналитика
#Добавил вариант с генераторным вырожением так как она отрабатывает быстрей время приведено выше