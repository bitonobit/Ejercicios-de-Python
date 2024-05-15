# PIP es un administrador de paquetes para paquetes o módulos de Python
# Un paquete contiene todos los archivos necesarios para un módulo.
# Los módulos son bibliotecas de código Python 
# que puedes incluir en tu proyecto.
# Verifica la versión de PIP desde el CMD:
# C:\Users\Candy\AppData\Local\Programs\Python\Python36-32\Scripts>pip --version
# Instalar PIP
# Si no tienes PIP instalado, puedes descargarlo e instalarlo desde esta página: https://pypi.org/project/pip/

# PIP es un administrador de paquetes para paquetes o módulos de Python.
# Si tienes una versión 3.4 o posterior viene incluido de forma predeterminada
# Para saber si está instalado escribe eso en tu terminal: C:\Users\TuNombre\AppData\Local\Programs\Python\Python36-32\Scripts>pip --version
# Descargar un paquete es muy fácil.
# Abre la interfaz de línea de comando y 
# Dile a PIP que descargue el paquete que deseas.

# Navega por la línea de comando hasta la ubicación del directorio de secuencias de comandos de Python y escribe lo siguiente:
# C:\Users\Candy\AppData\Local\Programs\Python\Python36-32\Scripts>pip install camelcase
# Esto descargará el paquete camelcase
# Una vez que el paquete esté instalado, estará listo para usar.
# Lo importamos en el proyecto y listo
# Encuentra paquetes en https://pypi.org/ .

import camelcase
c = camelcase.CamelCase()
txt = "candy gonzález"
print(c.hump(txt))

# Utiliza el comando uninstall para eliminar un paquete, desde el CMD
# C:\Users\Candy\AppData\Local\Programs\Python\Python36-32\Scripts>pip uninstall camelcase
# Utiliza el comando list para listar todos los paquetes, desde el CMD
# C:\Users\Candy\AppData\Local\Programs\Python\Python36-32\Scripts>pip list