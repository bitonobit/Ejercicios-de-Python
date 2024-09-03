import requests
from bs4 import BeautifulSoup

# URL de la página web que contiene la tabla
url = "https://www.axesor.es/directorio-informacion-empresas/empresas-de-Santa-Cruz-De-Tenerife/informacion-empresas-de-Santa-Cruz-De-Tenerife/1"

# Hacer una solicitud HTTP GET a la URL
response = requests.get(url)

# Comprobar que la solicitud fue exitosa
if response.status_code == 200:
    # Parsear el contenido HTML de la página
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontrar la tabla en la página  
    tabla = soup.find('table')

    # Lista para almacenar los valores de los <td>
    td_values = []

    # Parsear todas las filas <tr> de la tabla
    for row in tabla.find_all('tr'):
        # Parsear todas las celdas <td> de la fila
        for cell in row.find_all('td'):
            # Añadir el texto de la celda a la lista
            td_values.append(cell.get_text(strip=True))

    # Imprimir los valores de los <td>
    print(td_values)
else:
    print(f"Error al obtener la página: {response.status_code}")

