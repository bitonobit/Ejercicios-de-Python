# ******************************************************************************
# Crear un archivo CSV utilizando la biblioteca estándar csv para scrapear un  # directorio de empresas
# ******************************************************************************
import csv
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

def parsearTabla(url):
  # Hacer una solicitud HTTP GET a la URL
  response = requests.get(url)
  # Comprobar que la solicitud fue exitosa
  if response.status_code == 200:
    # Parsear el contenido HTML de la página
    soup = BeautifulSoup(response.content, 'html.parser')
    # Encontrar la tabla en la página 
    table = soup.find('table')
    # if table:
    # Lista para almacenar los valores de los <td>
    td_values = []
    # Parsear todas las filas <tr> de la tabla
    for row in table.find_all('tr'):
      # Parsear todas las celdas <td> de la fila
      for cell in row.find_all('td'):
        # Añadir el texto de la celda a la lista
        td_values.append(cell.get_text(strip=True))

    # Imprimir los valores de los <td>
    print(td_values)
    # else:
    #   print("No se encontró ninguna tabla en la página.")
    # Avanzar a la siguiente página (url) 
    prox = soup.find_all('a', class_='next') 
    if prox:
      for link in prox:
        href = link.get('href')
        print(href)
        return href
    else:
      return "fin"
  else:
      print(f"Error al obtener la página: {response.status_code}")


# URL base de la página web que contiene la tabla
x="https://www.informa.es/directorio-empresas/J062_PROGRAMACION-CONSULTORIA-OTRAS-ACTIVIDADES-RELACIONADAS-INFORMATICA.html"
url=parsearTabla(x)
while url !="fin":
  url=parsearTabla(url)
  

def archivo(datos):
  # Crear y abrir un archivo CSV para escritura con codificación UTF-8
  with open('datos.csv', mode='w', newline='', encoding='utf-8') as archivo_csv:
      escritor_csv = csv.writer(archivo_csv)
      # Escribir los datos en el archivo CSV
      escritor_csv.writerows(datos)

  print("Archivo CSV creado exitosamente.")