# Escribe un programa en Python para comprobar si un número es primo
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