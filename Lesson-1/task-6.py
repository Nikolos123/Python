
"""
Задание 6.
Задание на закрепление навыков работы с очередью
Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока
Реализуйте структуру "доска задач".
Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
После реализации структуры, проверьте ее работу на различных сценариях
"""
list_task = {'Выполнить расчеты': 1, 'Выполнить пересчеты': 1, 'Выполнить дорасчеты': 1,
             'Выполнить домашнее задание': 0, 'НеВыполнить расчеты': 0}
done = {}
revision = {}

class Task:
    def __init__(self, k,v):
        self.k = k
        self.v = v
    def decision_task(self):

            if self.v == 1:
                del list_task[self.k]
                done.setdefault(self.k, self.v)
            elif self.v == 0:
                del list_task[self.k]
                revision.setdefault(self.k, self.v)

    def decision_task_revision(self):
            if v == 0:
                del revision[k]
                done.setdefault(k, 1)


print(f' Задачи {list_task} \n Выполнено {done} \n Переделать {revision}')

copy_dici_dic = list_task.copy() #  у нас нету двойного вложения так что подойдет такой вариант

for k, v in copy_dici_dic.items():
    mc = Task(k,v)
    mc.decision_task()
    print(f' Задачи {list_task} \n Выполнено {done} \n Переделать {revision}')

print("ВЫПОЛНЯЕМ РЕШЕНИЯ ПОВТОРНЫХ ЗАДАЧ")

copy_revi_dic = revision.copy()
for k, v in copy_revi_dic.items():
    mc = Task(k, v)
    mc.decision_task_revision()
    print(f' Задачи {list_task} \n Выполнено {done} \n Переделать {revision}')
