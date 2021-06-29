class Persona:
    # contiene muchos metodos
    # metodos => funciones
    # __init__ => es el constructor
    # el constructor es la funcion que se ejecuta al iniciary
    # la clase
    #                   Pepito 85
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    # Creo un metodo llamado saludar
    def saludar(self, otro_nombre):
        return f'Hola {otro_nombre} mi nombre' \
               f' es {self.nombre}, mi edad es {self.edad}' \
               f' y mi DNI es {self.dni}'


# instanciar => Llamar a una clase
persona = Persona('Pepito', 85, '7856987')
mi_saludo = persona.saludar('Juanito')
print(mi_saludo)
