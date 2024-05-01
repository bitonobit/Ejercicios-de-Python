
# **************************************************************************************
#                        Clasees y Objetos
# Python es un lenguaje de programación orientado a objetos.
# Casi todo en Python es un objeto, con sus propiedades y métodos.
# Una clase es como un constructor de objetos o una "plantilla" para crear objetos.
# **************************************************************************************
class MiClase:      #Crea una clase
  x = 5

p1 = MiClase()      #Crea un objeto de la clase MiClase
print(p1.x)

# Todas las clases tienen una función llamada __init__(), que siempre se ejecuta cuando se inicia la clase.

class Persona:
  def __init__(self, nombre, apellidos, edad):  
    self.nombre = nombre
    self.apellidos = apellidos
    self.edad = edad
    #La __init__()función se llama automáticamente cada vez que se utiliza la clase para crear un nuevo objeto.
p1 = Persona("Candy", "González", 51)

print(p1.nombre, p1.apellidos, p1.edad)

# La función __str__() controla lo que se debe devolver cuando el objeto de clase se representa como una cadena.

print(p1)     # Si la función __str__() no está configurada, se devuelve la representación de cadena del objeto, algo como: <__main__.Person object at 0x15039e602100>

# self es una referencia a la instancia actual de la clase y se utiliza para acceder a variables que pertenecen a la clase.
class Alumno:
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

  def __str__(self):
    return f"{self.nombre}({self.edad})"
  #Métodos
  def saludar(self):        
    print("Hola pepsicola!! Bienvenida " + self.nombre)

p1 = Alumno("Candy", 26)

print(p1)

# Modificar una propiedad
p1.edad=51
del p1.edad       #Elimina la propiedad edad
del p1            #Elimina el objeto p1

# La herencia nos permite definir una clase que hereda todos los métodos y propiedades de otra clase.
# La clase principal es la clase de la que se hereda, también llamada clase base o padre.
# La clase hija es la clase que hereda de otra clase, también llamada clase derivada.
class Estudiante(Persona):
  pass      #Se usa cuando no quieres agregar nada más a la clase

# Ahora la clase estudiante hereda todo de la clase persona
p1=Estudiante("Ana", 20)
print(p1.nombre)


#Cuando agregamos __init__(), la clase ya no heredará la función __init__()  de la clase principal. Para mantener la herencia  debemos agregar una llamada a la función principal __init__():
class Profesora(Persona):
  def __init__(self, nombre, apellidos, edad):     
    Persona.__init__(self, nombre, apellidos, edad)    #Llamada a la clase principal para mantener la herencia


class Administrativo(Persona):
  def __init__(self, nombre, apellidos, edad, dni):
    super().__init__(nombre, apellidos, edad)          #Hace que se hereden todas las propiedades y métodos de la clase padre
    self.dni=dni                                       #Agregamos una prpopiedad aquí y en los parámetros de la función inint
  #Métodos
  def nombreCompleto(self):
    print("Bienvenido ", self.apellidos, ", ", self.nombre)        
    #PD: Si agregamos un método en la clase secundaria con el mismo nombre que uno de la clase principal, se anulará la herencia del método principal.

p2=Administrativo("Andres", "Glez", 25, "12345678Z")
p2.nombreCompleto()

# Un iterador es un objeto que contiene un número contable de valores. Es un objeto que implementa el protocolo del iterador, que consta de los métodos __iter__() y __next__().

# Las listas, tuplas, diccionarios y conjuntos son todos objetos iterables. Son contenedores iterables de los que puede obtener un iterador.

# Todos estos objetos tienen un iter()método que se utiliza para obtener un iterador:
tuplaN = ("A", "B", "C")
iterable = iter(tuplaN)
print(next(iterable))
print(next(iterable))
print(next(iterable))

# Crear un iterador que devuelva números, comenzando con 1, y cada secuencia aumentará en uno (devolviendo 1,2,3,4,5, etc.). Para crear un objeto/clase como iterador, debe implementar los métodos __iter__()y __next__()su objeto.
class MiIterador:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

miClase = MiIterador()
miIter = iter(miClase)

print(next(miIter))
print(next(miIter))
print(next(miIter))
print(next(miIter))
print(next(miIter))

# Polimorfismo: El polimorfismo se usa a menudo en métodos de clase, donde podemos tener varias clases con el mismo nombre de método.
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):     #mismo nombre de método, diferentes acciones
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):     
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

for x in (car1, boat1, plane1):
  x.move()

