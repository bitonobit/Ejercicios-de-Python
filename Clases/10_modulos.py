# Considera que un módulo es lo mismo que una biblioteca, es decir, un archivo que contiene un conjunto de funciones que deseas incluir en tu aplicación
import miModulo           #Importas el módulo
miModulo.saluda("Candy")  #Llama a la función
# Nota: Cuando utilices una función de un módulo, utiliza la sintaxis: nombre_módulo.nombre_función 


import miModulo as m  #Crea un alias

# Hay varios módulos integrados en Python, que puedes importar cuando quieras.
# Puedes optar por importar solo partes de un módulo utilizando la palabra clave from

from miModulo import saluda
saluda("Bitonobit")
# Nota: Al importar utilizando from no se usa el nombre del módulo cuando haces referencia a sus elementos Ejemplo: saluda("Candy"), no miModulo.saludo("Candy")