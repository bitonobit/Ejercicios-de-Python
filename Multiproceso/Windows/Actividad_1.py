import multiprocessing
import random

# Configuración del juego
total_cartas = 24
num_parejas = total_cartas // 2 # Número de parejas
num_jugadores = 2  # Número de jugadores (procesos hijos)

# Crear el tablero con 12 parejas, duplicando números del 1 al 12 y barajando
cartas = list(range(1, num_parejas + 1)) * 2 # Duplicar para parejas
random.shuffle(cartas) # Barajar las cartas

# Estado del tablero: False si carta oculta, True si volteada (visible)
estado_tablero = [False] * total_cartas

def imprimir_tablero():
    """Muestra el tablero en consola mostrando cartas visibles y X para ocultas."""
    for i in range(total_cartas):
        if estado_tablero[i]:
            print(f"{cartas[i]:2}", end=' ')
        else:
            print(" X", end=' ')
        if (i + 1) % 6 == 0:
            print()

def jugador(pipe_padre):
    """Función para procesos hijos que representan jugadores."""
    while True:
        msg = pipe_padre.recv()
        if msg == 'tu_turno':
            print(f"\nJugador {multiprocessing.current_process().name} es tu turno.")
            while True:
                try:
                    pos1 = int(input("Ingresa posición 1 (0 a 23): "))
                    pos2 = int(input("Ingresa posición 2 (0 a 23): "))
                    # Validaciones para que las posiciones sean válidas y no estén ya volteadas
                    if pos1 == pos2 or not (0 <= pos1 < total_cartas) or not (0 <= pos2 < total_cartas) or estado_tablero[pos1] or estado_tablero[pos2]:
                        print("Posiciones inválidas. Intenta nuevamente.")
                        continue
                    break
                except ValueError:
                    print("Entrada inválida. Debes ingresar un número.")
            pipe_padre.send((pos1, pos2))
        elif msg == 'resultado':
            puntaje = pipe_padre.recv()
            ganador = pipe_padre.recv()
            if ganador:
                print(f"\nJugador {multiprocessing.current_process().name} ha ganado con {puntaje} puntos!")
            else:
                print(f"\nJugador {multiprocessing.current_process().name} terminó con {puntaje} puntos.")
        elif msg == 'fin':
            break

if __name__ == '__main__':
    # Crear tuberías para comunicación entre padre e hijos
    pipes = [multiprocessing.Pipe() for _ in range(num_jugadores)]
    procesos = []
    puntajes = [0] * num_jugadores

    # Lanzar procesos hijos para cada jugador
    for i in range(num_jugadores):
        p = multiprocessing.Process(target=jugador, args=(pipes[i][1],), name=f"P{i+1}")
        p.start()
        procesos.append(p)

    imprimir_tablero()

    cartas_restantes = total_cartas
    turno = 0

    while cartas_restantes > 0:
        # Indicar al jugador actual que es su turno
        pipes[turno][0].send('tu_turno')

        # Recibir posiciones elegidas por el jugador
        pos1, pos2 = pipes[turno][0].recv()

        # Voltear cartas y mostrar el tablero actualizado
        estado_tablero[pos1] = True
        estado_tablero[pos2] = True
        imprimir_tablero()

        # Verificar si las cartas son pareja
        if cartas[pos1] == cartas[pos2]:
            print(f"\nJugador P{turno+1} encontró pareja! +1 punto.")
            puntajes[turno] += 1
            cartas_restantes -= 2
            # El jugador sigue jugando (mismo turno)
        else:
            print(f"\nJugador P{turno+1} no encontró pareja. Se voltean cartas de nuevo.")
            estado_tablero[pos1] = False
            estado_tablero[pos2] = False
            # Cambiar turno al siguiente jugador
            turno = (turno + 1) % num_jugadores

    print("\n¡Juego terminado!")

    # Determinar puntaje máximo y enviar resultados a jugadores
    max_puntaje = max(puntajes)
    for i in range(num_jugadores):
        pipes[i][0].send('resultado')
        pipes[i][0].send(puntajes[i])
        pipes[i][0].send(puntajes[i] == max_puntaje)

    # Enviar señal para finalizar juegos a hijos
    for i in range(num_jugadores):
        pipes[i][0].send('fin')

    # Esperar a que terminen procesos hijos
    for p in procesos:
        p.join()
