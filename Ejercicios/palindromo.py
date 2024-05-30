# ******************************************************************************
#  Escribir una función para comprobar si una palabra es palíndrome. Es 
#  decir, si se lee igual de izquierda a derecha que de derecha a izquierda
# ******************************************************************************
def palindromo(p):
    # palabra= p.split( )
    aux=''.join(reversed(p))
    if aux==p:
        return f" '{p}' es un palíndromo"
    else:
        return f" '{p}' NO es un palíndromo -> {aux}"

if __name__=="__main__":
    print(palindromo(input("Dime la palabra: ")))