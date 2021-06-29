class Carro:

    def __init__(self, modelo, marca, hp, color, velocidad_maxima='200'):
        self.modelo = modelo
        self.marca = marca
        self.hp = hp
        self.color = color
        self.velocidad_maxima = velocidad_maxima
        self._motor = Motor(4, True)

    def acelerar(self, velocidad):
        self.velocidad_maxima = self.velocidad_maxima + velocidad

    def llenar_gasolina(self):
        self._motor.afinar_motor()

    def girar(self):
        pass

    def pagar_carro(self):
        pass

    def compar_partes_carro(self):
        pass

    def mantenimiento_carro(self):
        pass


class Motor:

    def __init__(self, cilindro, radiador):
        self.cilindro = cilindro
        self.radiador = radiador

    def afinar_motor(self):
        pass
