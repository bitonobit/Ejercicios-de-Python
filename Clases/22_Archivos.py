# El manejo de archivos es una parte importante de cualquier aplicación.
# La función clave para trabajar con archivos en Python es la función open()
# 1. Abrir un archivo y leerlo
aux=open("archivo.txt")
aux=open("archivo.txt", "r")
#  Imprime el contenido del archivo
print(aux.read())
# Lee e imprime los 10 prpimeros caracteres
print(aux.read(10))
# Leer líneas
print(aux.readline())
# Recorrer el archivo línea a línea
for x in aux:
  print(x)
# 2. Abre un archivo para agregarlo y crea el archivo si no existe
aux=open("archivo_2.txt", "a")
# 3. Abre un archivo para escribir, crea el archivo si no existe
aux=open("archivo_2.txt", "w")
# 4. Crea el archivo especificado, devuelve un error si el archivo existe
aux=open("archivo_2.txt", "x")
# 5. Cerrar el archivo
aux.close()
# Cierra siemprelos archivos,  debido al almacenamiento en búfer, es posible que los cambios realizados en un archivo no se muestren hasta que lo cierre.
# Además, puede especificar si el archivo debe manejarse en modo binario o texto.
# "t"- Texto - Valor predeterminado. Modo texto
# "b"- Binario - Modo binario (por ejemplo, imágenes)

# ******************* Importante ******************************
# "a"- Agregar: se agregará al final del archivo.
# "w"- Escribir: sobrescribirá cualquier contenido existente.

# 6. Eliminar un archivo
# Para eliminar un archivo, tenemos que importar el módulo del sistema operativo y ejecutar la función os.remove():
import os
if os.path.exists("archivo_2.txt"):
  os.remove("archivo_2.txt")
else:
  print("Archivo no encontrado")

# También podemos eliminar una carpeta, usando os.rmdir() pero sólo si está vacía:
import os
os.rmdir("nombreCarpeta")