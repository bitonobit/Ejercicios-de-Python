# Revisa todas las URLs de un sitio en busca de emails y los guarda en un archivo .csv esta sin terminar

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

# requests.packages.urllib3.disable_warnings()

def obtener_urls(sitio_web):
    # Utilizamos un conjunto para evitar duplicados
    urls = set()        
    # Hacemos una solicitud HTTP para obtener el contenido HTML del sitio web
    respuesta = requests.get(sitio_web)
    # Verificamos si la solicitud fue exitosa (código de estado 200)
    if respuesta.status_code == 200:
        # Parseamos el contenido HTML utilizando BeautifulSoup
        soup = BeautifulSoup(respuesta.content, 'html.parser')
        # Encontramos todos los elementos 'a' (enlaces) en el HTML
        enlaces = soup.find_all('a')
        # Iteramos sobre los enlaces encontrados
        for enlace in enlaces:
            # Obtenemos el atributo 'href' de cada enlace
            href = enlace.get('href')
            # Comprobamos si el enlace es relativo o absoluto y lo convertimos a una URL absoluta
            url_absoluta = urljoin(sitio_web, href)
            # Añadimos la URL a nuestro conjunto de URLs
            urls.add(url_absoluta)
    return urls

def buscaEmail(url):
  # Recorre la url en busca de un email
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  # Define la expresión regular que deseas buscar
  regex_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
  # Busca todos los elementos que coincidan con la expresión regular
  found_elements = soup.find_all(string=regex_pattern)
  emails=set()  #Utilizamos un conjunto para evitar duplicados
  for element in found_elements:
      print(element.strip())
      emails.add(element.strip())
  # Abrir un archivo en modo de escritura ('w')
  # Si el archivo no existe, se creará. Si ya existe, se sobrescribirá.
  with open('contactos.txt', 'a') as archivo:
    # Escribir en el archivo
    for e in emails:
      archivo.write(e + '\n')

  return emails

def encontrar_caracteres(cadena):
    # Expresión regular para encontrar elementos que contienen "?" o "="
    patron = re.compile(r'[?=]')
    # Buscar coincidencias en la cadena
    coincidencias = patron.search(cadena)
    # Devolver True si se encontraron coincidencias, False si no se encontraron
    return bool(coincidencias)


# Ejemplo de uso
if __name__ == "__main__":
    sitio_web = 'https://portalciencia.ull.es/investigadores'
    lista_url=set()
    urls = obtener_urls(sitio_web)
    for url in urls:
        if (url.find('portalciencia.ull.es/')!=-1) & (url.find('investigadores')!=-1):
          print(url)
          if encontrar_caracteres(url):
             continue
          urls_internas=obtener_urls(url)
          for u in urls_internas:
             if encontrar_caracteres(url):
               continue
             if u.find('detalle')!=-1:
                print(u)
                lista_url.add(u)

    for x in lista_url:           
      buscaEmail(x)


