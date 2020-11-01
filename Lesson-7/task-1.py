"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).


Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность
Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""

import copy
import timeit
import random


def bubble_sort(lst_obj):
    n = 1
    s = 0
    print(lst_obj)
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            s = 0
            if lst_obj[i] < lst_obj[i+1]:
                s +=1
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        if s == 0:
            return print(lst_obj)
        n += 1
    return print(lst_obj)



def bubble_sort1(lst_obj):
    n = 1

    print(lst_obj)
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return print(lst_obj)

orig_list = [random.randint(-100, 100) for _ in range(10)]

orig_list1 = copy.deepcopy(orig_list)


# замеры 10
print(timeit.timeit("bubble_sort(orig_list)", setup="from __main__ import bubble_sort, orig_list", number=1))

# замеры 10
print(timeit.timeit("bubble_sort1(orig_list1)", setup="from __main__ import bubble_sort1, orig_list1", number=1))


# [40, 12, 63, -92, 57, 20, -59, -11, 1, 1]
# [63, 57, 40, 20, 12, 1, 1, -11, -59, -92]
# 3.015099991898751e-05
# [40, 12, 63, -92, 57, 20, -59, -11, 1, 1]
# [63, 57, 40, 20, 12, 1, 1, -11, -59, -92]
# 1.4767999800824327e-05


#Прошу дать комментарий по этому дз я вроде улучшил но почему время хуже не понятно отсортировал в обратном порядке