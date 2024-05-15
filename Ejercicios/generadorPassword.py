import random
import string

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    #Selecciona caracteres aleatorios de un conjunto que incluye letras (mayúsculas y minúsculas), dígitos y caracteres especiales
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def main():
    longitud = int(input("Ingrese la longitud de la contraseña: "))
    contrasena = generar_contrasena(longitud)
    print("Contraseña generada:", contrasena)

if __name__ == "__main__":
    main()
