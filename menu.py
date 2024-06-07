from biblioteca_menu import *
from biblioteca_json import *
from biblioteca_mostrar import *
from biblioteca_calculos import *


menu = pedir_opcion()

lista_data = []

while True:

    match menu:

        # ------------------- Cargar Archivos ---------------------
        
        case 1:

            nombre_archivo = input("Ingrese el nombre del archivo a cargar: ")
            
            lista_data = cargar_archivo(nombre_archivo)

            respuesta = pedir_respuesta()

            if respuesta == "SI":
                menu = pedir_opcion()
            else:
                break

        # ------------------- Iprimir Lista -----------------------

        case 2:

            imprimir_lista(lista_data)

            respuesta = pedir_respuesta()

            if respuesta == "SI":
                menu = pedir_opcion()
            else:
                break

        # ------------------- Asingar Totales ---------------------

        case 3:

            asignar_totales(lista_data)

            respuesta = pedir_respuesta()

            if respuesta == "SI":
                menu = pedir_opcion()
            else:
                break

        # ------------------- Filtrar por tipo ---------------------
        
        case 4:

            filtro = int(input("Ingrese el tipo de servicio que desea: "))

            servicios_filtrados = filtrar_por_tipo(lista_data, filtro)

            escribir_archivo(servicios_filtrados, "tipo_servicio.json")


            respuesta = pedir_respuesta()

            if respuesta == "SI":
                menu = pedir_opcion()
            else:
                break

        # ------------------- Mostrar Servicios ---------------------

        case 5:

            lista_servicios_ordenada = ordenar_servicios(lista_data)

            imprimir_lista(lista_servicios_ordenada)

            respuesta = pedir_respuesta()

            if respuesta == "SI":
                menu = pedir_opcion()
            else:
                break

        # ------------------- Guardar Servicios ---------------------

        case 6:

            escribir_archivo(lista_servicios_ordenada, "servicios_ordenados.json")

            respuesta = pedir_respuesta()

            if respuesta == "SI":
                menu = pedir_opcion()
            else:
                break

        case 7:
                
            print("Chau!")

            break
        
        case _:

            print("Error!!")

            menu = pedir_opcion()