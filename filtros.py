import csv
from utils import quitar_tildes
from funciones import inicializar_archivo

RUTA_ARCHIVO = "ARCHIVO_PAISES\\paises.csv"

#------------------------------------------
#FILTROS
#------------------------------------------

def filtrado_continente():
    
    continentes_validos = ["america","europa","asia","africa","oceania","antartida"]
    
    continente = input("Ingrese el contiente con el que desea filtrar: ").strip()
    
    #Verificaciones de continente
    if not continente:
        print("\n" + "=" * 30)
        print("Entrada vacia. Intentelo de nuevo...")
        return
    
    if continente.isdigit():
        print("\n" + "=" * 30)
        print("No puede ingresar numero. Intentelo de nuevo...")
        return
    
    if continente not in continentes_validos:
        print("\n" + "=" * 30)
        print("El continente ingresado no existe. Intentelo de nuevo...")
        return
    
    
    cont_sin_tildes = quitar_tildes(continente.lower())
    
    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            encontrados = []
            
            for fila in lector:
                if quitar_tildes(fila["continente"].lower()) == cont_sin_tildes:
                    encontrados.append(fila)
            
            if encontrados:
                print(f"\nPaises del continente de {continente}: \n")
                    
                print("-" * 70)
                print(f"{'Nombre':<20} {'Población':<17} {'Superficie':<10} {'Continente':>15}")
                print("-" * 70)

                    
                for pais in encontrados:
                        nombre = pais["nombre"]
                        poblacion = int(pais["poblacion"])
                        superficie = float(pais["superficie"])
                        continente = pais["continente"]

                        print(f"{nombre:<20} | {poblacion:>12} | {superficie:>14} | {continente:>15} |")
                
    except FileNotFoundError:
        print(" El archivo no existe. Creando uno nuevo...")
        inicializar_archivo()

def filtrado_rango_poblacion():
    try:
        
        #Entrada de usuario y validaciones
        pobl_min = int(input("Ingrese la poblacion minima: "))
        
        if not pobl_min:
            print("\n" + "=" * 30)
            print("Entrada vacia. Intentelo de nuevo...")
            return
        
        pobl_max = int(input("Ingrese la poblacion maxima: "))
        
        if not pobl_max:
            print("\n" + "=" * 30)
            print("Entrada vacia. Intentelo de nuevo...")
            return
        
        
    except ValueError:
        print("\n" + "=" * 30)
        print("No puede ingresar letras. Intentelo de nuevo...")
        return
    
    try:
        
        #Apertura de archivo
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            encontrados = []
            
            #Busqueda de las poblacion solicitadas
            for fila in lector:
                try:
                    poblacion = int(fila["poblacion"])
                    
                    if pobl_min <= poblacion <= pobl_max:
                        encontrados.append(fila)
                    
                except ValueError:
                    continue
            
            #Escritura de la poblacion solicitadas
            if encontrados:
                
                print("\n" + "=" * 30)
                print(f"|Paises con poblacion entre {pobl_min} y {pobl_max} de habitantes: \n")
                
                print("-" * 70)
                print(f"{'Nombre':<20} {'Población':<17} {'Superficie':<10} {'Continente':>15}")
                print("-" * 70)
                    
                for pais in encontrados:
                    nombre = pais["nombre"]
                    poblacion = int(pais["poblacion"])
                    superficie = float(pais["superficie"])
                    continente = pais["continente"]

                    print(f"{nombre:<20} | {poblacion:<17} | {superficie:<10} | {continente:>15}")
    except FileNotFoundError:
        print(" El archivo no existe. Creando uno nuevo...")
        inicializar_archivo()

def filtrado_superficie():
    
    try:
        
        #Entrada de usuario y validaciones.
        sup_min = int(input("Ingrese la superficie minima: "))
        
        if not sup_min:
            print("\n" + "=" * 30)
            print("Entrada vacia. Intentelo de nuevo...")
            return
        
        sup_max = int(input("Ingrese la superficie maxima: "))
        
        if not sup_max:
            print("\n" + "=" * 30)
            print("Entrada vacia. Intentelo de nuevo...")
            return
        
    except ValueError:
        print("\n" + "=" * 30)
        print("No puede ingresar letras. Intentelo de nuevo...")
        return

    try:
        
        #Apertura de archivo
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            encontrados = []
            
            
            #Busqueda de las superficies solicitadas
            for fila in lector:
                try:
                    superficie = float(fila["superficie"])
                    
                    if sup_min <= superficie <= sup_max:
                        encontrados.append(fila)
                    
                except ValueError:
                    continue
            
            
            #Escritura de las superficies solicitadas
            if encontrados:
                
                print(f"\n|Paises con superficie entre {sup_min} y {sup_max} \n")
                
                print("-" * 70)
                print(f"{'Nombre':<20} {'Población':<17} {'Superficie':<10} {'Continente':>15}")
                print("-" * 70)
                    
                for pais in encontrados:
                    nombre = pais["nombre"]
                    poblacion = int(pais["poblacion"])
                    superficie = float(pais["superficie"])
                    continente = pais["continente"]

                    print(f"{nombre:<20} | {poblacion:<17} | {superficie:<10} | {continente:>15}")
                print("-" * 70)
                
    except FileNotFoundError:
        inicializar_archivo()

def filtrar_paises():
    
    print("\n" + "=" * 30)
    print("|Tipos de filtro: \n")
    
    print("|1. Filtrar por continente")
    print("|2. Filtrar por rango de poblacion")
    print("|3. Filtrar por rango de superficie")
    
    try:
        
        opc = int(input("\n-Seleccione una opción de filtro: "))
        print("\n" + "=" * 30)
        
        match opc:
            case 1:
                filtrado_continente()
            case 2:
                filtrado_rango_poblacion()
            case 3:
                filtrado_superficie()
            case _:
                print("Valor invalido. Intentelo de nuevo..")
                return
        
    except ValueError:
        print("\n" + "=" * 30)
        print("ERROR. No puede ingresar letras. Intentelo de nuevo...")
