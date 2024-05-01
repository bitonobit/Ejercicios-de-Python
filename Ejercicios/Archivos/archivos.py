# Escribe un código que pueda contar todas las palabras mayúsculas de un archivo. 
# Al usar with el archivo se cierra solo al terminar
cont=0
with open('archivo.txt', 'r') as archivo:
    texto=archivo.read()
for x in texto:
    if x.isupper():
        cont+=1
print(cont)