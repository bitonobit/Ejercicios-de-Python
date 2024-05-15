#*******************************************************************************
#  Libros
#*******************************************************************************
class Libro:
    def __init__(self, titulo, genero, num_paginas):
        self.titulo = titulo
        self.genero = genero
        self.num_paginas = int(num_paginas)

    def __str__(self):
        return f"Título: {self.titulo}\nGénero: {self.genero}\nNúmero de páginas: {self.num_paginas}"
    
l=Libro("Cien años de soledad", "Novela", "450" )
