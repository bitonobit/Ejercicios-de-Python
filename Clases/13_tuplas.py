
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

multiplica=t3*2         #Multiplica la tupla por dos (la repite) y la guarda en multiplica como si hubiese hecho t3 + t3
t3.count("c")     #Busca cuantas c hay en la tupla, 1
t3.index("c")     #Busca la primera ocurrencia de c y devuelve la posición
