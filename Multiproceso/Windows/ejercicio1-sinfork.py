from multiprocessing import Process
import os

def hijo(): # Proceso hijo
    # Muestra el PID del proceso hijo y su padre
    print(f"Proceso hijo: PID {os.getpid()}, PID padre {os.getppid()}") 

def padre(): # Proceso padre
    while True:
        p = Process(target=hijo) # Crea un nuevo proceso hijo
        p.start() # Inicia el proceso hijo
        # Muestra el PID del proceso padre y del hijo
        print(f"Proceso padre: PID {os.getpid()}, PID hijo {p.pid}") 
        p.join()  # Espera a que el proceso hijo termine
        reply = input("Pulsa 's' si quieres crear un nuevo proceso: ")
        if reply != 's':
            break

if __name__ == "__main__": # Ejecuta el proceso
    padre()
