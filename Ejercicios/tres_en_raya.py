# ******************************************************************************
# Vamos a jugar al tres en raya (Tic-Tac-Toe), permite jugar a dos jugadores en # la consola. El juego debe:
#   1. Imprimir el tablero: Mostrar el tablero en la consola
#   2. Verificar ganador: Comprobar si hay un ganador o un empate
#   3. Mover jugador: Permitir que los jugadores ingresen sus movimientos
#   4. Cambiar turno: Alternar entre los jugadores
#   5. Jugar el juego: Ejecutar el bucle principal del juego
# ******************************************************************************

def imprimir_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
        print("-" * 5)

def verificar_ganador(tablero, jugador):
    for fila in tablero:
        if all([celda == jugador for celda in fila]):
            return True
    for col in range(3):
        if all([tablero[fila][col] == jugador for fila in range(3)]):
            return True
    if all([tablero[i][i] == jugador for i in range(3)]) or all([tablero[i][2 - i] == jugador for i in range(3)]):
        return True
    return False

def verificar_empate(tablero):
    for fila in tablero:
        if any([celda == " " for celda in fila]):
            return False
    return True

def mover_jugador(tablero, jugador):
    while True:
        try:
            fila = int(input(f"Jugador {jugador}, ingresa la fila (0, 1, 2): "))
            col = int(input(f"Jugador {jugador}, ingresa la columna (0, 1, 2): "))
            if tablero[fila][col] == " ":
                tablero[fila][col] = jugador
                break
            else:
                print("Esa celda ya está ocupada. Intenta de nuevo.")
        except (IndexError, ValueError):
            print("Entrada no válida. Asegúrate de ingresar números entre 0 y 2.")

def cambiar_turno(jugador):
    return "O" if jugador == "X" else "X"

def jugar():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugador_actual = "X"
    
    while True:
        imprimir_tablero(tablero)
        mover_jugador(tablero, jugador_actual)
        
        if verificar_ganador(tablero, jugador_actual):
            imprimir_tablero(tablero)
            print(f"¡Jugador {jugador_actual} gana!")
            break
        
        if verificar_empate(tablero):
            imprimir_tablero(tablero)
            print("¡Es un empate!")
            break
        
        jugador_actual = cambiar_turno(jugador_actual)

if __name__ == "__main__":
    jugar()



# Opcional:
#   - Implementar una versión con una interfaz gráfica utilizando `tkinter` 
#   - Añadir inteligencia artificial para que un jugador pueda jugar contra lel ordenador.

