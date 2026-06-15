import csv

# FUNCIÓN PARA CARGAR PAÍSES DESDE ARCHIVO CSV

def cargar_paises(nombre_archivo):
    paises = []

    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                pais = {
                    "nombre": fila["nombre"],
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"]
                }

                paises.append(pais)

        print("Datos cargados correctamente.")
        return paises

    except FileNotFoundError:
        print("Error: no se encontró el archivo CSV.")
        return []

    except ValueError:
        print("Error: hay datos numéricos con formato incorrecto en el CSV.")
        return []

# FUNCIÓN PARA MOSTRAR TODOS LOS PAÍSES CARGADOS

def mostrar_paises(paises):
    if len(paises) == 0:
        print("No hay países cargados.")
    else:
        for pais in paises:
            print("--------------------------------")
            print("Nombre:", pais["nombre"])
            print("Población:", pais["poblacion"])
            print("Superficie:", pais["superficie"])
            print("Continente:", pais["continente"])

# PROGRAMA PRINCIPAL

paises = cargar_paises("paises.csv")
mostrar_paises(paises)