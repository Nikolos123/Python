"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def func(n=0, s=0, c=1):
    b = n + 1
    if b > c:
        s += c
        c += 1
        func(n, s, c)
    else:
        print(n)
        print(n * (n + 1) // 2)
        print(s)
        return


n = int(input('Введите число '))
func(n)
