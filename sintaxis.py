# Python es: interpretado y CaseSensitive
#Para saber si Python esta instlado teclea desde el cmd: C:\Users\Your Name>python --version 
# La forma de ejecutar un archivo Python es así en la línea de comando: C:\Users\Your Name>python nombreArchivo.py

import sys
print(sys.version)    # Consultar la versión de python desde el editor
# Entrada y salida 
print("Hola Mundo!")          # Imprime una salida
input("Dime tu nombre: ")     # Te pide una entrada, drá un tipo texto

# Python usa sangría para indicar un bloque de código.
if 3 > 2:
  print("Tres es mayor que dos!")
  # Tienes que usar la misma cantidad de espacios en el mismo bloque de código, sino, Python te dará un error

# Python no tiene ningún comando para declarar una variable, las variables se crean cuando le asignas un valor:
x = 5
y = "Candy González"

"""Comentarios
multilínea"""

'''
También sirven
las comillas
simples
'''
# No es necesario declarar las variables con ningún tipo en particular e incluso pueden cambiar de tipo después de haberlas configurado.
x = "Candy"
# Es lo mismo que
x = 'Candy'

#Python te permite asignar valores a múltiples variables en una línea:
x, y, z = "Bitonobit", "Python", "Candy"
print(x)
print(y)
print(z)
# O podría ser:
print(x + y + z)

#Las variables que se crean fuera de una función son globales y no se ven en la función a menos que uses global
def saluda():
  global x      #Convierte a x en una variable global
  x = "hola que tal"

saluda()
print("Candy, " + x)

#**********************************************************************************************
#Números
#========================================================================================
x = 1       # int -  entero, positivo o negativo, sin decimales, de longitud ilimitada
y = 2.8     # float -  número, positivo o negativo, que contiene uno o más decimales
x = 35e3    # float también
y = 12E4
z = -87.7e100
z = 1j   # complex - Los números complejos se escriben con una "j" como parte imaginaria

#Cadenas de caracteres
# ========================================================================================
a="Candy"   # str - Cedena de caracteres
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)    # Muestra los saltos de línea

#Las cadenas son arrays
print(a[0])     #muestra la L

# *******************************************************
#  Otros Tipos
# *******************************************************
x = ["apple", "banana", "cherry"]   # Una lista - list
x = ("apple", "banana", "cherry")   # Una tupla - tuple
x = range(6)                        # Un rango - range
x = {"name" : "John", "age" : 36}   # dict  
x = {"apple", "banana", "cherry"}   # set
x = frozenset({"apple", "banana", "cherry"}) # frozenset
x = True                        #bool
x = b"Hello"                    #bytes
x = bytearray(5)                #bytearray
x = memoryview(bytes(5))        #memoryview
x = None                        #NoneType

# **********************************
#   Conversión de tipo de datos
# **********************************
x = str(3)      # x será '3'
y = int(3)      # y será 3
z = float(3)    # z será 3.0
print(type(x))  # Para obtener el tipo de una variable

# **********************************
#   Anidar comillas
# **********************************
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# *******************************************************************************
#                         Operadores Aritméticos
# *******************************************************************************
# Operator	    Name	           Ejemplo
#   +	        Suma       	        x + y	
#   -	        Resta	            x - y	
#   *	        Multiplicación	    x * y	
#   /	        División	        x / y	
#   %	        Módulo	            x % y	
#   **          Exponenciación	    x ** y	
#   //          Floor división	    x // y

# *******************************************************************************
#                         Operadores de asignación
# *******************************************************************************
# Operador	    Ejemplo	    Igual a	 
#   =	        x = 5	    x = 5	
#   +=	        x += 3	    x = x + 3	
#   -=	        x -= 3	    x = x - 3	
#   *=	        x *= 3	    x = x * 3	
#   /=	        x /= 3	    x = x / 3	
#   %=	        x %= 3	    x = x % 3	
#   //= 	    x //= 3	    x = x // 3	
#   **= 	    x **= 3	    x = x ** 3	
#   &=	        x &= 3	    x = x & 3	
#   |=	        x |= 3	    x = x | 3	
#   ^=	        x ^= 3	    x = x ^ 3	
#   >>= 	    x >>= 3	    x = x >> 3	
#   <<= 	    x <<= 3	    x = x << 3

