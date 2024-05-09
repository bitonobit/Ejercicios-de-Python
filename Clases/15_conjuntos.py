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
s8=s1.difference(s2)     #Hace lo mismo que la anterior
#s10.diference_update(s2) #Hace lo mismo que la anterior
s9= s8.symmetric_difference(s7) #Mantiene sólo los elemntos que no esté en ambos conjuntos
s9= s8^s7               #Hace lo mismo que la anterior
s8.symmetric_difference_update(s7) #Mantiene sólo los elemntos que no esté en ambos conjuntos modificando el original
s10=s9.copy()           #Copia el conjunto
x = s10.isdisjoint(s9)  #Devuelve True si no hay ningún elemento del conjunto s10 presente en el conjunto s9
x = s10.issubset(s9)    #Devuelve True si todos los elementos del conjunto s10 están presente en el conjunto s9