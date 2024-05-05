# Una expresión regular, o expresión regular, es una secuencia de caracteres que forma un patrón de búsqueda. RegEx se puede utilizar para comprobar si una cadena contiene el patrón de búsqueda especificado.
import re   #importa el módulo
txt = "No puedo cambiar la dirección del viento, pero puedo ajustar las velas para llegar a mi destino"
#Verifica que la cadena empiece por No y termine en destino
x = re.search("^No.*destino$", txt)     

if x:
  print("Lo encontré!")
else:
  print("Lo siento, no hubo éxito")

# El módulo re ofrece un conjunto de funciones 
# que nos permiten buscar una cadena
# 1.La función findall() devuelve una lista que 
# contiene todas las coincidencias, en el orden en que las encuentra.
x = re.findall("ue", txt)
print(x)

# La función search() busca una coincidencia en la cadena 
# y devuelve un objeto Match si la encuentra y None si no es así.
# Si hay más de una coincidencia, solo se devolverá 
# la primera aparición de la coincidencia:
x = re.search("\s", txt)
print("El primer espacio en blanco está en la posición:", x.start()) 

# La función split() devuelve una lista,
# donde la cadena se ha dividido en cada coincidencia:
x = re.split("\s", txt) #Divide en cada espacio
print(x)

# Puedes controlar el número de apariciones 
# especificando el parámetro maxsplit:
x = re.split("\s", txt, 1) #Separa la primera palabra en la posición 0 y el resto de la cadena en la posición 1
print(x)

# La función sub() reemplaza las coincidencias con el texto de tu elección
x = re.sub("\s", "-", txt)
print(x)
# Se puede indicar el número de reemplazos
x = re.sub("\s", "9", txt, 2)
print(x)

# Objeto coincidente
# Un objeto Match es un objeto que contiene información sobre la búsqueda y el resultado.
# El objeto Match tiene propiedades y métodos utilizados para recuperar información sobre la búsqueda y el resultado:
# .span()devuelve una tupla que contiene las posiciones inicial y final de la coincidencia.
# .stringdevuelve la cadena pasada a la función
# .group()devuelve la parte de la cadena donde hubo una coincidencia
txt = "Cuando los Sapos canten"
x = re.search(r"\bS\w+", txt)
print(x.span())
print(x.string)
print(x.group())

