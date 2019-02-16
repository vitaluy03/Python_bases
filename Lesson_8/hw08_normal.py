'''
Задание_1. Создать класс. В конструктор передать два параметра - два числа.
Создать второй класс. В конструкторе первого предусмотреть создание
объекта второго класса. Кроме того, в первом классе предусмотреть три метода,
в которых делегировать получение остатка от деления, результата деления и целой
части от деления в методы второго класса (предусмотреть вычисление в соотв. методах
второго класса).
'''
# Задание_1. Создать класс.
class First:
    # В конструктор передать два параметра - два числа.
    def __init__(self, a, b):
        # В конструкторе первого предусмотреть создание
        # объекта второго класса.
        self.calc = Calculator()
        self.a = a
        self.b = b

    # Кроме того, в первом классе предусмотреть три метода, в которых делегировать получение

    # остатка от деления,
    def get_remainder(self):
        return self.calc.remainder(self.a, self.b)

    # результата деления
    def get_divide(self):
        return self.calc.divide(self.a, self.b)

    # и целой части от деления
    def get_whole_divide(self):
        return self.calc.whole_divide(self.a, self.b)


# Создать второй класс.
class Calculator:

    # в методы второго класса
    # (предусмотреть вычисление в соотв. методах второго класса).
    def remainder(self, a, b):
        return a % b

    def divide(self, a, b):
        return a / b

    def whole_divide(self, a, b):
        return a // b


my_obj = First(27, 5)
print(my_obj.get_remainder())
print(my_obj.get_divide())
print(my_obj.get_whole_divide())

