import subprocess 
# Importa el módulo subprocess para ejecutar procesos del sistema
try:
  subprocess.run(['ping','www.marcombo.com',"-n","5"])  # Pasa parámetros al comando ping de Windows
# Captura errores en la ejecución del proceso
except subprocess.CalledProcessError as e: 
      print(f"Error al ejecutar ping: {e}")