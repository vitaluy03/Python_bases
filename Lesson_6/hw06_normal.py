'''
Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
'''

import math

class Triangle ():
    def __init__(self, a_x, a_y, b_x, b_y, c_x, c_y):
        self.a_x = a_x
        self.a_y = a_y
        self.b_x = b_x
        self.b_y = b_y
        self.c_x = c_x
        self.c_y = c_y
        self.AB = round (math.sqrt(int (math.fabs(((b_y - a_y)**2) + ((b_x - a_x)**2)))),2)
        self.BC = round(math.sqrt(int(math.fabs(((c_y - b_y) ** 2) + ((c_x - b_x) ** 2)))), 2)
        self.CA = round(math.sqrt(int(math.fabs(((a_y - c_y) ** 2) + ((a_x - c_x) ** 2)))), 2)

    def perimetr(self):
        self.perimetr = (self.AB + self.BC + self.CA)
        return (self.perimetr)

    def ploshad(self):
        self.perimetr /=2
        self.ploshad =  round(math.sqrt(self.perimetr*(self.perimetr - self.AB) \
        *(self.perimetr - self.BC)* (self.perimetr - self.CA)),2)
        return (self.ploshad)

    def vysota(self):
        self.ploshad *=2
        self.vysota =  round((self.ploshad / self.CA),2)
        return (self.vysota)

treugol_1 = Triangle(13, 31, 43, 54, 54, 32)

print(treugol_1.perimetr())
print(treugol_1.ploshad())
print(treugol_1.vysota())
