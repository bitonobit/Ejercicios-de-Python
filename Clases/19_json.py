# JSON es una sintaxis para almacenar e intercambiar datos.
# JSON es texto escrito con notación de objetos JavaScript.

import json             #Importamos el módulo

# *********************************************************
#           De JSOn a Python
# *********************************************************

# 1. Creamos un JSON:
x =  '{ "nombre":"Candy", "edad":"30", "lugar":"Tenerife"}'
# x = '{ "name":"John", "age":30, "city":"New York"}'
# 2. Parseamos x:
y = json.loads(x)

# 3. El resultado es un diccionario de Python:
print(y["lugar"])

# *********************************************************
#           De Python a JSOn 
# *********************************************************

# 1. Creamos el diccionario de Python:
x = {
  "nombre": "Rafael",
  "apellidos": "Glez",
  "dni": "12345678Z"
}

# 2. Convertimos a JSON:
y = json.dumps(x)

# 3. El resultado es un string de JSON:
print(y)

# Se pueden convertir a JSON:
print(json.dumps({"nombre": "Ana", "edad": 30}))  # Diccionarios
print(json.dumps(["Azúcar", "Café", "Leche"]))    # Listas
print(json.dumps(("E1", "E2", "PO", "PP")))       # Tuplas
print(json.dumps("hello"))                        # Cadenas
print(json.dumps(42))                             # Números
print(json.dumps(31.76))
print(json.dumps(True))                           # Booleanos
print(json.dumps(False))
print(json.dumps(None))

# Un ejemplo usando todos los tipos posibles
x = {
  "nombre": "Ana",
  "edad": 30,
  "registro": True,
  "suscripcion": False,
  "cursos": ("Python","Js"),
  "abandonos": None,
  "proyectos": [
    {"titulo": "Tienda Online", "entrega": 1},
    {"titulo": "Reproductor de mp3", "entrega": 2}
  ]
}

print(json.dumps(x))

# Utiliza el parámetro indent para definir el número de sangrías:
print(json.dumps(x, indent=4))

# Se puede usar el parámetro separators para cambiar el separador predeterminado:
print(json.dumps(x, indent=4, separators=(". ", " = ")))

# Tambien se puede agregar un parametro para ordenar los resultados
print(json.dumps(x, indent=4, sort_keys=True))