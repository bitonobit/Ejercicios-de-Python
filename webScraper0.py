# Busca los elementos div de una web que tengan la clase especificada
# Importar bibliotecas:
import requests
from bs4 import BeautifulSoup
# Obtener el contenido de la página web:
url = 'https://es.python.org/'
response = requests.get(url)
# Analizar el contenido HTML: Utiliza BeautifulSoup para analizar el contenido HTML y encontrar los elementos que te interesan. Por ejemplo, si quieres extraer los div con una clase:
soup = BeautifulSoup(response.text, 'html.parser')
titles = soup.find_all('div', class_='container')
# Extraer información:
for title in titles:
    print(title.text)
