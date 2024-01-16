class GestionPelículas:
    def __init__(self):
        self.peliculas = {}

    def añadir_peliculas(self, nombre, director, año, presupuesto):
        if nombre not in self.peliculas:
            self.peliculas[nombre] = {'Director': director, 'Año': año, 'Presupuesto': presupuesto}
            print(f'{nombre}añadida a la lista')
        else:
            print(f'{nombre}ya esta en la lista')

    def borrar_pelicula(self, nombre):
        if nombre in self.peliculas:
            self.peliculas.remove(nombre)
            print(f'{nombre}eliminada de la lista')
        else:
            print(f'{nombre} no esta en la lista')

    def mostrar_lista(self):
            if not self.peliculas:
                print('La lista de películas está vacía.')
            else:
                print('Lista de películas:')
                for nombre, info in self.peliculas.items():
                    print(f"{nombre} - Director: {info['Director']}, Año: {info['Año']}, Presupuesto: {info['Presupuesto']}")
                          
    def modificar_pelicula(self, nombre):
        if nombre in self.peliculas:
            director = input('Nuevo director: ')
            año = input('Nuevo año: ')
            presupuesto = input('Nuevo presupuesto: ')
            self.peliculas[nombre] = {'Director': director, 'Año': año, 'Presupuesto': presupuesto}
            print(f'Información de {nombre} actualizada.')
        else:
            print(f'La película {nombre} no está en la lista.')

    def buscar_pelicula(self, nombre):
        if nombre in self.peliculas:
            print(f'La pelicula {nombre} está en la lista')
        else:
            print(f'La película {nombre} no está en la lista')

    def modificar_presupuesto(self, porcentaje):
        for nombre, info in self.peliculas.items():
            presupuesto_actual = info['Presupuesto']
            try:
                aumento = float(presupuesto_actual) * (1 + float(porcentaje) / 100)
                nuevo_presupuesto = presupuesto_actual + aumento if aumento > 0 else presupuesto_actual
                self.peliculas[nombre]['Presupuesto'] = nuevo_presupuesto
            except ValueError:
                print(f'Error: Valor no válido para el porcentaje en la película {nombre}.')


def main():
    gestion_peliculas =  GestionPelículas()

    while True:
        print('\nMenú:')
        print('1. Añadir Película')
        print('2. Eliminar Película')
        print('3. Mostrar Lista de Películas')
        print('4. Modificar película')
        print('5. Buscar Película')
        print('6. Modificar presupuesto')
        print('7. Salir')
        opcion = input('Selecciona una opción del 1 al 7: ')

        if opcion == '1':
            nombre = input('Ingrese el nombre de la película a añadir: ')
            director = input(' Ingrese el nombre del director: ')
            año = input( 'Ingrese el año de la película: ')
            presupuesto = input( ' Ingrese el presupuesto de la película: ')
            gestion_peliculas.añadir_peliculas(nombre, director, año, presupuesto)
        elif opcion == '2':
            pelicula_eliminar = input('Ingrese la película que desee eliminar: ')
            gestion_peliculas.borrar_pelicula(pelicula_eliminar)
        elif opcion == '3':
            gestion_peliculas.mostrar_lista()
        elif opcion == '4':
            nombre = input('Ingrese el nombre de la película a modificar: ')
            gestion_peliculas.modificar_pelicula(nombre)
            
        elif opcion == '5':
            pelicula_buscar = input('Ingrese la película que desea buscar:')
            gestion_peliculas.buscar_pelicula(pelicula_buscar)
        elif opcion == '6':
            porcentaje = input('Ingrese nuevo presupuesto')
            gestion_peliculas.modificar_presupuesto( porcentaje)
        elif opcion == '7':
            print('Saliendo del programa. ¡Hasta luego!')
            break
        else:
            print('Opción no válida. Por favor, seleccione una opción válida.')
if __name__ == "__main__":
    main()