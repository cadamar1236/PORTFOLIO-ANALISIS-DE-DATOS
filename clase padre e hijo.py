class Animal:
    def __init__(self, nombre,  tamaño, país):
    self.nombre = nombre
    self.tamaño = tamaño
    self.país = país

class Carnívoro(Animal):
    def comer_carne():
        // alimentación carnívora

class Herbívoro(Animal):
    def comer_vegetal()
        // se alimenta de plantas

## Otro ejemplo
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        print("Haciendo algún sonido ")


class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        # Llamamos al constructor de la clase padre usando super()
        super().__init__(nombre, edad)
        self.raza = raza

    def hacer_sonido(self):
        print("¡Guau! ¡Guau!")

    def mostrar_info(self):
        # Método adicional específico de la clase Perro
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Raza: {self.raza}")


# Crear una instancia de la clase Perro
mi_perro = Perro(nombre="Thor", edad=3, raza="Labrador")

# Acceder al método de la clase padre desde la clase hija
mi_perro.hacer_sonido()

# Acceder al método específico de la clase Perro
mi_perro.mostrar_info()


