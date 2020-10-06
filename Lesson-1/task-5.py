"""
Задание 6.
Задание на закрепление навыков работы со стеком


Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "стопка тарелок".
Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.

Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.
После реализации структуры, проверьте ее работу на различных сценариях
"""
print("Сложность O(n2)")
print("Задача 5")
steck = []
class StackOfPlates:

    def __init__(self, a):
        self.a = a
    def add_plates(self):
        if len(steck) == 0:
            steck.append([])
            steck[0].append(self.a)
        else:
            kossmass = len(steck)
            kolmasspol = len(steck[kossmass-1])

            if kolmasspol != 10:
                steck[kossmass-1].append(self.a)
            else:
                steck.append([])
                steck[kossmass].append(self.a)


    def del_plates(self):
        steck[self.a].pop()

ites = [i for i in range(1,19)]
print(ites)
for i in ites:
    mc = StackOfPlates(int(i))
    mc.add_plates()
    print(steck)
st = 0
for i in steck:
    ii = 0
    while len(i)>=1:
        mc = StackOfPlates(st)
        mc.del_plates()
        print(steck)
        ii +=1
    st += 1