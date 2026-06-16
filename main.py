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
    texto = texto.strip()

    if texto == "":
        return False

    texto_sin_espacios = texto.replace(" ", "")

    if texto_sin_espacios.isalpha():
        return True
    else:
        return False


# ---------------------------------------------------------
# FUNCIÓN PARA NORMALIZAR TEXTO EN COMPARACIONES
# ---------------------------------------------------------
def normalizar_texto(texto):
    texto = texto.strip().lower()

    texto = texto.replace("á", "a")
    texto = texto.replace("é", "e")
    texto = texto.replace("í", "i")
    texto = texto.replace("ó", "o")
    texto = texto.replace("ú", "u")
    texto = texto.replace("ü", "u")

    return texto


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
# FUNCIÓN PARA LEER UN NÚMERO ENTERO NO NEGATIVO
# ---------------------------------------------------------
def leer_entero_no_negativo(mensaje):
    while True:
        try:
            numero = int(input(mensaje))

            if numero < 0:
                raise ValueError

            return numero

        except ValueError:
            print("Error: debe ingresar un número entero igual o mayor a cero.")


# ---------------------------------------------------------
# FUNCIÓN PARA SELECCIONAR CONTINENTE
# ---------------------------------------------------------
def seleccionar_continente(permitir_volver):
    while True:
        print("\nSeleccione el continente:")
        print("1. América")
        print("2. Europa")
        print("3. Asia")
        print("4. África")
        print("5. Oceanía")

        if permitir_volver:
            print("6. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            return "América"
        elif opcion == "2":
            return "Europa"
        elif opcion == "3":
            return "Asia"
        elif opcion == "4":
            return "África"
        elif opcion == "5":
            return "Oceanía"
        elif opcion == "6" and permitir_volver:
            return ""
        else:
            print("Opción inválida. Intente nuevamente.")


# ---------------------------------------------------------
# FUNCIÓN PARA VERIFICAR SI UN PAÍS YA EXISTE
# ---------------------------------------------------------
def pais_existe(paises, nombre):
    for pais in paises:
        if normalizar_texto(pais["nombre"]) == normalizar_texto(nombre):
            return True

    return False


# ---------------------------------------------------------
# FUNCIÓN PARA BUSCAR EL ÍNDICE DE UN PAÍS
# ---------------------------------------------------------
def buscar_indice_pais(paises, nombre):
    for i in range(len(paises)):
        if normalizar_texto(paises[i]["nombre"]) == normalizar_texto(nombre):
            return i

    return -1


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

    continente = seleccionar_continente(False)

    pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(pais)

    print("País agregado correctamente.")


# ---------------------------------------------------------
# FUNCIÓN PARA ACTUALIZAR POBLACIÓN Y/O SUPERFICIE
# ---------------------------------------------------------
def actualizar_pais(paises):
    print("\n--- ACTUALIZAR PAÍS ---")

    if len(paises) == 0:
        print("No hay países cargados para actualizar.")
        return

    while True:
        nombre = input("Ingrese el nombre del país a actualizar: ").strip()

        if nombre == "":
            print("Operación cancelada. Volviendo al menú principal.")
            return

        if not texto_valido(nombre):
            print("Error: el nombre no puede contener números o símbolos.")

        else:
            indice = buscar_indice_pais(paises, nombre)

            if indice == -1:
                print("No se encontró el país. Intente nuevamente o presione Enter para volver al menú.")
            else:
                break

    print("\nDatos actuales:")
    print("Nombre:", paises[indice]["nombre"])
    print("Población:", paises[indice]["poblacion"])
    print("Superficie:", paises[indice]["superficie"], "km²")
    print("Continente:", paises[indice]["continente"])

    while True:
        print("\n¿Qué dato desea actualizar?")
        print("1. Población")
        print("2. Superficie")
        print("3. Población y superficie")
        print("4. Cancelar")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nueva_poblacion = leer_entero_positivo("Ingrese la nueva población: ")
            paises[indice]["poblacion"] = nueva_poblacion
            print("Población actualizada correctamente.")
            break

        elif opcion == "2":
            nueva_superficie = leer_entero_positivo("Ingrese la nueva superficie en km²: ")
            paises[indice]["superficie"] = nueva_superficie
            print("Superficie actualizada correctamente.")
            break

        elif opcion == "3":
            nueva_poblacion = leer_entero_positivo("Ingrese la nueva población: ")
            nueva_superficie = leer_entero_positivo("Ingrese la nueva superficie en km²: ")

            paises[indice]["poblacion"] = nueva_poblacion
            paises[indice]["superficie"] = nueva_superficie

            print("Población y superficie actualizadas correctamente.")
            break

        elif opcion == "4":
            print("Actualización cancelada.")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


# ---------------------------------------------------------
# FUNCIÓN PARA BUSCAR PAÍSES POR NOMBRE
# ---------------------------------------------------------
def buscar_pais_por_nombre(paises):
    print("\n--- BUSCAR PAÍS POR NOMBRE ---")

    if len(paises) == 0:
        print("No hay países cargados para buscar.")
        return

    while True:
        busqueda = input("Ingrese el nombre o parte del nombre del país, o presione Enter para volver al menú: ").strip()

        if busqueda == "":
            print("Volviendo al menú principal.")
            return

        if not texto_valido(busqueda):
            print("Error: la búsqueda no puede contener números o símbolos.")
        else:
            resultados = []

            for pais in paises:
                nombre_pais = normalizar_texto(pais["nombre"])

                if normalizar_texto(busqueda) in nombre_pais:
                    resultados.append(pais)

            if len(resultados) == 0:
                print("No se encontraron países con esa búsqueda. Intente nuevamente.")
            else:
                print("\nPaíses encontrados:")
                mostrar_paises(resultados)

                print("\nPuede realizar otra búsqueda o presionar Enter para volver al menú.")


# ---------------------------------------------------------
# FUNCIÓN PARA FILTRAR POR CONTINENTE
# ---------------------------------------------------------
def filtrar_por_continente(paises):
    print("\n--- FILTRAR POR CONTINENTE ---")

    continente_buscado = seleccionar_continente(True)

    if continente_buscado == "":
        print("Volviendo al menú de filtros.")
        return

    resultados = []

    for pais in paises:
        if normalizar_texto(pais["continente"]) == normalizar_texto(continente_buscado):
            resultados.append(pais)

    if len(resultados) == 0:
        print("No se encontraron países para ese continente.")
    else:
        print("\nPaíses encontrados:")
        mostrar_paises(resultados)


# ---------------------------------------------------------
# FUNCIÓN PARA FILTRAR POR RANGO DE POBLACIÓN
# ---------------------------------------------------------
def filtrar_por_rango_poblacion(paises):
    print("\n--- FILTRAR POR RANGO DE POBLACIÓN ---")

    while True:
        poblacion_minima = leer_entero_no_negativo("Ingrese la población mínima: ")
        poblacion_maxima = leer_entero_no_negativo("Ingrese la población máxima: ")

        if poblacion_minima > poblacion_maxima:
            print("Error: la población mínima no puede ser mayor que la población máxima.")
        else:
            break

    resultados = []

    for pais in paises:
        if pais["poblacion"] >= poblacion_minima and pais["poblacion"] <= poblacion_maxima:
            resultados.append(pais)

    if len(resultados) == 0:
        print("No se encontraron países dentro de ese rango de población.")
    else:
        print("\nPaíses encontrados:")
        mostrar_paises(resultados)


# ---------------------------------------------------------
# FUNCIÓN PARA FILTRAR POR RANGO DE SUPERFICIE
# ---------------------------------------------------------
def filtrar_por_rango_superficie(paises):
    print("\n--- FILTRAR POR RANGO DE SUPERFICIE ---")

    while True:
        superficie_minima = leer_entero_no_negativo("Ingrese la superficie mínima en km²: ")
        superficie_maxima = leer_entero_no_negativo("Ingrese la superficie máxima en km²: ")

        if superficie_minima > superficie_maxima:
            print("Error: la superficie mínima no puede ser mayor que la superficie máxima.")
        else:
            break

    resultados = []

    for pais in paises:
        if pais["superficie"] >= superficie_minima and pais["superficie"] <= superficie_maxima:
            resultados.append(pais)

    if len(resultados) == 0:
        print("No se encontraron países dentro de ese rango de superficie.")
    else:
        print("\nPaíses encontrados:")
        mostrar_paises(resultados)


# ---------------------------------------------------------
# FUNCIÓN PARA FILTRAR PAÍSES
# ---------------------------------------------------------
def filtrar_paises(paises):
    if len(paises) == 0:
        print("No hay países cargados para filtrar.")
        return

    while True:
        print("\n--- FILTRAR PAÍSES ---")
        print("1. Filtrar por continente")
        print("2. Filtrar por rango de población")
        print("3. Filtrar por rango de superficie")
        print("4. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            filtrar_por_continente(paises)

        elif opcion == "2":
            filtrar_por_rango_poblacion(paises)

        elif opcion == "3":
            filtrar_por_rango_superficie(paises)

        elif opcion == "4":
            print("Volviendo al menú principal.")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


# ---------------------------------------------------------
# FUNCIONES AUXILIARES PARA ORDENAMIENTO
# ---------------------------------------------------------
def obtener_nombre(pais):
    return normalizar_texto(pais["nombre"])


def obtener_poblacion(pais):
    return pais["poblacion"]


def obtener_superficie(pais):
    return pais["superficie"]


# ---------------------------------------------------------
# FUNCIÓN PARA ELEGIR SENTIDO DEL ORDENAMIENTO
# ---------------------------------------------------------
def elegir_orden_descendente():
    while True:
        print("\nSeleccione el tipo de orden:")
        print("1. Ascendente")
        print("2. Descendente")
        print("3. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            return False
        elif opcion == "2":
            return True
        elif opcion == "3":
            return None
        else:
            print("Opción inválida. Intente nuevamente.")


# ---------------------------------------------------------
# FUNCIÓN PARA ORDENAR PAÍSES
# ---------------------------------------------------------
def ordenar_paises(paises):
    if len(paises) == 0:
        print("No hay países cargados para ordenar.")
        return

    while True:
        print("\n--- ORDENAR PAÍSES ---")
        print("1. Ordenar por nombre")
        print("2. Ordenar por población")
        print("3. Ordenar por superficie")
        print("4. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            descendente = elegir_orden_descendente()

            if descendente is None:
                print("Volviendo al menú de ordenamiento.")
            else:
                paises_ordenados = paises.copy()
                paises_ordenados.sort(key=obtener_nombre, reverse=descendente)

                print("\nPaíses ordenados por nombre:")
                mostrar_paises(paises_ordenados)

        elif opcion == "2":
            descendente = elegir_orden_descendente()

            if descendente is None:
                print("Volviendo al menú de ordenamiento.")
            else:
                paises_ordenados = paises.copy()
                paises_ordenados.sort(key=obtener_poblacion, reverse=descendente)

                print("\nPaíses ordenados por población:")
                mostrar_paises(paises_ordenados)

        elif opcion == "3":
            descendente = elegir_orden_descendente()

            if descendente is None:
                print("Volviendo al menú de ordenamiento.")
            else:
                paises_ordenados = paises.copy()
                paises_ordenados.sort(key=obtener_superficie, reverse=descendente)

                print("\nPaíses ordenados por superficie:")
                mostrar_paises(paises_ordenados)

        elif opcion == "4":
            print("Volviendo al menú principal.")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


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
            actualizar_pais(paises)

        elif opcion == "4":
            buscar_pais_por_nombre(paises)

        elif opcion == "5":
            filtrar_paises(paises)

        elif opcion == "6":
            ordenar_paises(paises)

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