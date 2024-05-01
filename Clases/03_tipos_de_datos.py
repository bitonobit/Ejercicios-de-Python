# *******************************************************
#                   Números
# *******************************************************
x = 1       # int -  entero, positivo o negativo, sin decimales, de longitud ilimitada
y = 2.8     # float -  número, positivo o negativo, que contiene uno o más decimales
x = 35e3    # float también
y = 12E4
z = -87.7e100
z = 1j      # complex - Los números complejos se escriben con una "j" como parte imaginaria

# *******************************************************
#                   Cadenas de caracteres
# Las cadenas son listas
# *******************************************************

a="Candy"       # str - Cedena de caracteres
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)        # Muestra los saltos de línea
print(a[0])     # Muestra la L

# *******************************************************
#                   Otros Tipos
# *******************************************************
x = ["apple", "banana", "cherry"]   # Una lista - list
x = ("apple", "banana", "cherry")   # Una tupla - tuple
x = range(6)                        # Un rango - range
x = {"name" : "John", "age" : 36}   # dict  
x = {"apple", "banana", "cherry"}   # set
x = frozenset({"apple", "banana", "cherry"}) # frozenset
x = True                            #bool
x = b"Hello"                        #bytes
x = bytearray(5)                    #bytearray
x = memoryview(bytes(5))            #memoryview
x = None                            #NoneType


# Para verificar el tipo de cualquier objeto en Python, 
# usamos la función type() :
print(type(a))


# **********************************
#   Conversión de tipo de datos
# **********************************
x = str(3)      # x será '3'
y = int(3)      # y será 3
z = float(3)    # z será 3.0
print(type(x))  # Para obtener el tipo de una variable