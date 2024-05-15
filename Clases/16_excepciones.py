# El bloque try: permite probar un bloque de código en busca de errores.
# El bloque except: permite manejar el error.
# El bloque else: permite ejecutar código cuando no hay ningún error.
# El bloque finally: permite ejecutar código, independientemente del resultado de los s try y except.
try:
  print(x)
except:
  print("x no está definido")

# Se pueden crear tantas excepciones como queramos
try:
  print(y)
except NameError:
  print("Variable y no está definida")
except:
  print("Ups ha habido un error")

# Se puede usar un else para colocar un código que se ejecuta si no hay errores
try:
  print("Hola pepsicola")
except:
  print("Upss, error")
else:
  print("Todo OK")

# El bloque finally, si se especifica, se ejecutará independientemente de si el bloque try genera un error o no.
try:
  print("Hola pepsicola")
except:
  print("Upss, error")
finally:
  print("La excepción ha finalizado")

# Para lanzar (o generar) una excepción, usamos la palabra clave: raise
x = -1
if x < 0:
  raise Exception("No se permiten valores negativos")

# Se puede definir qué tipo de error generar y el texto que se imprimirá al usuario.
x = "Hola"

if not type(x) is int:
  raise TypeError("Sólo se permiten números")