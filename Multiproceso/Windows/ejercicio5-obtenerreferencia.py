import subprocess
import time

def CrearProceso():
    try:
        porc = subprocess.Popen(['notepad.exe'])
        return porc # Devuelve la referencia al proceso creado
    except subprocess.CalledProcessError as e:
        print(e.output)
        # print(f"Error al crear el proceso: {e}")
        # return None
p=CrearProceso()
# print(f"Proceso creado con PID: {p.pid}")
print("El PID de este proceso es:}" + str(p.pid))
time.sleep(5)
p.kill()
print("Fin de ejecución ...")
