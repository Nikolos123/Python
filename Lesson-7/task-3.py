
"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.
Задачу можно решить без сортировки исходного
массива.
Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...
arr[m]
from statistics import median
"""

import  numpy as np

a = np.arange(22).reshape(1, 22)
print(a)
print(np.median(a,axis=(0,1)))

#Вариант решения нашел в библиотеки numpy очень полезная библиотека

#Вариант решения через ШЕЛЛ
def shell(seq):
    inc = len(seq) // 2
    while inc:
        for i, el in enumerate(seq):
            while i >= inc and seq[i - inc] > el:
                seq[i] = seq[i - inc]
                i -= inc
            seq[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)


data = [i for i in range(1,22)]
shell(data)
print(data)
print(len(data)/2)