# Sacar los email de una web, los muestra por consola y los guarda en una lista
# 1. Importar bibliotecas:
import requests
from bs4 import BeautifulSoup
import re

def buscaEmail(href):
    lista=[]
    url = href
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Define la expresión regular para buscar emails
    regex_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    # Busca todos los elementos que coincidan con la expresión regular
    found_elements = soup.find_all(string=regex_pattern)
    for element in found_elements:
       lista.append(element.strip())
       print(element)
    return lista

# 2. Poner la url de la web a scrapear
url = 'https://ejemplo.com'
# 3. Regoger la respuesta http
response = requests.get(url)
# 4. Parsear la respuesta con la biblioteca
soup = BeautifulSoup(response.text, 'html.parser')
# 5. Establecer el criterio de búsqueda y lo guarda en
links = soup.find_all('a')
# 6. Mostrar el resultado
for link in links:
    href = link.get('href')
    buscaEmail(href)
