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
coche.update("rojo")    #Cambia el valor de una propiedad, si no existe se crea la propiedad
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
