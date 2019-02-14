'''
Задача-1: Создать класс Матрица. В конструктор класса передавать переменную
содержащую матрицу в виде списка списков. В конструкторе класса преобразовать
список списков в привычный матричный вид. Переопределить стандартное поведение
методов __add__ и __str__ класса. Создать два экземпляра класса Матрица с данными.
Метод __add__ должен реализовывать сложение матриц, а __str__ - вывод итоговой
матрицы.
'''
class Matrix:
    def __init__ (self, a):
        self.a = a

    def __str__(self):
        self.a_str = '\n'.join(str(el) for el in self.a)
        return  self.a_str

    def __add__(self, other):
        res = []
        for i in range(len(self.a)):
            numbers = []
            for j in range(len(self.a[i])):
                summa = other.a[i][j] + self.a[i][j]
                numbers.append(summa)
            res.append(numbers)

        return Matrix(res)

m = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m1 = Matrix([[3, 2, 1], [6, 5, 4], [9, 8, 7]])

print(m + m1)


