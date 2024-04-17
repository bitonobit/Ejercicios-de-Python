# Python es: interpretado y CaseSensitive
#Para saber si Python esta instlado teclea desde el cmd: C:\Users\Your Name>python --version 
# La forma de ejecutar un archivo Python es así en la línea de comando: C:\Users\Your Name>python nombreArchivo.py
# Consultar la versión de python desde el editor
import sys
print(sys.version)
print("Hola Mundo!") #Imprime una salida
# Python usa sangría para indicar un bloque de código.
if 3 > 2:
  print("Tres es mayor que dos!")
  # Tienes que usar la misma cantidad de espacios en el mismo bloque de código, sino, Python te dará un error

#Python no tiene ningún comando para declarar una variable, las variables se crean cuando le asignas un valor:
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
# es lo mismo que
x = 'Candy'

#Python te permite asignar valores a múltiples variables en una línea:
x, y, z = "Bitonobit", "Python", "Candy"
print(x)
print(y)
print(z)

#Si tiene una colección de valores en una lista, tupla, etc. Python le permite extraer los valores en variables. A esto se le llama desempacar .
nombres = ["Ana", "Pedro", "Juan"]
x, y, z = nombres
print(x)
print(y)
print(z)
# También podría ser:
print(x, y, z)
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
# Escapa un caracter \'
# Salto de línea \n
# Retorno del carro \r
# Tabulador \t
# Retroceso \b
# \f
# Permite escribir en octal\ooo.            Ejemplo: txt = "\110\145\154\154\157"
# Permite escribir en hexadecimal \xhh.     Ejemplo: txt = "\x48\x65\x6c\x6c\x6f"

# **********************************
#      Más funciones de cadena
# **********************************
# Método                	Description
#===================================================================================================================
# capitalize()	            Converts the first character to upper case
# casefold()	            Converts string into lower case
# center()	                Returns a centered string
# count()	                Returns the number of times a specified value occurs in a string
# encode()	                Returns an encoded version of the string
# endswith()	            Returns true if the string ends with the specified value
# expandtabs()	            Sets the tab size of the string
# find()	                Searches the string for a specified value and returns the position of where it was found
# format()	                Formats specified values in a string
# format_map()	            Formats specified values in a string
# index()	                Searches the string for a specified value and returns the position of where it was found
# isalnum()	                Returns True if all characters in the string are alphanumeric
# isalpha()	                Returns True if all characters in the string are in the alphabet
# isascii()	                Returns True if all characters in the string are ascii characters
# isdecimal()	            Returns True if all characters in the string are decimals
# isdigit()	                Returns True if all characters in the string are digits
# isidentifier()	        Returns True if the string is an identifier
# islower()	                Returns True if all characters in the string are lower case
# isnumeric()	            Returns True if all characters in the string are numeric
# isprintable()	            Returns True if all characters in the string are printable
# isspace()	                Returns True if all characters in the string are whitespaces
# istitle()	                Returns True if the string follows the rules of a title
# isupper()	                Returns True if all characters in the string are upper case
# join()	                Joins the elements of an iterable to the end of the string
# ljust()	                Returns a left justified version of the string
# lower()	                Converts a string into lower case
# lstrip()	                Returns a left trim version of the string
# maketrans()	            Returns a translation table to be used in translations
# partition()	            Returns a tuple where the string is parted into three parts
# replace()	                Returns a string where a specified value is replaced with a specified value
# rfind()	                Searches the string for a specified value and returns the last position of where it was found
# rindex()	                Searches the string for a specified value and returns the last position of where it was found
# rjust()	                Returns a right justified version of the string
# rpartition()	            Returns a tuple where the string is parted into three parts
# rsplit()	                Splits the string at the specified separator, and returns a list
# rstrip()	                Returns a right trim version of the string
# split()	                Splits the string at the specified separator, and returns a list
# splitlines()	            Splits the string at line breaks and returns a list
# startswith()	            Returns true if the string starts with the specified value
# strip()	                Returns a trimmed version of the string
# swapcase()	            Swaps cases, lower case becomes upper case and vice versa
# title()	                Converts the first character of each word to upper case
# translate()	            Returns a translated string
# upper()	                Converts a string into upper case
# zfill()	                Fills the string with a specified number of 0 values at the beginning


# *******************************************************************************
#                           Funciones de lógicas
# *******************************************************************************
# La bool()función le permite evaluar cualquier valor y darle Trueo False a cambio
print(bool(15))             # Devuelve True
print(bool(0))              # Devuelve False
bool(["A", "B", "C"])       # Devuelve True
bool([])                    # Devuelve False




#Bucles a través de una cadena
for x in "Bitonobit":
  print(x)
