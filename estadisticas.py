from funciones import RUTA_ARCHIVO,inicializar_archivo
import csv

#------------------------------------------
#ESTADISTICAS
#------------------------------------------

def pais_menor_mayor():
    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            
            primera = True
            nombre_mayor = nombre_menor = None
            may_poblacion = None
            men_poblacion = None

            for fila in lector:
                try:
                    pobl = int(fila["poblacion"])
                except (ValueError, KeyError):
                    continue
                
                if primera:
                    may_poblacion = men_poblacion = pobl
                    nombre_mayor = nombre_menor = fila["nombre"]
                    primera = False
                    
                else:
                    if pobl > may_poblacion:
                        may_poblacion = pobl
                        nombre_mayor = fila["nombre"]
                        
                    if pobl < men_poblacion:
                        men_poblacion = pobl
                        nombre_menor = fila["nombre"]

            if primera:
                print("No hay paises con poblacion valida.")
                return

            print(f"|Pais con mayor poblacion: {nombre_mayor} |Poblacion: {may_poblacion}")
            print(f"|Pais con menor poblacion: {nombre_menor} |Poblacion: {men_poblacion}")

    except FileNotFoundError:
        inicializar_archivo()

def promedio_poblacion():
    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            paises = list(lector)
            
            suma_poblacion = 0
            
            #Suma de la poblacion de cada pais.
            for fila in paises:
                try:
                    suma_poblacion += int(fila["poblacion"])
                except ValueError:
                    continue
            
            #Promedio total
            
            try:
                prom_poblacion = suma_poblacion / len(paises)
            except ZeroDivisionError:
                print("ERROR. Valor invalido para division..")
            
            print("\n" + "=" * 30)
            print(f"|El promedio de poblacion mundial es de: {round(prom_poblacion)}")
            
    except FileNotFoundError:
        print(" El archivo no existe. Creando uno nuevo...")
        inicializar_archivo()

def promedio_superficie():
    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            paises = list(lector)
            
            suma_superficie = 0
            
            #Suma de la superficie de cada pais
            for fila in paises:
                try:
                    suma_superficie += float(fila["superficie"])
                except ValueError:
                    continue
            
            #Promedio total
            prom_superficie = suma_superficie / len(paises)
            
            print("\n" + "=" * 30)
            print(f"|El promedio de la superficie mundial es de: {round(prom_superficie,2)}")
            
    except FileNotFoundError:
        print(" El archivo no existe. Creando uno nuevo...")
        inicializar_archivo()

def paises_por_continente():
    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            paises = list(lector)
            
            #Diccionario de continentes vacio
            conteo_continentes = {}

            for pais in paises:
                
                #Asignacion de continente
                continente = pais["continente"].strip().capitalize()
                
                #Verificacion si suma al contador del continente
                if continente in conteo_continentes:
                    conteo_continentes[continente] += 1
                    
                #Verificacion si ingresa un nuevo continente
                else:
                    conteo_continentes[continente] = 1
                
            for continente, cantidad in conteo_continentes.items():
                print(f"|Continente {continente} | Cantidad de paises: {cantidad}")
                
                
    except FileNotFoundError:
        print(" El archivo no existe. Creando uno nuevo...")
        inicializar_archivo()

def mostrar_estadisticas():
    print("\n" + "=" * 30)
    print("\n- Tipos de estadisticas:\n ")
    
    print("|1. Pais con menor y mayor poblacion")
    print("|2. Promedio de poblacion")
    print("|3. Promedio de superficie")
    print("|4. Cantidad de paises por continente")
    
    try:
        
        opc = int(input("\n- Ingrese una opcion de estadistica: "))
        print("\n" + "=" * 30)
        
        match opc:
            case 1:
                pais_menor_mayor()
            case 2:
                promedio_poblacion()
            case 3:
                promedio_superficie()
            case 4:
                paises_por_continente()
            case _:
                print("No puede ingresar numero negativos. Intentelo de nuevo...")
                return
        
    except ValueError:
        print("ERROR. No puede ingresar letras. Intentelo de nuevo...")
