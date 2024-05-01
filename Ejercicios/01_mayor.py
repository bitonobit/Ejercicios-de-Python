# Dados dos números, escriba un código Python para encontrar el mayor de estos dos números
def mayor(a,b):
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