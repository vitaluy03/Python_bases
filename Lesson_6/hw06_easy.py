'''
Задача-1: Написать класс, например, Worker, который должен содержать информацию
о работнике (ФИО, оклад, надбавка за напряженность).
Создать экземпляр класса и передать конкретные данные (примеры ФИО, должности,
оклад и надбавки). Оклад и надбавку передать в виде строки.
На основе строки создать атрибут income, который реализовать в виде словаря
и инкапуслировать. Словарь income должен содержать информацию об окладе и надбавке.
Применить к экземпляру класса метод __dict__ и проверить какой будет результат
 применения этого метода.
А комментариях к заданию написать тип результата на русском языке.
'''
"""
class Worker:
    def __init__(self, name, surname, position, wage, surcharge, percent):
        self.name = name
        self.surname = surname
        self.position = position
        #elf.surcharge = surcharge
        self.percent = percent
        self.__income = {
        'wage' : int(wage),
        'surcharge' : int(surcharge)
        }

worker_1 = Worker("Алексанлр", "Петров", "Сварщик", '30000', '5000')
worker_2 = Worker("Сергей", "Иванов", "Каменщик", '30000', '3000')

#print(worker_1.get_full_name())
#print(worker_1.__income)
#print(worker_1.__dict__)
"""
"""
метод __dict__ примененный в экземпляру класса Worker позволяет вывести данные
в виде словаря где ключом является параметр класса а значение --значение экземпляра
класса
"""



'''
Задача-2: Продолжить работу над задачей 1. Создать на основе класса Worker класс
Position (реализовать наследование). Добавить классу уникальный атрибут -
% премии к зарплате (от суммы оклада).
Создать метод расчета зарплаты с учетом только премии.
Реализовать обращение к этому атриубуту, как к свойству.
Проверить работу всей структуры на реальных данных, вывести результаты.
'''
"""
class Worker:
    def __init__(self, name, surname, position, wage, surcharge):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {
        'wage' : int(wage),
        'surcharge' : int(surcharge)
        }


class Position(Worker):
    def __init__(self, name, surname, position, wage, surcharge, percent):
        Worker.__init__(self, name, surname, position, wage, surcharge)
        self.percent = percent

    @property
    def pobschii_dohod(self):
       dohod = (int(self._income['wage']) * int(self.percent))/100 + \
                                      (self._income['wage'])
       return dohod

position_1 = Position("Алексанлр", "Петров", "Сварщик", '30000', '5000', '15')
position_2 = Position("Сергей", "Иванов", "Каменщик", '30000', '3000', '12')
print(position_1.pobschii_dohod)
"""
'''
Задача-3: Продолжить работу над задачей 2.  Реализовать полиморфизм
использования знака + в методах 1) вывода полного имени работника и возраста
2) вычисления общего дохода работника с учетом надбавки .
Проверить работу всей структуры на реальных данных, вывести результаты.
'''

class Worker:
    def __init__(self, name, surname, position, wage, surcharge):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {
        'wage' : int(wage),
        'surcharge' : int(surcharge)
        }


class Position(Worker):
    def __init__(self, name, surname, age, position, wage, surcharge, percent):
        Worker.__init__(self, name, surname, position, wage, surcharge)
        self.percent = percent
        self.age = age

    @property
    def obschii_dohod(self):
       dohod = (int(self._income['wage']) * int(self.percent))/100 + \
                                      (self._income['wage'])

       return dohod
    @property
    def get_full_name_and_age_worker(self):
        return self.name + ' ' + self.surname + ' ' + str(self.age)



position_1 = Position("Алексанлр", "Петров", 30, "Сварщик", '30000', '5000', '15')
position_2 = Position("Сергей", "Иванов", 31, "Каменщик", '30000', '3000', '12')
#print(position_1.pobschii_dohod)
print(position_1.get_full_name_and_age_worker)
print(position_2.obschii_dohod)