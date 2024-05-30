# ******************************************************************************
# Escribe una función para invertir palabras enteras de una cadena dada (frase) # y hablar como Yoda :)
# ******************************************************************************
def palindromo(frase):
    palabras= frase.split( )            #Corta la frase en palabras
    aux=' '.join(reversed(palabras))    #Vuelve a unir la cadena
    return aux                          #Retorna la cadena

if __name__=="__main__":
    print(palindromo(input("Dime la frase: ")))     #Pide la frase por consola