# **********************************************
#     Operadores de comparación
# **********************************************
# Operador	    Nombre	            Ejemplo	 
#   ==      	Igual	            x == y	
#   !=      	Diferente	        x != y	
#   >	        Mayor que	        x > y	
#   <	        Menor que	        x < y	
#   >=      	Mayor o igua que	x >= y	
#   <=      	Menor o igua que	x <= y

# *******************************************************************************
#                         Operadores de lógicos
# *******************************************************************************
# Operador	    Descripción	                                    Ejemplo
#   and 	    Retorna verdad si ambos son verdad      	x < 5 and  x < 10	
#   or	        Retorna verdad si uno es verdad         	x < 5 or x < 4	
#   not	        Negación                                	not(x < 5 and x < 10)

# *******************************************************************************
#                         Operadores de identidad
# *******************************************************************************
# Operador	    Descripción	                                        Ejemplo
#   is 	        Devuelve verdad si ambas son el mismo objeto         x is y	
#   is not	    Devuelve verdad si ambas NO son el mismo objeto      x is not y	

# **************************************************************************************************
#                         Operadores de membresía
# **************************************************************************************************
#   Los operadores de membresía se utilizan para probar si una secuencia se presenta en un objeto:

# Operador	    Descripción	                            Ejemplo
#   in 	        Devuelve True si está presente	        x in y	
#   not in	    Devuelve True si NO está presente     x not in y	

# ********************************************************************************************************
#                         Operadores bit a bit 
# ********************************************************************************************************
# Los operadores bit a bit se utilizan para comparar números (binarios):

# Operador  Nombre	                Descripción	                                                Ejemplo
#   & 	    AND	                    Establece cada bit en 1 si ambos bits son 1	                x & y	
#   |	    OR	                    Establece cada bit en 1 si uno de los dos bits es 1	        x | y	
#   ^	    XOR	                    Establece cada bit en 1 si sólo uno de los dos bits es 1	x ^ y	
#   ~	    NOT	                    Invierte todos los bits	                                    ~x	
#   <<	    Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
#   >>	    Signed right shift	    Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

# **********************************************
#            Funciones matemáticas
# **********************************************
# Python no tiene una random() función para crear 
# un número aleatorio, pero Python tiene un módulo 
# integrado llamado random que se puede utilizar para 
# crear números aleatorios:
import random
print(random.randrange(1, 10))


# *******************************************************************************
#                           Funciones de cadenas
# *******************************************************************************
a = "Bitonobit"
print(len(a))       #Longitud de la cadena 9
print(a.upper())    #Mayúsculas
print(a.lower())    #minúsculas

#Para comprobar si una determinada frase o carácter está presente en una cadena, podemos utilizar la palabra clave in
txt = "Programar es fácil y divertido!"
print("fácil" in txt)
print("fácil" not in txt)
# Otra forma
txt = "Programar es fácil y divertido !"
if "divertido" in txt:
  print("Sip, 'divertido' está en la cadena.")

print(txt.strip())  #Elimina los espacios en blanco  
print(txt.replace("f", "súper f"))  #Reemplaza caracteres de la cadena
print(txt.split(" ")) # devuelve ['Programar', ' es', 'facil', 'y', 'divertido']
#Puedes devolver un grupo de caracteres utilizando la sintaxis de segmento.
b = "Programar es fácil y divertido !"
print(b[2:5])
print(b[:5])  #comienza desde cero
print(b[4:])  #comienza desde 4 hasta el final de la cadena
print(b[-5:2])

#Operadores
nombre='Candy'
apellido='González'
nombreCompleto= nombre + ' ' + apellido #Concatenar 
# NO se puede concatenar un cadena y un número, en su lugar se usa f{}
edad = 51
saludo = f"Mi nombre es Candy y tengo {edad} años"
print(saludo)

# Formateando un float
pi=3.1415
res=f"El valor de pi es {pi:.2f}"   #.2f son sólo 2 decimales
print(res)
# Se pueden hacer operaciones matemáticas
res=f"El valor de pi es {10 *5}"
# **********************************
#       Caracteres de escape
# **********************************
print("Muestra \"texto\" entre comillas")   # Escapa un caracter \"
print("Hace un \n salto de línea")          # Salto de línea \n
print("Hace un \r salto de línea")          # Retorno del carro \r
print("Coloca un \r Tabulador en el texto") # Tabulador \t
print("Hace un \b retroceso en el texto")   # Retroceso \b
txt = "\110\145\154\154\157"                # Permite escribir en octal\ooo.
print(txt)
txt = "\x48\x65\x6c\x6c\x6f"                # Permite escribir en hexadecimal \xhh.
print(txt)

