'''
Задание 1. Реализовать класс-строитель. В его конструктор передать два списка.
Класс должен возвратить python-объект словарь. Проверить, что объект
создается корректно - создать экземпляр класса и обратиться к значению
элемента словаря, как к атрибуту класса.
'''

class DeatilBuilder:
     def __init__(self, elem):
        for a, b in elem.items():
            setattr(self, a, b)

detail = DeatilBuilder({'name' : 'sensor', 'purpose' : 'cooling system'})
print(detail.name)
print(detail.purpose)




'''
Задание 2.
Создать класс-обертку для списка. Список передвайте в конструктор класса.
Реализуйте удаление всех элементов из списка через функцию clear.
Но функция должна применяться не к списку, а к экземпляру класса.
Внутри класса должно быть предусмотрено делегирование этой функции методу (clear)
списка.
'''
class MyClass:
    def __init__(self, lst):
        self.obj = lst

    def __getattr__(self, attr):
        return getattr(self.obj, attr)


new_lst = MyClass([1, 2, 3, 4, 5, 6, 7, 8, 9])
new_lst.clear()
print(new_lst.obj)


