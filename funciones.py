import csv, os
from utils import quitar_tildes

RUTA_ARCHIVO = "ARCHIVO_PAISES/paises.csv"

#--------------------------
#FUNCIONES PROGRAMA
#------------------------- 

#Funcion para crear archivo si no existe
def inicializar_archivo():
    if not os.path.exists("paises.csv"):
        with open("paises.csv", "w", encoding="utf-8",newline="") as archivo:
            
            #nombre de las Claves/Encabezados
            encabezados = ["nombre", "poblacion", "superficie", "continente"]
            
            #Crea una lista de diccionarios y toma la primer linea/fila como encabezados como (key), y los demas como (value)
            escritor = csv.DictWriter(archivo, fieldnames=encabezados) 
            
            #escribe los encabezados en el archivo
            escritor.writeheader()

#--------------------------
#FUNCIONES MENU
#--------------------------

def mostrar_paises():
    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            
            #lee el contenido del archivo como lista de diccionarios
            contenido = csv.DictReader(archivo)
            contenido = list(contenido)
            
            if not contenido:
                print("No hay países registrados.")
                return
            
            # Encabezado con ancho fijo
            print("-" * 70)
            print(f"{'Nombre':<20} {'Población':<17} {'Superficie':<10} {'Continente':>15}")
            print("-" * 70)

            contenido_valido = []
                
            #Paises
            for fila in contenido:
                try: 
                    nombre = fila['nombre']
                    poblacion = int(fila['poblacion'])
                    superficie = float(fila['superficie'])
                    continente = fila['continente']

                    print(f"{nombre:<20} | {poblacion:>12} | {superficie:>14} | {continente:>15} |")
                    
                    contenido_valido.append(fila)
                    
                except ValueError:
                    #elimina paises con errores de formato
                    print(f"- País {fila.get('nombre')}' eliminado por error de formato.")
            print("-" * 70)
            
            
        #Sobrescribo el csv original
        if contenido_valido:
            with open(RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
                encabezado = ["nombre","poblacion","superficie","continente"]
                escritor = csv.DictWriter(archivo, fieldnames=encabezado)
                escritor.writeheader()
                escritor.writerows(contenido_valido)
        
    except FileNotFoundError:
        print("El archivo no existe. Creando uno nuevo....")
        inicializar_archivo()

def buscar_pais():
    
    pais_buscar = input("\nIngrese el nombre del pais que desea buscar: ").strip()
    
    if not pais_buscar:
        print("\n" + "=" * 30)
        print("Entrada vacia. Intentelo de nuevo...")
        return
    
    if pais_buscar.isdigit():
        print("\n" + "=" * 30)
        print("No puede ingresar numeros. Intentelo de nuevo...")
        return
    
    #Quito las tildes al pais ingresado para la comparacion.
    pais_sin_tildes = quitar_tildes(pais_buscar.lower()) 
    
    encontrado = False
    
    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            
            for fila in lector:
                
                #Quito las tildes del pais que esta dentro del CSV
                nombre_sin_tildes = quitar_tildes(fila["nombre"].lower())
                
                #Comparacion
                if nombre_sin_tildes == pais_sin_tildes:
                    
                    print(f"\n{'=' * 30}")
                    print("|Pais Encontrado: ")
                    print(f"|Nombre: {fila['nombre']} | Poblacion: {fila['poblacion']} | Superficie: {fila['superficie']} | Continente: {fila['continente']}")
                    
                    encontrado = True
                    break
                
            if not encontrado:
                print("EL pais ingresado no se encuentra en el registro.")
                
    except FileNotFoundError:
        print("El archivo no existe. Creando uno nuevo....")
        inicializar_archivo()

def agregar_pais():
    
    continentes_validos = ["america","europa","asia","africa","oceania","antartida"]
    
    #-----------------------------------------------------------------------
    #Entradas del usuario y verificaciones
    #-----------------------------------------------------------------------
    
    #------------------------------------------------------------------------
    #Entrada y validacion de nombre de pais
    nuevo_nombre = str(input("\n-Ingrese el nombre del pais a ingresar: ").strip())
    if not nuevo_nombre or nuevo_nombre.isdigit():
        
        print("=" * 30)
        print("Entrada vacia o valor incorrecto. Intentelo de nuevo...")
        return
    
    with open(RUTA_ARCHIVO, "r",encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        paises = list(lector)
        
        #Verificacion para saber si existe dentro del csv
        for pais in paises:
            
            if quitar_tildes(pais["nombre"].lower()) == quitar_tildes(nuevo_nombre.lower()):
                print("El pais ingresado ya se encuentra dentro del sistema..")
                return
    
    #------------------------------------------------------------------------
    
    #------------------------------------------------------------------------
    #Entrada y validacion de poblacion
    nuevo_poblacion = input("-Ingrese la poblacion del pais: ").strip()
    if not nuevo_poblacion.isdigit() or int(nuevo_poblacion) < 0:
        
        print("=" * 30)
        print("No puede ingresar letras o numeros negativos. Intentelo de nuevo....")
        return
    #------------------------------------------------------------------------
    
    #------------------------------------------------------------------------
    #Entrada y validacion de superficie
    nuevo_superficie = input("-Ingrese la superficie del pais: ").strip()
    
    try:
        if int(nuevo_superficie) < 0:
            
            print("=" * 30)
            print("No puede ingresar letras o numeros negativos. Intentelo de nuevo....")
            return
    except ValueError:
        print("=" * 30)
        print("La superficie debe ser un numero valido. intentelo de nuevo....")
        return
    #------------------------------------------------------------------------
    
    #------------------------------------------------------------------------
    #Entrada y validacion de continente
    nuevo_continente = str(input("-Ingrese el contienten del pais: ").strip())
    if nuevo_continente not in continentes_validos:
    
        print("=" * 30)
        print("El continente ingresado no existe. Intentelo de nuevo")
        return
    #---------------------------------------------------------------------------
    
    #Creacion de la fila del pais
    nuevo_pais = {"nombre": nuevo_nombre.capitalize(), "poblacion": nuevo_poblacion, "superficie": nuevo_superficie, "continente": nuevo_continente.capitalize()}
    
    try:
        
        #Escritura de la nueva fila
        with open(RUTA_ARCHIVO, "a", newline="") as archivo:
            encabezados = ["nombre","poblacion", "superficie", "continente"]
            escritor = csv.DictWriter(archivo, fieldnames=encabezados)
            escritor.writerow(nuevo_pais)
        print("\n|Pais agregado con exito.")

    except FileNotFoundError:
        print(" El archivo no existe. Creando uno nuevo...")
        inicializar_archivo()

    except csv.Error:
        print("Error al procesar el archivo CSV. Verifique el formato.")

def eliminar_pais():
    
    pais_eliminar = str(input("\n-Ingrese el pais que desea eliminar: ")).strip()
    
    #Entrada vacia
    if not pais_eliminar:
        print("Entrada vacia. Intentelo de nuevo.")
        return
    
    #Existencia de archivo
    if not os.path.exists(RUTA_ARCHIVO):
        print("El archivo no existe. Creando uno nuevo...")
        inicializar_archivo()
        return
    
    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            
            lector = csv.DictReader(archivo)
            paises = list(lector)
            
            encontrado = False
            paises_modificado = []
            
            #Busqueda del pais ingresado por el usuario
            for pais in paises:
                if quitar_tildes(pais["nombre"].lower()) == quitar_tildes(pais_eliminar.lower()):
                    encontrado = True
                else:
                    paises_modificado.append(pais)
            
            
            #Escritura del nuevo archivo (sin el pais eliminado)
            if encontrado:
            
                with open(RUTA_ARCHIVO, "w", encoding="utf-8", newline="") as archivo:
                    encabezado = ["nombre", "poblacion", "superficie", "continente"]
                    escritor = csv.DictWriter(archivo, fieldnames=encabezado)
                    escritor.writeheader()
                    escritor.writerows(paises_modificado)
                
                print("=" * 30)
                print("\n|Pais eliminado con exito -")
            
            else:
                print("=" * 30)
                print("El pais ingresado no se encuentra en el sistema. ")
        
    except csv.Error:
        print("Error al procesar el archivo CSV. Verifique el formato.")
