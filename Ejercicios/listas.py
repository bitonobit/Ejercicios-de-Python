# 1. En la lista1 es [4, 6, 8, 1, 0, 3], imprime el último elemento de la lista
lista1=[1,2,3,4,5]
print(lista1[-1])

# Para copiar listas ten en cuenta que si las igualas solo haces una referencia a la lista que copias y los cambios afectaran a las dos variables
#2. Copia la lista1 en otra variable y muestra los resultados
lista2=list(lista1)     # Permite copiar una lista
lista2[2]=0
print("\n--- Listas ---")
print(lista1)
print(lista2)

# 5. Escribe un código que desordene al azar una lista.
from random import shuffle
x=['Candy','Bitonobit', 'Háblame']
shuffle(x)  #No puedo meterla en el print porque devuelve None
print(x)

# 2. Pedir por consola los elementos de una lista y realizar la suma de los mismos
def sumar(lista):
    if len(lista)==0:
        return "La lista está vacía"
    elif len(lista)==1:
        return lista[0]
    else:
        return lista[0] + sumar(lista[1:])
    
def pedirLista():
    cadena=input("Introduce los números de la lista separados por comas:")
    aux=cadena.split(",")
    l=[]
    for x in aux:
        l.append(int(x))
    print(f"Los valores a sumar son: {l}")
    print("La suma es:", sumar(l))

pedirLista()