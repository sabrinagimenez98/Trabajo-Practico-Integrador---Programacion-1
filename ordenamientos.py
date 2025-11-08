from funciones import RUTA_ARCHIVO, inicializar_archivo
import csv


#------------------------------------------
#ORDENAMIENTOS
#------------------------------------------

def buscar_nombre(pais):
    return pais["nombre"].lower()
def ordenamiento_nombre():
    try:
        
        #Apertura de archivo
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            paises = list(lector)
            
            if not paises:
                print("\n" + "=" * 30)
                print("El archivo esta vacio. No hay paises para ordenar.")
            
            paises_ordenados = sorted(paises, key=buscar_nombre)

            #Se sobrescribe el CSV original por el nuevo ordenado
            with open(RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
                encabezado = ["nombre", "poblacion","superficie","continente"]
                escritor = csv.DictWriter(archivo, fieldnames=encabezado)
                escritor.writeheader()
                escritor.writerows(paises_ordenados)
            print("\n" + "=" * 30)
            print("Paises ordenado correctamente.")
            
    except FileNotFoundError:
        print(" El archivo no existe. Creando uno nuevo...")
        inicializar_archivo()

def obtener_poblacion(pais):
    return int(pais["poblacion"])
def ordenamiento_poblacion(opcion):
    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            paises = list(lector)
            
            if not paises:
                print("\n" + "=" * 30)
                print("El archivo esta vacio. No hay paises para ordenar.")
            
            #Ordenamiento Ascendente y Descendente (a/d)
            if opcion == "a":
                ordenados_poblacion = sorted(paises, key=obtener_poblacion)
                print("\n" + "=" * 30)
                print("- Paises ordenados ascendentemente -.")
                
            elif opcion == "d":
                ordenados_poblacion = sorted(paises, key=obtener_poblacion, reverse=True)
                print("\n" + "=" * 30)
                print("- Paises ordenados descendentemente - .")
            
            #Se sobreescribe el CSV original por el nuevo ordenado
            with open(RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
                encabezado = ["nombre","poblacion","superficie","continente"]
                escritor = csv.DictWriter(archivo, fieldnames=encabezado)
                escritor.writeheader()
                escritor.writerows(ordenados_poblacion)
            
            
    except FileNotFoundError:
        print(" El archivo no existe. Creando uno nuevo...")
        inicializar_archivo()

def obtener_superficie(pais):
    return float(pais["superficie"])
def ordenamiento_superficie(opcion):
    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            paises = list(lector)
            
            if not paises:
                print("\n" + "=" * 30)
                print("El archivo esta vacio. No hay paises para ordenar.")
            
            #Ordenamiento Ascendente o Descendente (a/d)
            if opcion == "a":
                ordenados_superficie = sorted(paises, key=obtener_superficie)
                print("- Paises ordenados ascendentemente -.")
                
            elif opcion == "d":
                ordenados_superficie = sorted(paises, key=obtener_superficie, reverse=True)
                print("- Paises ordenados descendentemente - .")
            
            #Sobreescribo el CSV original por el nuevo ordenado
            with open(RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
                encabezado = ["nombre","poblacion","superficie","continente"]
                escritor = csv.DictWriter(archivo, fieldnames=encabezado)
                escritor.writeheader()
                escritor.writerows(ordenados_superficie)
            
            
    except FileNotFoundError:
        print(" El archivo no existe. Creando uno nuevo...")
        inicializar_archivo()

def ordenar_paises():
    
    print("\n" + "=" * 30)
    print("\n- Tipos de ordenamiento:\n ")
    
    print("|1. Por nombre")
    print("|2. Por poblacion  (ascendente o descendente)")
    print("|3. Por superficie (ascendente o descendente)")
    
    try:
        opc = int(input("\n- Ingrese una opcion de ordenamiento: "))
        print("\n" + "=" * 30)
        
        match opc:
            
            #Ordenar alfabeticamente
            case 1:
                ordenamiento_nombre()
            
            
            #Ordenar por poblacion (ascendente o descendente)
            case 2:
                print("|Ascendente  (a)")
                print("|Descendente (d)")
                
                try:
                    opcion = input("\n- Elige una opcion: ").lower()
                    
                    match opcion:
                        case "a":
                            ordenamiento_poblacion(opcion)
                        case "d":
                            ordenamiento_poblacion(opcion)
                        case _:
                            print("\n" + "=" * 30)
                            print("Valor invalido. Intentelo de nuevo...")
                            return
                except ValueError:
                    print("\n" + "=" * 30)
                    print("ERROR. No puede ingresar numeros. Intentelo de nuevo...")

            #Ordenar por superficie (ascendente o descendente)
            case 3:
                print("|Ascendente  (a)")
                print("|Descendente (d)")
                
                try:
                    opcion = input("\n- Elige una opcion: ").lower()

                    match opcion:
                        case "a":
                            ordenamiento_superficie(opcion)
                        case "d":
                            ordenamiento_superficie(opcion)
                except ValueError:
                    print("\n" + "=" * 30)
                    print("ERROR. No puede ingresar numeros. Intentelo de nuevo...")
        
    except ValueError:
        print("\n" + "=" * 30)
        print("ERROR. No puede ingresar letras. Intentelo de nuevo...")