# 💻 Trabajo Practico Integrador - Programacion 1 💻
## 📕 Integrantes
- Sabrina gimenez
- Ismael Saleme

## 💻 Descripcion del programa:
### Este proyecto es una aplicación de consola en Python para gestionar un pequeño dataset de países almacenado en un archivo CSV (paises.csv). 

#### El programa ofrece un menú interactivo con opciones para:

- **mostrar todos los países**
- **buscar un país por nombre**
- **filtrar por continente / rango de población / rango de superficie**
- **ordenar por nombre/población/superficie (asc/desc)**
- **ver estadísticas (mayor/menor población, promedios, conteo por continente)**
- **agregar y eliminar países.**

#### El código está dividido en dos partes principales:

- **PRACTICA_INTEGRADO.PY** — script principal: contiene el menú, funciones de entrada/salida con el usuario (imprimir, solicitar inputs), y algunas utilidades (por ejemplo quitar_tildes() y inicializar_archivo()). Todas las operaciones del menú invocan funciones aquí o llaman al módulo de apoyo. 
- **fcs_fIltrado_paises.py** — módulo auxiliar: contiene la mayoría de los filtros, ordenamientos y estadísticas (funciones que trabajan con el CSV y devuelven/impresionan resultados). El principal script llama a estas funciones cuando el usuario escoge filtrar, ordenar o pedir estadísticas.
