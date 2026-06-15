import csv


# ---------------------------------------------------------
# FUNCIÓN PARA CARGAR PAÍSES DESDE ARCHIVO CSV
# ---------------------------------------------------------
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


# ---------------------------------------------------------
# FUNCIÓN PARA MOSTRAR EL MENÚ PRINCIPAL
# ---------------------------------------------------------
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


# ---------------------------------------------------------
# FUNCIÓN PARA MOSTRAR TODOS LOS PAÍSES CARGADOS
# ---------------------------------------------------------
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


# ---------------------------------------------------------
# FUNCIÓN PARA VALIDAR TEXTO
# ---------------------------------------------------------
def texto_valido(texto):
    if texto == "":
        return False

    for caracter in texto:
        if not (caracter.isalpha() or caracter == " "):
            return False

    return True


# ---------------------------------------------------------
# FUNCIÓN PARA LEER UN NÚMERO ENTERO POSITIVO
# ---------------------------------------------------------
def leer_entero_positivo(mensaje):
    while True:
        try:
            numero = int(input(mensaje))

            if numero <= 0:
                raise ValueError

            return numero

        except ValueError:
            print("Error: debe ingresar un número entero positivo.")


# ---------------------------------------------------------
# FUNCIÓN PARA VERIFICAR SI UN PAÍS YA EXISTE
# ---------------------------------------------------------
def pais_existe(paises, nombre):
    for pais in paises:
        if pais["nombre"].strip().lower() == nombre.strip().lower():
            return True

    return False


# ---------------------------------------------------------
# FUNCIÓN PARA AGREGAR UN PAÍS
# ---------------------------------------------------------
def agregar_pais(paises):
    print("\n--- AGREGAR PAÍS ---")

    while True:
        nombre = input("Ingrese el nombre del país: ").strip()

        if not texto_valido(nombre):
            print("Error: el nombre no puede estar vacío ni contener números o símbolos.")

        elif pais_existe(paises, nombre):
            print("Error: el país ya existe en el sistema.")

        else:
            break

    poblacion = leer_entero_positivo("Ingrese la población: ")
    superficie = leer_entero_positivo("Ingrese la superficie en km²: ")

    while True:
        continente = input("Ingrese el continente: ").strip()

        if not texto_valido(continente):
            print("Error: el continente no puede estar vacío ni contener números o símbolos.")
        else:
            break

    pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(pais)

    print("País agregado correctamente.")


# ---------------------------------------------------------
# FUNCIÓN PRINCIPAL DEL PROGRAMA
# ---------------------------------------------------------
def main():
    paises = cargar_paises("paises.csv")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_paises(paises)

        elif opcion == "2":
            agregar_pais(paises)

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


# ---------------------------------------------------------
# EJECUCIÓN DEL PROGRAMA
# ---------------------------------------------------------
main()