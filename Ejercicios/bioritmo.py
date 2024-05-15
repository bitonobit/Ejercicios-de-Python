# El biorritmo es una teoría que sugiere que nuestras vidas están influenciadas por ciclos biológicos que afectan nuestro estado físico, emocional e intelectual.
import math

def calcular_biorritmo(dia_nacimiento, dia_actual, ciclo):
    return math.sin((dia_actual - dia_nacimiento) * (2 * math.pi) / ciclo)

def imprimir_biorritmo(nombre, valor):
    if valor > 0:
        estado = "en alta"
    elif valor < 0:
        estado = "en baja"
    else:
        estado = "en equilibrio"
    print(f"{nombre.capitalize()}: {valor:.2f} ({estado})")

def main():
    dia_nacimiento = int(input("Ingrese el día de su nacimiento (1-31): "))
    dia_actual = int(input("Ingrese el día actual (1-31): "))

    ciclo_fisico = 23  # Ciclo físico de 23 días
    ciclo_emocional = 28  # Ciclo emocional de 28 días
    ciclo_intelectual = 33  # Ciclo intelectual de 33 días

    biorritmo_fisico = calcular_biorritmo(dia_nacimiento, dia_actual, ciclo_fisico)
    biorritmo_emocional = calcular_biorritmo(dia_nacimiento, dia_actual, ciclo_emocional)
    biorritmo_intelectual = calcular_biorritmo(dia_nacimiento, dia_actual, ciclo_intelectual)

    imprimir_biorritmo("Biorritmo físico", biorritmo_fisico)
    imprimir_biorritmo("Biorritmo emocional", biorritmo_emocional)
    imprimir_biorritmo("Biorritmo intelectual", biorritmo_intelectual)

if __name__ == "__main__":
    main()
