
# *******************************************************************************
#                          Funciones
# *******************************************************************************
def miFuncion():
  print("Hola mundo!")  #Cuerpo de la función

miFuncion()             #Llamada a la función

def suma():
  #Función que suma dos números
  x=int(input("Introduce el primer número:"))
  y=int(input("Introduce el segundo número:"))
  res=x+y
  return res 

suma()

# Parámetros
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


# Una función lambda es una pequeña función anónima. Una función lambda puede tomar cualquier número de argumentos, pero solo puede tener una expresión. Sintaxis: lambda arguments : expression

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

# Ámbito de las variables
#Las variables que se crean fuera de una función son globales y no se ven en la función a menos que uses global
def saluda():
  global x      #Convierte a x en una variable global
  x = "hola que tal"

saluda()
print("Candy, " + x)


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


