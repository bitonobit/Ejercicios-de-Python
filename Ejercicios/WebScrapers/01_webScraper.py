# ******************************************************************************
# Busca los elementos div de una web que tengan la clase especificada, por     # ejemplo "container"
# ******************************************************************************
# 01. Importar bibliotecas:
import requests
from bs4 import BeautifulSoup
# 02. Obtener el contenido de la página web:
url = 'https://es.python.org/'
response = requests.get(url)
# 03. Analizar el contenido HTML: Utilizando BeautifulSoup para analizar el contenido HTML y encontrar los elementos que te interesan. Por ejemplo, si quieres extraer los div con una clase:
soup = BeautifulSoup(response.text, 'html.parser')
titles = soup.find_all('div', class_='container')
# 04. Extraer información:
for title in titles:
    print(title.text)
