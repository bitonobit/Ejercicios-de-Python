# ******************************************************************************
# ** Ejercicios de Objetos                                                    **
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
    
a=Autor("Gabriel", "García Márquez", "Colombiano")
a.agregar_libro("Cien años de soledad", "Novela", "450")
a.agregar_libro("Crónica de una muerte anunciada", "Novela", "410")
a.agregar_libro("Prueba", "Novela", "40")
a.eliminar_libro("Prueba")
print(a)