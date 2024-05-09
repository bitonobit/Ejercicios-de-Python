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

def ejemplo1(*parametros):      #Agregar *delante del parametro permite recibir una tupla de n elementos
  for x in parametros:          #Se le llama argumentos arbitrarios
    print(x)

def ejemplo2(**param):          #Agregar ** delante del parametro permite recibir un diccionario
  for x in param:               #Se le llama argumentos arbitrarios
    print(x)

def ejemplo3(nombre="Candy"):   #Define un parámetro predeterminado, asi puedes llamar a la función sin argumentos
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