# **********************************
#      Más funciones de cadena
# **********************************
# Método            Description
#============================================================================================================
# capitalize()	    Convierte el primer caracter a mayúsculas
# casefold()	      Converts string into lower case
# center()	        Returns a centered string
# count()	          Returns the number of times a specified value occurs in a string
# encode()	        Returns an encoded version of the string
# endswith()	      Returns true if the string ends with the specified value
# expandtabs()	    Sets the tab size of the string
# find()	          Searches the string for a specified value and returns the position of where it was found
# format()	        Formats specified values in a string
# format_map()	    Formats specified values in a string
# index()	          Searches the string for a specified value and returns the position of where it was found
# isalnum()	        Returns True if all characters in the string are alphanumeric
# isalpha()	        Returns True if all characters in the string are in the alphabet
# isascii()	        Returns True if all characters in the string are ascii characters
# isdecimal()	      Returns True if all characters in the string are decimals
# isdigit()	        Returns True if all characters in the string are digits
# isidentifier()	  Returns True if the string is an identifier
# islower()	        Returns True if all characters in the string are lower case
# isnumeric()	      Returns True if all characters in the string are numeric
# isprintable()	    Returns True if all characters in the string are printable
# isspace()	        Returns True if all characters in the string are whitespaces
# istitle()	        Returns True if the string follows the rules of a title
# isupper()	        Returns True if all characters in the string are upper case
# join()	          Joins the elements of an iterable to the end of the string
# ljust()	          Returns a left justified version of the string
# lower()	          Converts a string into lower case
# lstrip()	        Returns a left trim version of the string
# maketrans()	      Returns a translation table to be used in translations
# partition()	      Returns a tuple where the string is parted into three parts
# replace()	        Returns a string where a specified value is replaced with a specified value
# rfind()	          Searches the string for a specified value and returns the last position of where it was found
# rindex()	        Searches the string for a specified value and returns the last position of where it was found
# rjust()	          Returns a right justified version of the string
# rpartition()	    Returns a tuple where the string is parted into three parts
# rsplit()	        Splits the string at the specified separator, and returns a list
# rstrip()	        Returns a right trim version of the string
# split()	          Splits the string at the specified separator, and returns a list
# splitlines()	    Splits the string at line breaks and returns a list
# startswith()	    Returns true if the string starts with the specified value
# strip()	          Returns a trimmed version of the string
# swapcase()	      Swaps cases, lower case becomes upper case and vice versa
# title()	          Converts the first character of each word to upper case
# translate()	      Returns a translated string
# upper()	          Converts a string into upper case
# zfill()	          Fills the string with a specified number of 0 values at the beginning

# *******************************************************************************
#                           Funciones de lógicas
# *******************************************************************************
# La bool()función le permite evaluar cualquier valor y darle Trueo False a cambio
print(bool(15))             # Devuelve True
print(bool(0))              # Devuelve False
bool(["A", "B", "C"])       # Devuelve True
bool([])                    # Devuelve False

# Colecciones de Python (matrices)
# ====================================================================================
# Hay cuatro tipos de datos de recopilación en el lenguaje de programación Python:
# 1. Lista es una colección ordenada y modificable. Permite miembros duplicados.
# 2. Tupla es una colección ordenada e inmutable. Permite miembros duplicados.
# 3. Set es una colección desordenada, inmutable y no indexada. 
# No hay miembros duplicados. Los elementos establecidos no se pueden cambiar,
# pero puedes eliminar y/o agregar elementos cuando quieras
# 4. El diccionario es una colección ordenada (A partir de Pytho 3.7) y modificable. 
# No hay miembros duplicados.

# *******************************************************************************
#                          Listas
# Los elementos de la lista son modificables y permiten valores duplicados.
# *******************************************************************************
lista = ["Candy", "Glez", "Bitonobit"]
# Una lista puede contener diferentes tipos de datos:
lista = [1, True, "Bitonobit"]
var= list(("Candy", "Glez", "Bitonobit")) # Constructor de list debes agregar doble (())
#Si tiene una colección de valores en una lista, tupla, etc. Python le permite extraer los valores en variables.
# A esto se le llama desempacar .
nombres = ["Ana", "Pedro", "Juan"]
x, y, z = nombres
print(x)
print(y)
print(z)
# También podría ser:
print(x, y, z)
a=[1,2,3,4,5,6,7,8,9,10]
print(a[0])     # Muestra el valor en la posición 0 -> 1
print(a[-1])    # Muestra el valor en la última posición -> 5
a[-1]=100       #Cambiar un valor

