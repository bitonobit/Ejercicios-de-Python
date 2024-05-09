# Sacar los email de un sitio 
# 1. Importar bibliotecas:
import requests
from bs4 import BeautifulSoup
import re
# 2. Poner la url de la web a scrapear
url = 'https://es.wikipedia.org/wiki/Python'
# 3. Regoger la respuesta http
response = requests.get(url)
# 4. Parsear la respuesta con la biblioteca
soup = BeautifulSoup(response.text, 'html.parser')
# 5. Establecer el criterio de búsqueda y lo guarda en
links = soup.find_all('a')
lista=(())
# 6. Mostrar el resultado
for link in links:
    href = link.get('href')
    
