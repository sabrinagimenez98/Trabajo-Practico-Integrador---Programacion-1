# Trabajo Práctico Integrador – Programación 1
## Gestión de Países con archivos CSV

### 📌 Descripción del programa
Este proyecto es una aplicación de consola escrita en Python que administra un registro de países almacenado en un archivo CSV.  
Permite realizar tareas variadas de consulta, búsqueda, filtrado, ordenamiento y estadísticas sobre cada país, además de agregar y eliminar registros.

Cada país del dataset posee:
- **Nombre**
- **Población**
- **Superficie (km²)**
- **Continente**

El sistema trabaja leyendo y escribiendo datos directamente en `paises.csv` utilizando diccionarios, listas y manejo de archivos con la librería `csv`.

---

### ✅ Funcionalidades principales
✔ Mostrar todos los países registrados en formato tabla  
✔ Buscar país por nombre
✔ Filtrar por:
- Continente
- Rango de población
- Rango de superficie

✔ Ordenar por:
- Nombre
- Población
- Superficie  
(en forma ascendente o descendente)

✔ Estadísticas:
- País con mayor población
- País con menor población
- Promedio de población
- Promedio de superficie
- Cantidad de países por continente

✔ Agregar un país al archivo  
✔ Eliminar un país por nombre  
✔ Verificación y validación de entradas del usuario  
✔ Manejo de errores y registros con formato incorrecto  

---

### 📜 Instrucciones de uso

1. **Requisitos**
   - Python **3.10+** (necesario porque se usa `match/case`)
   - Librerías estándar de Python (no requiere instalación extra)

2. **Ejecución**
   - Abrir la carpeta del proyecto
   - Ejecutar el archivo principal:
     
     python PRACTICA_INTEGRADO.py
   
   - Se mostrará un menú numérico con opciones.

3. **Archivo CSV**
   - No es necesario crearlo manualmente.
   - Si no existe `paises.csv`, el programa lo inicializa automáticamente.
   - Las modificaciones (agregar, eliminar, ordenar) quedan guardadas en el archivo.

---

### 🧪 Ejemplos de uso

#### ✅ Ejemplo 1 – Mostrar países
**Entrada (usuario): 1**
<img width="843" height="437" alt="imagen" src="https://github.com/user-attachments/assets/0990559a-6f13-4a97-92dc-9ce45a50510c" />

