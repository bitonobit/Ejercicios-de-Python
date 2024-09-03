# ******************************************************************************
# Visita todas las URLs de un sitio web y las imprime
# ******************************************************************************
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import re

def get_all_urls(base_url):
    # Almacenamos las URLs únicas que ya hemos visitado para evitar ciclos infinitos
    visited_urls = set()
    # Inicializamos una lista para almacenar todas las URLs encontradas
    all_urls = []

    # Función para obtener todas las URLs de una página dada
    def get_urls_from_page(url):
        # Solicitamos el contenido de la página web
        response = requests.get(url)
        # Creamos un objeto BeautifulSoup para analizar el HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        # Buscamos todos los elementos <a> que contienen enlaces
        links = soup.find_all('a', href=True)
        # Iteramos sobre los enlaces encontrados
        for link in links:
            # Construimos la URL absoluta a partir del enlace relativo
            absolute_url = urljoin(url, link['href'])
            # Parseamos la URL para normalizarla y evitar duplicados
            parsed_url = urlparse(absolute_url)
            # Si la URL es válida y no hemos visitado esta URL antes, la agregamos a la lista
            if parsed_url.scheme and parsed_url.netloc and absolute_url not in visited_urls:
                all_urls.append(absolute_url)
                visited_urls.add(absolute_url)
                print(link)

    # Empezamos con la URL base
    get_urls_from_page(base_url)

    # Iteramos sobre todas las URLs almacenadas y buscamos más URLs en cada página
    for url in all_urls:
        get_urls_from_page(url)

    return all_urls

# URL base del sitio web que deseas recorrer
base_url = 'https://www.gobiernodecanarias.org/principal/'

# Llamamos a la función para obtener todas las URLs del sitio web
all_urls = get_all_urls(base_url)

# Imprimimos todas las URLs encontradas
for url in all_urls:
    print(url)
