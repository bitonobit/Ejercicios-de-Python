# En este script, utilizamos la biblioteca requests para hacer una solicitud a una API de tipo de cambio de moneda (exchangerate-api.com). La función obtener_tipo_cambio hace la solicitud y extrae el tipo de cambio entre la moneda de origen y la moneda de destino. Luego, la función convertir_moneda utiliza este tipo de cambio para convertir la cantidad especificada de la moneda de origen a la moneda de destino.

# En la función main, el usuario ingresa la cantidad de moneda, la moneda de origen y la moneda de destino, y luego se muestra el resultado de la conversión en la consola.
import requests

def obtener_tipo_cambio(moneda_origen, moneda_destino):
    url = f"https://api.exchangerate-api.com/v4/latest/{moneda_origen}"
    response = requests.get(url)
    data = response.json()
    tipo_cambio = data['rates'][moneda_destino]
    return tipo_cambio

def convertir_moneda(cantidad, moneda_origen, moneda_destino):
    tipo_cambio = obtener_tipo_cambio(moneda_origen, moneda_destino)
    cantidad_convertida = cantidad * tipo_cambio
    return cantidad_convertida

def main():
    cantidad = float(input("Ingrese la cantidad de moneda a convertir: "))
    moneda_origen = input("Ingrese la moneda de origen (por ejemplo, USD): ").upper()
    moneda_destino = input("Ingrese la moneda de destino (por ejemplo, EUR): ").upper()

    cantidad_convertida = convertir_moneda(cantidad, moneda_origen, moneda_destino)
    print(f"{cantidad} {moneda_origen} equivalen a {cantidad_convertida} {moneda_destino}.")

if __name__ == "__main__":
    main()
