def minimum(a,b):
    if a<=b:    
        return a
    else:
        return b
# print(minimum(2,4))

def palindromo(frase):
    palabras= frase.split( )
    pal=' '.join(reversed(palabras))
    return pal

# if __name__=="__main__":
#     print(palindromo(input("Dime la frase: ")))

# Realizar la suma de los elementos de una tupla
tupla=(7,8,9,1,19,7)
print(f"Los valores a sumar son: {tupla}")
def sumar(tupla):
    if len(tupla)==1:
        return tupla[0]
    else:
        return tupla[0] + sumar(tupla[1:])
print("La suma es:", sumar(tupla))

# 5. Escriba un código que desordene al azar una lista.
from random import shuffle
x=['Candy','Bitonobit', 'Háblame']
shuffle(x)  #No puedo meterla en el print porque devuelve None
print(x)

# 6. Escriba un código que pueda contar todas las palabras mayúsculas de un archivo. 
# Al usar with el archivo se cierra solo al terminar
cont=0
with open('archivo.txt', 'r') as archivo:
    texto=archivo.read()
for x in texto:
    if x.isupper():
        cont+=1
print(cont)
# 7. ¿Si la lista 1 es [4, 6, 8, 1, 0, 3], que sería la lista 1 [-1]?
lista1=[1,2,3,4,5]
print(lista1[-1])
# Para copiar listas ten en cuenta que si las igualas solo haces una referencia a la lista que copias y los cambios afectaran a las dos variables
lista2=list(lista1) # Permite copiar una lista
lista2[2]=0
print(lista2)

# 8. Escriba un programa para producir la serie Fibonacci en Python.
def fibo(terminos):
    if n>=1:
        t1=0
        t2=1
        serie=f"Serie de Ficonacci de {terminos}: {t1}"
        for i in range(0,terminos-1):
            serie+=f" , {t2}"   # Concatenar el nuevo término
            # Calcular el nuevo término
            aux=t1
            t1=t2
            t2=aux+t1
    else:
        serie="El valor debe introducido debe ser mayor que 0"
    return serie
# n=int(input("¿Cuántos términos quieres calcular?: "))
# print(fibo(n))

# 9. Escriba un programa en Python para comprobar si un número es primo
def primo(n):
    if n>1:         #Validamos que sea mayor que 1
        cont=2      # Iniciamos el contador
        for i in range(2,(n//2+1)):      # Buscamos divisores
            if n%i==0:
                 cont+=1             # Contamos los divisores que encontremos
        # Finaliza el bucle for
        if cont>2:
            return f"El número {n} NO es un número primo"
        else:
             return f"El número {n} es un número primo"
    else:
        return "El valor introducido debe ser mayor que 1" 
#  Llamamos a la funcion
n=int(input("Intrduce un número mayor que 1: "))
print(primo(n))

# 10. Escribir un programa en Python para comprobar si un número es capicúa. Es decir, si se lee igual de derecha a
# izquierda que de izquierda a derecha
def capicua(n):
    palabras= n.split( )
    res=''.join(reversed(n))
    if res==n:
        return f"El numero {n} es un número capicúa"
    else:
        return f"El numero {n} NO es un número capicúa"

n=input("Intrduce un número de varias cifras: ")
print(capicua(n))

# 11. Escribir un algoritmo de ordenación para un conjunto de datos numéricos en Python.
lista=[5, 10, 6]
lista.sort()
print(lista)