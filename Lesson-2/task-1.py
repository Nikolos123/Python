"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, /
- условие завершения рекурсии - введена операция 0
Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""

def calc():
    print('Введите операцию (+, -, *, / или 0 для выхода)')
    a = int(input("Введите число 1 "))
    b = int(input("Введите число 2 "))

    c = input("Введите операцию ")
    if c == '0':
        return print('выход из программы')
    elif c == '+':
        print(f'сумма  = {a +b}')
        calc()
    elif c == '-':
        print(f'вычетание  = {a - b}')
        calc()
    elif c == '*':
        print(f'умножение  = {a * b}')
        calc()
    elif c == '/':
        if a and b != 0:
            print(f'вычетание  = {a / b}')
            calc()
        else:
            print('Деление на 0 не возможно')
            calc()
    else:
        return print('выход из программы')
calc()