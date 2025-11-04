import subprocess 
# Importa el módulo subprocess para ejecutar procesos del sistema

try:
  subprocess.run(['notepad.exe','texto.txt']) # Lanza el bloc de notas de Windows
# Captura errores en la ejecución del proceso
except subprocess.CalledProcessError as e: 
      print(f"Error al lanzar notepad: {e}")