from math import pi

#Función con la excepción TypeError y verificación de negativos
def area(r):
#Verificamos los tipos correctos
    if type(r) not in [float, int]:
        raise TypeError("Solo números enteros o de coma flotante.")
    #Verificamos los valores negativos
    if r<0:
        raise ValueError("No se permiten valores negativos")
    areaC = pi*(r**2)
    return areaC