# Al especificar un rango, el valor de retorno será una nueva lista con los elementos especificados.
print(a[2:5]) #comienza en 2 incluido y termina en 4 porque no incluye el 5
print(a[:5])  #comienza desde cero
print(a[4:])  #comienza desde 4 hasta el final de la cadena
print(a[-5:-2]) 

a[1:3]=["a","b"]  # Cambiar un rango de valores 
print(a)

# Buscar un valor en la lista
if 5 in a:        
  print("Sip, 5 está en la lista")    

# *******************************************************************************
#                         Métodos de Listas
# *******************************************************************************
len(a)                  # Cuenta el número de elementos de la lista
a.insert(2, "x")        # Inserta el caracter x en la posición 2
a.append("y")           # Inserta el caracter x en la última posición
b=[22,44,33,67]
a.extend(b)             # Agregar elementos de otra lsita
d= a + b                # Otra forma de unir dos listas
# El extend()método no tiene que agregar listas , puede agregar cualquier objeto iterable
c=(99,98,97)
a.extend(c)
a.remove(97)            # Remueve un elemento especificado
a.remove("x")           # Remueve la primera aparición de x
a.pop(2)                # Remueve el elemento en la posición 2
a.pop()                 # Remueve el último elemento 
del a[5]                # Remueve el elemento en la posición 5
del a                   # Elimina la lista por completo
a.clear()               # Limpia la lista
a.index(22)             # Devuelve el índice del elemento encontrado
nElementos=a.count("x")    # Cuenta el número de ocurrencias de un elemento
a.sort()                # Ordena una lista ascendentemente
a.sort(reverse = True)  # Ordena una lista descendentemente
b = a.copy()            # Copiar una lista
c = list(b)             # Otra forma de copiar una lista

# Recorrer la lista
for x in a:
  print(x)

# Recorrer un rango de la lista
for x in range(3,5):
  print(x)

#  Crear una lista a partir de otra con una condición. Ejemplo que el nombre contenga una e
alumnos = ["Ana", "Pedro", "Juan", "Rafael", "Alejandro"]
nuevaLista = []

for x in alumnos:
  if "e" in x:
    nuevaLista.append(x)

print(nuevaLista)

# Usando comprensión de lista sería más corto de escribir
otraLista = [x for x in alumnos if "e" in x]
print(otraLista)
# Sintaxis: newlist = [expression for item in iterable if condition == True]

num = [x for x in range(10)]      # Crea una lista con números del 1 al 10
listaMayusculas = [x.upper() for x in alumnos]    # Crea los valores de la nueva lista en mayúsculas

# Condicionar la creación de la lista:
listaCondicionada = [x if x != "Ana" else "Rafael" for x in a]  #Cambia las Ana por Rafael

# *******************************************************************************
#                        Tuplas
# Una tupla es una colección ordenada e inmutable, no se pueden modificar y 
# permiten valores duplicados.
# *******************************************************************************
t=(3,4,2,7,6)
print(len(t))
# Crear una tupla de 1 elemento
t1=(8,)   #La coma es necesaria
t2=tuple((5,"a", 3))  # Crear una tupla usando el constructor
print(t2[1]) # Muestra el elemento "a"
print(t2[-1]) # Muestra el elemento 3, osea el último
print(t2[0:2]) # Muestra el 5 y la a porque no incluye la posición 2
print(t2[:2]) # Muestra desde el principio hasta la posición 1
print(t2[1:]) # Muestra desde la posición 1 hasta el final
if "a" in t2:
  print(" a esta en la tupla")
# Las tuplas son inmutables, así que para cambiar un elemento puedes convertirla en una lista y luego en una tupla otra vez
t3 = ("a", "b", "c")
l1 = list(t3)
l1[1] = "x"     # Cambia el elemento de la posición 1
l1.append("d")  # Agrega un elemento al final
t3 = tuple(l1)
t4=("e",)
t3+=t4          # Tambien agrega un valor o más al final
print(t3)
# No se pueden eliminar elementos de una tupla, a menos que la conviertas en una lista :)
del t4    # Borra la tupla por completo y si tratas de hacer unprint de t4 te da error

#Las tuplas tambien se pueden desempaquetar
(a, b, c, d, e) = t3    # Una variable para cada valor
(a,b, *letras)=t3       # O un asterísco para crear una lista con las que sobran
(a, *x, e)=t3           #Tambien hace una lista, en este caso intermedia

