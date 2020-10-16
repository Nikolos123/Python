"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через cProfile и через timeit
Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
import timeit
import cProfile

A = 10


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def main():
    revers(A)
    revers_2(A)
    revers_3(A)


# Цифры говорят сами за себя в 1 и 2 решении используется много сравнений и других операций а это время в нижнем идет присвоении и срез
# 0.04545813000004273 milleseconds
# 0.029811742002493702 milleseconds
# 0.02300449999893317 milleseconds

print(timeit.timeit("revers(A)", setup="from __main__ import revers, A", number=100000), "milleseconds")
print(timeit.timeit("revers_2(A)", setup="from __main__ import revers_2, A", number=100000), "milleseconds")
print(timeit.timeit("revers_3(A)", setup="from __main__ import revers_3, A", number=100000), "milleseconds")

cProfile.run('main()')
# Насчет Cprofile это действительно мошный инструмент он не только показывает ваши функции но и все что
# он вызвал по дароге исполняя код
# в нашем случаи везде нули(это значит хорошо) так как действия у нас очень легкие