class GestionPelículas:
    def __init__(self):
        self.lista_peliculas = []

    def añadir_peliculas(self, pelicula):
        if pelicula not in self.lista_peliculas:
            self.lista_peliculas.append(pelicula)
            print(f'{pelicula}añadida a la lista')
        else:
            print(f'{pelicula}ya esta en la lista')

    def borrar_pelicula(self, pelicula):
        if pelicula in self.lista_peliculas:
            self.lista_peliculas.remove(pelicula)
            print(f'{pelicula}eliminada de la lista')
        else:
            print(f'{pelicula} no esta en la lista')

    def mostrar_lista(self):
            if not self.lista_peliculas:
                print('La lista de películas está vacía.')
            else:
                print('Lista de películas:')
                for pelicula in self.lista_peliculas:
                    print(pelicula)

    def buscar_pelicula(self, pelicula):
        if pelicula in self.lista_peliculas:
            print(f'La pelicula {pelicula} está en la lista')
        else:
            print(f'La película {pelicula} no está en la lista')


def main():
    gestion_peliculas =  GestionPelículas()

    while True:
        print('\nMenú:')
        print('1. Añadir Película')
        print('2. Eliminar Película')
        print('3. Mostrar Lista de Películas')
        print('4. Buscar Película')
        print('5. Salir')
        opcion = input('Selecciona una opción del 1 al 5: ')

        if opcion == '1':
            pelicula_nueva = input('Ingrese el nombre de la película a añadir: ')
            gestion_peliculas.añadir_peliculas(pelicula_nueva)
        elif opcion == '2':
            pelicula_eliminar = input('Ingrese la película que desee eliminar: ')
            gestion_peliculas.borrar_pelicula(pelicula_eliminar)
        elif opcion == '3':
            gestion_peliculas.mostrar_lista()
        elif opcion == '4':
            pelicula_buscar = imput('Ingrese la película que desea buscar:')
            gestion_peliculas.buscar_pelicula(pelicula_buscar)
        elif opcion == '5':
            print('Saliendo del programa. ¡Hasta luego!')
            break
        else:
            print('Opción no válida. Por favor, seleccione una opción válida.')

if __name__ == "__main__":
    main()
