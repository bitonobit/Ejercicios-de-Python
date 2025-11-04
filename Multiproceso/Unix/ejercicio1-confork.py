import os

def padre():
    while True:
        newpid = os.fork()
        if newpid == 0:   #Proceso hijo
            hijo()
        else:
            print(f"Padre {os.getpid()}, Hijo {newpid}")
            reply = input("Pulsa 's' si quieres crear un nuevo proceso: ")
            if reply != 's':
                break

def hijo():
    print(f"Nuevo hijo creado con el pid {os.getpid()} a punto de finalizar")
    os._exit(0)

if __name__ == "__main__":
    padre()
