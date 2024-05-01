# Invertir letras de una palabra dada y ver si se lee igual
def palindromo(p):
    # palabra= p.split( )
    aux=''.join(reversed(p))
    if aux==p:
        return f" '{p}' es un palíndromo"
    else:
        return f" '{p}' NO es un palíndromo -> {aux}"

if __name__=="__main__":
    print(palindromo(input("Dime la palabra: ")))