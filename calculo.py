import math


class Calculo:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calcular_raices(self, signo):
        if signo == "+":
            res = -self.b + math.sqrt(math.pow(self.b, 2) - (4 * self.a * self.c))
        else:
            res = -self.b - math.sqrt(math.pow(self.b, 2) - (4 * self.a * self.c))
        return res / (2 * self.a)

    def mostrar_raices(self):
        x1 = self.calcular_raices("+")
        x2 = self.calcular_raices("-")
        return f'La raiz1 es {x1} \nLa raiz2 es {x2}'
