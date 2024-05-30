# ******************************************************************************
#  Dados dos números, escribe una función encontrar el mayor número
# ******************************************************************************
def mayor(a,b):
    """
    Esta función determina el mayor de dos números dados

    Args:
        a,b (int): Nímeros a comparar

    Returns:
        str: Un mensaje que dice cual de los números es mayor o si son iguales
    """
    if a>b:    
        return f"a= {a} es mayor que b={b}"
    elif a<b:
        return f"b= {b} es mayor que a={a}"
    else:
        return f"a=b= {b} son iguales" 

print("\n--- El mayor de dos números ---")
x=int(input("Introduce el número a:"))    
y=int(input("Introduce el número b:"))    
print(mayor(x,y))