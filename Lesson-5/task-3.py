from collections import deque
import timeit

"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.
Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
"""


def func1():
    print(deque(range(1000)))


def func2():
    d = deque()
    for i in range(1000):
        d.append(i)

    print(d)


def func3():
    d = deque(range(1000))
    d.pop()
    print(d)


def func4():
    print(deque().appendleft(range(1)))


print(timeit.timeit("func1", setup="from __main__ import func1", number=100000), "milleseconds")
print(timeit.timeit("func2", setup="from __main__ import func2", number=100000), "milleseconds")
print(timeit.timeit("func3", setup="from __main__ import func3", number=100000), "milleseconds")
print(timeit.timeit("func4", setup="from __main__ import func4", number=100000), "milleseconds")

print('=' * 100)


def func11():
    d = list(range(1000))


def func22():
    d = list()
    for i in range(1000):
        d.append(i)


def func33():
    d = list(range(1000))
    d.pop()


def func44():
    d = list
    d.insert(0, 1)


print(timeit.timeit("func11", setup="from __main__ import func11", number=100000), "milleseconds")
print(timeit.timeit("func22", setup="from __main__ import func22", number=100000), "milleseconds")
print(timeit.timeit("func33", setup="from __main__ import func33", number=100000), "milleseconds")
print(timeit.timeit("func44", setup="from __main__ import func44", number=100000), "milleseconds")

## Как было сказано вставляем через дописываем и получаем используем deque в в иных list та как есть приток во времени работы
