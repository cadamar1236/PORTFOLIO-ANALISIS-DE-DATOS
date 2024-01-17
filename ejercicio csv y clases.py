import csv
from abc import ABC, abstractmethod
from datetime import datetime

class Animal(ABC):
    def __init__(self, nombre, edad, fecha_nacimiento):
        self._nombre = nombre
        self._edad = edad
        self._fecha_nacimiento = fecha_nacimiento
        self._especie = "Desconocida"  # Atributo privado para la especie

    @abstractmethod
    def hacer_sonido(self):
        pass

    def obtener_info_general(self):
        return f"Nombre: {self._nombre}, Edad: {self._edad}, Especie: {self._especie}"

    def obtener_dia_nacimiento(self):
        try:
            fecha_nacimiento_obj = datetime.strptime(self._fecha_nacimiento, "%Y-%m-%d")
            dia_nacimiento = fecha_nacimiento_obj.strftime("%A")
            return dia_nacimiento
        except ValueError:
            return "Error en el formato de fecha"

    @staticmethod
    def obtener_info_general_especie():
        return "Los animales son seres vivos diversos en la Tierra."

    @property
    def nombre(self):
        return self._nombre

    @property
    def edad(self):
        return self._edad

    @property
    def especie(self):
        return self._especie

    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento

class Perro(Animal):
    def __init__(self, nombre, edad, fecha_nacimiento, raza):
        super().__init__(nombre, edad, fecha_nacimiento)
        self._raza = raza
        self._especie = "Perro"  # Específico para la clase Perro

    def hacer_sonido(self):
        print("¡Guau! ¡Guau!")

    def mostrar_info(self):
        print(super().obtener_info_general(), f"Raza: {self._raza}")

# Crear una instancia de la clase Perro
mi_perro = Perro(nombre="Thor", edad=3, fecha_nacimiento="2019-01-15", raza="Labrador")

# Escribir información del perro en un archivo CSV
archivo_csv = "animales.csv"
campos = ["Nombre", "Edad", "Especie", "Raza", "Fecha de Nacimiento", "Día de Nacimiento"]

with open(archivo_csv, mode='a', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=campos)

    # Si el archivo está vacío, escribe los encabezados
    if file.tell() == 0:
        writer.writeheader()

    # Escribir información del perro en el archivo CSV
    writer.writerow({
        "Nombre": mi_perro.nombre,
        "Edad": mi_perro.edad,
        "Especie": mi_perro.especie,
        "Raza": mi_perro._raza,
        "Fecha de Nacimiento": mi_perro.fecha_nacimiento,
        "Día de Nacimiento": mi_perro.obtener_dia_nacimiento()
    })

# Leer información desde el archivo CSV
with open(archivo_csv, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

# Solicitar información de un nuevo animal al usuario
nombre_nuevo = input("Ingrese el nombre del nuevo animal: ")
edad_nueva = input("Ingrese la edad del nuevo animal: ")
fecha_nacimiento_nueva = input("Ingrese la fecha de nacimiento del nuevo animal (formato YYYY-MM-DD): ")
raza_nueva = input("Ingrese la raza del nuevo animal: ")

# Crear una instancia del nuevo animal y agregarlo al archivo CSV
nuevo_animal = Perro(nombre=nombre_nuevo, edad=edad_nueva, fecha_nacimiento=fecha_nacimiento_nueva, raza=raza_nueva)

with open(archivo_csv, mode='a', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=campos)

    # Escribir información del nuevo animal en el archivo CSV
    writer.writerow({
        "Nombre": nuevo_animal.nombre,
        "Edad": nuevo_animal.edad,
        "Especie": nuevo_animal.especie,
        "Raza": nuevo_animal._raza,
        "Fecha de Nacimiento": nuevo_animal.fecha_nacimiento,
        "Día de Nacimiento": nuevo_animal.obtener_dia_nacimiento()
    })

# Mostrar la información actualizada desde el archivo CSV
with open(archivo_csv, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