multiplica=t4*2         #Multiplica la tupla por dos (la repite) y la guarda en multiplica como si hubiese hecho t4 + t4
t4.count("c")     #Busca cuantas c hay en la tupla, 1
t4.index("c")     #Busca la primera ocurrencia de c y devuelve la posición

# *******************************************************************************
#                        set
# Un conjunto es una colección desordenada, inmutable * y no indexada. Se pueden
# eliminar y agregar elementos, pero no cambiarlos
# NOOO permiten valores duplicados.
# *******************************************************************************
s1={"a", "b", "c"}      #Los elementos pueden aparecer en un orden diferente cada vez que los usas y no se puede hacer referencia a ellos mediante índice o clave.

# True y 1 serían iguales y los toma como duplicados, False y 0 lo mismo
print(len(s1))    #Longitud

s2 = {"abc", 34, True, 40, "ver"}   #Puede contener distintos tipos de elementos
s3=set((1,2,3))                     #Con el constructor recuerda usar doble (())

# Recorre el conjunto e imprime los valores:
for x in s2:
  print(x)

print("c" in s1)        #Comprueba si c está en s1
print("c" not in s1)    #Comprueba si c NO está en s1
s1.add("d")             #Agrega un elemento
s1.update(s2)           #Agrega un conjunto de elementos a s1, también puede agregar cualquier iterable
s1.remove("b")          #Elimina un elemento, si el elemento no existe en el conjunto dará error
s1.discard("b")         #Elimina un elemento, si el elemento no existe en el conjunto NO dará error
s1.pop()                #Elimina un elemento aleatoriamente
s1.clear()              #Vacía el conjunto
del s1                  #Elimina el conjunto por completo, es decir s1 ya no existe
s1={"a", "b", "c"}
s4=s2.union(s3)         #Unión de conjuntos
s4=s2 | s3              #Unión de conjuntos, da el mismo resultado
s5=s1.union(s2,s3,s4)   #Unión de varios conjuntos
s6=s5.intersection(s1)  #Conserva sólo los valores duplicados, es decir, que estén en ambos conjuntos
s6=s5 & s1              #Da el mismo resultado, pero está limitado a unir sólo conjuntos con conjuntos
s6.intersection_update(s1)  #Hace lo mismo, pero sicambia el conjunto s6
s7= s6-s5               #Devuelve un nuevo conjunto que contendrá solo los elementos del s6 que no están  presentes en s5.
s8=s1.diference(s2)     #Hace lo mismo que la anterior
s8.diference_update(s2) #Hace lo mismo que la anterior
s9= s8.symetric_diference(s7) #Mantiene sólo los elemntos que no esté en ambos conjuntos
s9= s8^s7               #Hace lo mismo que la anterior
s8.symetric_diference_update(s7) #Mantiene sólo los elemntos que no esté en ambos conjuntos modificando el original
s10=s9.copy()           #Copia el conjunto
x = s10.isdisjoint(s9)  #Devuelve True si no hay ningún elemento del conjunto s10 presente en el conjunto s9
x = s10.issubset(s9)    #Devuelve True si todos los elementos del conjunto s10 están presente en el conjunto s9

# **************************************************************************************
#                        Diccionario
# Los diccionarios se utilizan para almacenar valores de datos en pares clave:valor.
# Un diccionario es una colección ordenada*, modificable y que NO permite duplicados.
# Los diccionarios se pueden cambiar, lo que significa que podemos cambiar, agregar o 
# eliminar elementos una vez creado el diccionario.
# Los valores de los elementos del diccionario pueden ser de cualquier tipo de datos
# **************************************************************************************

coche = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(coche)
print(len(coche))   #Longitud
print(type(coche))  #Devuelve el tipo dict

persona=dict(nombre='Candy', Apellido="González", edad=50)
x=persona["nombre"]
y=persona.get("nombre")   #Accede al valor de la propiedad
z=persona.keys()          #Devuelve todas las claves del diccionario

coche["color"]="Blanco" #Agrega una nueva propiedad
x=coche.values()        #Devolverá una lista de todos los valores del diccionario.
y=coche.items()         #Devolverá cada elemento del diccionario, como tuplas en una lista.
if "color" in coche:
  print("Si está")

