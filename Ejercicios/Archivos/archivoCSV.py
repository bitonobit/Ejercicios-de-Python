# ******************************************************************************
# Crear un archivo CSV tilizando la biblioteca estándar csv
#   01. Importar la biblioteca csv
#   02. Crear datos para el CSV, los datos pueden estar en una lista de listas 
#       o en un diccionario
#   03. Abrir un archivo CSV para escritura usando la función open en modo 
#       escritura ('w')
#   04. Debes especificar la codificación UTF-8 al abrir el archivo utilizando
#       el parámetro encoding='utf-8' al abrir el archivo. 
#   04. Crear un objeto escritor de CSV usando csv.writer  
#   05. Escribir los datos en el archivo con el método writerow para escribir 
#       una fila a la vez, o writerows para escribir múltiples filas.
# ******************************************************************************
import csv

# 01. Datos a escribir en el archivo CSV
datos = [
    ["Nombre", "Edad", "Ciudad"],
    ["Ana", 28, "Madrid"],
    ["Juan", 34, "Barcelona"],
    ["María", 22, "Valencia"],
    ["Pepe Ñáñez", 40, "Sevilla"]
]

# Crear y abrir un archivo CSV para escritura con codificación UTF-8
with open('datos.csv', mode='w', newline='', encoding='utf-8') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    
    # Escribir los datos en el archivo CSV
    escritor_csv.writerows(datos)

print("Archivo CSV creado exitosamente.")

