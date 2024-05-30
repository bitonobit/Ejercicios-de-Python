# ******************************************************************************
#  Escribe un programa para producir la serie Fibonacci en Python.
# ******************************************************************************
def fibo(terminos):
    if n>=1:
        t1=0
        t2=1
        serie=f"Serie de Ficonacci de {terminos}: {t1}"
        for i in range(0,terminos-1):
            serie+=f" , {t2}"   # Concatenar el nuevo término
            aux=t1              # Calcular el nuevo término
            t1=t2               # con intercambio de variables
            t2=aux+t1
    else:
        serie="El valor debe introducido debe ser mayor que 0"
    return serie

n=int(input("¿Cuántos términos quieres calcular?: "))
print(fibo(n))