# Trabajo Práctico Integrador - Programación 1

## Tema

**Gestión de Datos de Países en Python: filtros, ordenamientos y estadísticas**

## Descripción del proyecto

Este proyecto fue desarrollado como Trabajo Práctico Integrador de la materia **Programación 1** de la Tecnicatura Universitaria en Programación.

El sistema permite gestionar información de países utilizando Python. Los datos se cargan desde un archivo CSV y se almacenan en una lista de diccionarios. A partir de esa estructura, el programa permite agregar países, actualizar datos, buscar, filtrar, ordenar y calcular estadísticas básicas.

El programa funciona por consola mediante un menú interactivo.

## Funcionalidades principales

El sistema permite:

1. Mostrar todos los países cargados.
2. Agregar un nuevo país.
3. Actualizar la población y/o superficie de un país.
4. Buscar países por nombre, con coincidencia parcial o exacta.
5. Filtrar países por:

   * Continente.
   * Rango de población.
   * Rango de superficie.
6. Ordenar países por:

   * Nombre.
   * Población.
   * Superficie.
   * En orden ascendente o descendente.
7. Mostrar estadísticas:

   * País con mayor población.
   * País con menor población.
   * Promedio de población.
   * Promedio de superficie.
   * Cantidad de países por continente.
8. Salir del programa.

## Estructura de datos utilizada

El programa trabaja con una **lista de diccionarios**.

Cada país se representa mediante un diccionario con las siguientes claves:

* `nombre`
* `poblacion`
* `superficie`
* `continente`

Ejemplo:

```python
{
    "nombre": "Argentina",
    "poblacion": 45376763,
    "superficie": 2780400,
    "continente": "América"
}
```

Todos los países se almacenan dentro de una lista llamada `paises`.

## Archivos del proyecto

* `main.py`: contiene el código principal del programa.
* `paises.csv`: contiene el dataset base de países.
* `README.md`: contiene la descripción del proyecto, instrucciones de uso y ejemplos.

## Formato del archivo CSV

El archivo `paises.csv` utiliza el siguiente formato:

```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
Japón,125800000,377975,Asia
Brasil,213993437,8515767,América
```

## Instrucciones de uso

1. Descargar o clonar el repositorio.
2. Abrir la carpeta del proyecto en Visual Studio Code o en otro editor.
3. Verificar que los archivos `main.py` y `paises.csv` estén en la misma carpeta.
4. Ejecutar el archivo `main.py` con Python 3.
5. Utilizar el menú de consola para elegir la operación deseada.

Comando de ejecución:

```bash
python main.py
```

## Ejemplos de uso

### Mostrar países

Entrada:

```text
1
```

Salida esperada:

```text
Nombre: Argentina
Población: 45376763
Superficie: 2780400 km²
Continente: América
```

### Agregar un país

Entrada de ejemplo:

```text
2
Nombre: Perú
Población: 33720000
Superficie: 1285216
Continente: América
```

Salida esperada:

```text
Archivo CSV actualizado correctamente.
País agregado correctamente.
```

### Buscar país por nombre

Entrada:

```text
4
ar
```

Salida esperada:

```text
Países encontrados:
Argentina
```

### Filtrar por continente

Entrada:

```text
5
1
América
```

Salida esperada:

```text
Países encontrados:
Argentina
Brasil
Chile
Uruguay
```

### Ordenar por población descendente

Entrada:

```text
6
2
2
```

Salida esperada:

```text
Países ordenados por población:
India
China
Brasil
...
```

### Mostrar estadísticas

Entrada:

```text
7
```

Salida esperada:

```text
País con mayor población:
Nombre: India

País con menor población:
Nombre: Uruguay

Promedio de población: ...
Promedio de superficie: ...

Cantidad de países por continente:
América: ...
Europa: ...
Asia: ...
África: ...
Oceanía: ...
```

## Validaciones implementadas

El programa incluye validaciones para:

* Evitar campos vacíos.
* Evitar nombres de países con números o símbolos.
* Evitar continentes mal escritos mediante selección por menú.
* Evitar países duplicados, incluso si se escriben con o sin acento.
* Validar que población y superficie sean números enteros positivos.
* Controlar errores de formato en el archivo CSV.
* Informar cuando una búsqueda o filtro no tiene resultados.
* Controlar opciones inválidas en los menús.

## Persistencia de datos

El sistema lee los datos desde el archivo `paises.csv`.

Cuando se agrega un país o se actualizan datos de población o superficie, el programa vuelve a guardar la información actualizada en el archivo CSV. De esta manera, los cambios no se pierden al cerrar el programa.

## Conceptos aplicados

En este proyecto se aplicaron los siguientes contenidos de Programación 1:

* Variables.
* Entrada y salida de datos.
* Condicionales.
* Bucles `while` y `for`.
* Listas.
* Diccionarios.
* Funciones.
* Parámetros y retorno de valores.
* Archivos CSV.
* Manejo básico de errores.
* Validaciones.
* Ordenamientos.
* Estadísticas básicas.

## Integrante

* Nombre y apellido: Alessandra Borges Licciardi

## Enlaces

* Video demostrativo: a completar
* Informe PDF: a completar

## Estado del proyecto

Proyecto funcional finalizado para entrega académica.
