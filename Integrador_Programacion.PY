from funciones import mostrar_paises, buscar_pais, agregar_pais,eliminar_pais
from ordenamientos import ordenar_paises
from estadisticas import mostrar_estadisticas
from filtros import filtrar_paises

#--------------------------
# RUTA ARCHIVO
#--------------------------

RUTA_ARCHIVO = "ARCHIVO_PAISES\\paises.csv"

def menu():
    
    while True:
        try:
            print("=" * 30)
                
            print(" ==== Menú de opciones: ====\n")
            print("|1. Mostrar todos los paises: ")
            print("|2. Buscar pais (por nombre): ")
            print("|3. Filtrar paises: ")
            print("|4. Ordenar paises: ")
            print("|5. Mostrar estadisticas: ")
            print("|6. Agregar pais: ")
            print("|7. Eliminar pais: ")
            print("|8. Salir")
                
            print("=" * 30)
                
            opcion = int(input("\n- Seleccione una opción: "))
                
            match opcion:
                case 1:
                    mostrar_paises()
                case 2:
                    buscar_pais()
                case 3:
                    filtrar_paises()
                case 4:
                    ordenar_paises()
                case 5:
                    mostrar_estadisticas()
                case 6:
                    agregar_pais()
                case 7:
                    eliminar_pais()
                case 8:
                    print("- Saliendo del programa....... Hasta luego!")
                    break
                case _:
                    print("Opción no válida. Intente de nuevo.")

        except ValueError:
            print("=" * 30)
            print("ERROR. No puede ingresar algo que no sea un numero. Intentelo de nuevo... ")


#--------------------------
#PRINCIPAL
#--------------------------

menu()