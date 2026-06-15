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

    except KeyError:
        print("Error: el archivo CSV no tiene las columnas esperadas.")
        return []

# FUNCIÓN PARA MOSTRAR EL MENÚ PRINCIPAL

def mostrar_menu():
    print("\n" + "=" * 50)
    print("        GESTIÓN DE DATOS DE PAÍSES")
    print("=" * 50)
    print("1. Mostrar todos los países")
    print("2. Agregar un país")
    print("3. Actualizar población y superficie")
    print("4. Buscar país por nombre")
    print("5. Filtrar países")
    print("6. Ordenar países")
    print("7. Mostrar estadísticas")
    print("8. Salir")
    print("=" * 50)

# FUNCIÓN PARA MOSTRAR TODOS LOS PAÍSES CARGADOS

def mostrar_paises(paises):
    if len(paises) == 0:
        print("No hay países cargados.")
    else:
        for pais in paises:
            print("--------------------------------")
            print("Nombre:", pais["nombre"])
            print("Población:", pais["poblacion"])
            print("Superficie:", pais["superficie"], "km²")
            print("Continente:", pais["continente"])

# FUNCIÓN PRINCIPAL DEL PROGRAMA

def main():
    paises = cargar_paises("paises.csv")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_paises(paises)

        elif opcion == "2":
            print("Función agregar país en desarrollo.")

        elif opcion == "3":
            print("Función actualizar país en desarrollo.")

        elif opcion == "4":
            print("Función buscar país en desarrollo.")

        elif opcion == "5":
            print("Función filtrar países en desarrollo.")

        elif opcion == "6":
            print("Función ordenar países en desarrollo.")

        elif opcion == "7":
            print("Función estadísticas en desarrollo.")

        elif opcion == "8":
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

# EJECUCIÓN DEL PROGRAMA

main()