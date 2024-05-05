class Autor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def eliminar_libro(self, libro):
        if libro in self.libros:
            self.libros.remove(libro)
            print(f"Libro '{libro}' eliminado del autor '{self.nombre}'.")
        else:
            print(f"El libro '{libro}' no está en la lista de libros del autor '{self.nombre}'.")

    def __str__(self):
        if self.libros:
            return f"{self.nombre} - Libros: {', '.join(self.libros)}"
        else:
            return self.nombre


class ListaAutores:
    def __init__(self):
        self.autores = []

    def agregar_autor(self, nombre):
        self.autores.append(Autor(nombre))

    def agregar_libros_autor(self, posicion, libros):
        try:
            autor = self.autores[posicion]
            for libro in libros:
                autor.agregar_libro(libro)
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

    def modificar_autor(self, posicion, nuevo_nombre):
        try:
            self.autores[posicion].nombre = nuevo_nombre
            print("Autor modificado correctamente.")
        except IndexError:
            print("La posición ingresada no es válida.")

    def eliminar_libro_autor(self, posicion_autor, libro):
        try:
            autor = self.autores[posicion_autor]
            autor.eliminar_libro(libro)
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
        print("5. Modificar un autor")
        print("6. Eliminar libros de un autor")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre_autor = input("Ingrese el nombre del nuevo autor: ")
            lista_autores.agregar_autor(nombre_autor)
        elif opcion == '2':
            lista_autores.mostrar_autores()
            try:
                posicion = int(input("Ingrese la posición del autor al que desea agregar libros: ")) - 1
                libros = input("Ingrese la lista de libros separados por coma: ").split(',')
                lista_autores.agregar_libros_autor(posicion, libros)
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
                posicion = int(input("Ingrese la posición del autor que desea modificar: ")) - 1
                nuevo_nombre = input("Ingrese el nuevo nombre del autor: ")
                lista_autores.modificar_autor(posicion, nuevo_nombre)
            except ValueError:
                print("Por favor ingrese un número válido.")
        elif opcion == '6':
            lista_autores.mostrar_autores()
            try:
                posicion_autor = int(input("Ingrese la posición del autor del que desea eliminar libros: ")) - 1
                libros_eliminar = input("Ingrese la lista de libros a eliminar separados por coma: ").split(',')
                for libro in libros_eliminar:
                    lista_autores.eliminar_libro_autor(posicion_autor, libro)
            except ValueError:
                print("Por favor ingrese un número válido.")
        elif opcion == '7':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor seleccione una opción válida.")


if __name__ == "__main__":
    main()
