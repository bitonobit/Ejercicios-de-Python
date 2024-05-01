# Escribir un programa en Python para 
# comprobar si un número es capicúa. 
# Es decir, si se lee igual de derecha a
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