coche["color"]="Azul"   #Cambia el valor de una propiedad
coche.update("Rojo")    #Cambia el valor de una propiedad, si no existe se crea la propiedad
coche.pop("color")      #Elimina una propiedad
coche.popitem()         #Elimina la última propiedad a partir de la versión 3.7
del coche["year"]       #Elimina la propiedad especificada
del coche               #Elimina todo el diccionario
persona.clear()         #Vacía el diccionario
coche = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in coche:
  print(x)            #Imprime los nombres de las propiedades

for x in coche.keys():
  print(x)            #Imprime los nombres de las propiedades

for x in coche:
  print(coche[x])     #Imprime los valores de las propiedades

for x in coche.values():
  print(x)           #Imprime los valores de las propiedades

for x, y in coche.items():
  print(x, y)           #Imprime las claves y los valores 

d1=coche.copy()     #Hace una copia
d2=dict(d1)         #Tambien hace una copia
# Diciionarios anidados
biblioteca={
  "libro1" : {
              "titulo": "Los renglones torcidos de Dios",
              "autor": "Torcuato Luca de Teno",
              "pag": 512
            },
 "libro2" : {
              "titulo": "El tiempo entre costuras",
              "autor": "María Dueñas",
              "pag": 640
            },            
}

print(biblioteca["libro1"]["autor"])

# *******************************************************************************
#                          Condicionales
# *******************************************************************************
a = 10
b = 20
if b > a:
  print("b es mayor que a")
elif a == b:
  print("a y b son iguales")
else:
  print("a es mayor que b")

if a==0: print("a es igual a 0")    #Si corto
print(a) if a>b else print(b)       #Si sino corto
print("a es mayor") if a > b else print("iguales") if a == b else print("b es mayor") #si con 3 condiciones

# *******************************************************************************
#                          Bucles
# *******************************************************************************

i = 0
while i < 10:
  print(i)
  i = i + 1
#  Se puede usar break y continue igual que en php o js
i = 1
while i < 5:
  print(i)
  i += 1
else:
  print("i no es mayor que 5")        #Se ejecuta una vez cuando la condición ya no es verdadera

# Bucles a través de una cadena
for x in "Bitonobit":
  print(x)

for i in range(len(t3)):
  print(t3[i])            #Recorre la tupla t3

a = ["Carlos", "Ana", "María", "Ana"]
for x in a:
  print(x)
  if x == "Ana":
    continue

for x in range(6):
  print(x)

for x in range(2, 6):
  print(x)

for x in range(1, 30, 3):
  print(x)                #Cuenta del 1 al 30, pero de 3 en 3
else:
  print("Terminé!")

# *******************************************************************************
#                          Funciones
# *******************************************************************************
def miFuncion():
  print("Hola mundo!")

miFuncion()     #Llamada a la función

#Parámetros
def nombreCompleto(fname, lname):
  print(fname+ " " + lname)

def ejemplo1(*parametros):     #agregar *delante del parametro permite recibir una tupla de n elementos
  for x in parametros:        #Se le llama argumentos arbitrarios
    print(x)

def ejemplo2(**param):         #agregar ** delante del parametro permite recibir un diccionario
  for x in param:             #Se le llama argumentos arbitrarios
    print(x)

def ejemplo3(nombre="Candy"):  #Define un parámetro predeterminado, asi puedes llamar a la función sin argumentos
    print(nombre)

ejemplo3()


# Una función lambda es una pequeña función anónima. Una función lambda puede tomar cualquier número de argumentos, pero solo puede tener una expresión.Sintaxis: lambda arguments : expression

x = lambda a: a + 10      #Agregue 10 al argumento ay devuelva el resultado
print(x(5))

x = lambda a, b : a * b   #Multiplica argumento apor argumento by devuelve el resultado:
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# El poder de lambda se muestra mejor cuando los usa como una función anónima dentro de otra función.
def mifunc(n):
  return lambda a : a * n


def mifunc2(n):
  return lambda a : a * n

doble = mifunc2(2)
print(doble(10))    #Devolverá un 20 


# Python no tiene array de forma nativa hay que usar listas o importar una librería como NumPy

# https://www.w3schools.com/python/numpy/default.asp












#   Personalizar la función de clasificación https://www.w3schools.com/python/python_lists_sort.asp
# También puede personalizar su propia función utilizando el argumento de palabra clave .key = function

# La función devolverá un número que se utilizará para ordenar la lista (el número más bajo primero):

# Ejemplo
# Ordena la lista según lo cerca que esté el número de 50:

# def myfunc(n):
#   return abs(n - 50)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)