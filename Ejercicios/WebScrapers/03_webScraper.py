# ******************************************************************************
# Sacar los email de una web usando una expresión regular
# ******************************************************************************
import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.ull.es/masteres/listado-masteres/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# Define la expresión regular que deseas buscar
regex_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

# Busca todos los elementos que coincidan con la expresión regular
found_elements = soup.find_all(string=regex_pattern)

for element in found_elements:
    print(element.strip())
