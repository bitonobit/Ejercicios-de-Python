# ******************************************************************************
# ** Crea una biblioteca con autores y libros  que permita: 
# **    1. Agregar nuevo autor
# **    2. Agregar lista de libros a un autor
# **    3. Mostrar todos los autores con sus libros
# **    4. Eliminar un autor 
# **    5. Eliminar libros de un autor 
# ******************************************************************************
class Libro:
    def __init__(self, titulo, genero, num_paginas):
        self.titulo = titulo
        self.genero = genero
        self.num_paginas = int(num_paginas)

    def __str__(self):
        return f"Título: {self.titulo}\n  - Género: {self.genero}\n  - Número de páginas: {self.num_paginas}"
    
#*******************************************************************************
#  Autor
#*******************************************************************************
class Autor:
    def __init__(self, nombre, apellidos, nacionalidad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.nacionalidad = nacionalidad
        self.libros = []

    def agregar_libro(self, titulo, genero, num_paginas):
        self.libros.append(Libro(titulo, genero, num_paginas))

    def eliminar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                self.libros.remove(libro)
                print(f"Libro '{titulo}' eliminado del autor '{self.nombre} {self.apellidos}'.")
            else:
                print(f"El libro '{titulo}' no está en la lista de libros del autor '{self.nombre} {self.apellidos}'.")

    def __str__(self):
        libros_str = "\n".join([f"  - {libro} \n" for libro in self.libros])
        return f"Autor: {self.nombre} {self.apellidos}\nNacionalidad: {self.nacionalidad}\nLibros:\n{libros_str}"
    
# a=Autor("Gabriel", "García Márquez", "Colombiano")
# a.agregar_libro("Cien años de soledad", "Novela", "450")
# a.agregar_libro("Crónica de una muerte anunciada", "Novela", "410")
# a.agregar_libro("Prueba", "Novela", "40")
# a.eliminar_libro("Prueba")
# print(a)

class ListaAutores:
    def __init__(self):
        self.autores = []

    def agregar_autor(self, nombre, apellidos, nacionalidad):
        self.autores.append(Autor(nombre, apellidos, nacionalidad))

    def agregar_libros_autor(self, posicion, libro):
        try:
            autor = self.autores[posicion]
            # for i in libro:
            titulo, genero, num_paginas = libro
            autor.agregar_libro(titulo, genero, int(num_paginas))
            print("Lista de libros agregada correctamente al autor.")
        except IndexError:
            print("La posición ingresada no es válida.")

    def mostrar_autores(self):
        if not self.autores:
            print("No hay autores en la lista.")
        else:
            for i, autor in enumerate(self.autores):
                print(f"{i+1}. {autor}")

    def eliminar_autor(self, posicion):
        try:
            del self.autores[posicion]
            print("Autor eliminado correctamente.")
        except IndexError:
            print("La posición ingresada no es válida.")

    def eliminar_libro_autor(self, posicion_autor, titulo):
        try:
            autor = self.autores[posicion_autor]
            autor.eliminar_libro(titulo)
        except IndexError:
            print("La posición ingresada no es válida.")


def main():  
    lista_autores = ListaAutores()
    while True:
        print("\n--- Gestor de Autores ---")
        print("1. Agregar nuevo autor")
        print("2. Agregar lista de libros a un autor")
        print("3. Mostrar todos los autores")
        print("4. Eliminar un autor")
        print("5. Eliminar libros de un autor")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del nuevo autor: ")
            apellidos = input("Ingrese los apellidos del nuevo autor: ")
            nacionalidad = input("Ingrese la nacionalidad del nuevo autor: ")
            lista_autores.agregar_autor(nombre, apellidos, nacionalidad)
        elif opcion == '2':
            lista_autores.mostrar_autores()
            try:
                posicion = int(input("Ingrese la posición del autor al que desea agregar libros: ")) - 1
                libros = input("Ingresa los datos del libro 'titulo, genero, número de paginas' separados por coma: ")
                l=libros.split(',')
                lista_autores.agregar_libros_autor(posicion, l)
            except ValueError:
                print("Por favor ingrese un número válido.")
        elif opcion == '3':
            lista_autores.mostrar_autores()
        elif opcion == '4':
            lista_autores.mostrar_autores()
            try:
                posicion = int(input("Ingrese la posición del autor que desea eliminar: ")) - 1
                lista_autores.eliminar_autor(posicion)
            except ValueError:
                print("Por favor ingrese un número válido.")
        elif opcion == '5':
            lista_autores.mostrar_autores()
            try:
                posicion_autor = int(input("Ingrese la posición del autor del que desea eliminar libros: ")) - 1
                titulo = input("Ingrese el título del libro que desea eliminar: ")
                lista_autores.eliminar_libro_autor(posicion_autor, titulo)
            except ValueError:
                print("Por favor ingrese un número válido.")
        elif opcion == '6':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor seleccione una opción válida.")


if __name__ == "__main__":
    main()
