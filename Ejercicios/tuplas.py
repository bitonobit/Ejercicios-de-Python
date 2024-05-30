# ******************************************************************************
# ** Ejercicios de Tuplas                                                     **
# ******************************************************************************

# 1. Realizar la suma de los elementos de una tupla
tupla=(7,8,9,1,19,7)
print(f"Los valores a sumar son: {tupla}")

def sumar(tupla):
    if len(tupla)==0:
        return "La tupla está vacía"
    elif len(tupla)==1:
        return tupla[0]
    else:
        return tupla[0] + sumar(tupla[1:])
    
print("La suma es:", sumar(tupla))

