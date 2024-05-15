# Obtiene los hipervínculos de una web
# 1. Importar bibliotecas:
import requests
from bs4 import BeautifulSoup
# 2. Poner la url de la web a scrapear
url = 'https://portalciencia.ull.es/investigadores'
# 3. Regoger la respuesta http
response = requests.get(url)
# 4. Parsear la respuesta con la biblioteca
soup = BeautifulSoup(response.text, 'html.parser')
# 5. Establecer el criterio de búsqueda y lo guarda en
links = soup.find_all('a')
lista=[]
# 6. Mostrar el resultado
for link in links:
    href = link.get('href')
    print(href)
    lista.append(href)
    
