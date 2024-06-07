import json
import copy


# -------------------------------- 1 ---------------------------------

def cargar_archivo(nombre_archivo:str) -> list:
    """
    Esta función carga los datos del archivo JSON especificado y los normaliza antes de devolverlos.
    
    Args:
        nombre_archivo (str): El nombre del archivo JSON a cargar.
    
    Returns:
        list: Una lista de diccionarios que contiene los datos normalizados del archivo cargado.
    """

    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as file:
            servicios = json.load(file)
            print(f"Archivo {nombre_archivo} cargado con éxito.")

            # Normaliza los datos si es necesario
            servicios_copia = normalizar_datos(servicios)

            return servicios_copia

    except FileNotFoundError:
        print(f"Error: El archivo {nombre_archivo} no se encontró.")
    
    except json.JSONDecodeError:
        print(f"Error: El archivo {nombre_archivo} no está en el formato JSON correcto.")



def normalizar_datos(lista_servicios:list) -> list:
    """
    Realiza la normalización de los datos en la lista de servicios.
    
    Args:
        lista_servicios (list): Una lista de diccionarios que contiene los datos de los servicios.
    
    Returns:
        list: Una copia de la lista de servicios con los datos normalizados.
    """
    # Realizar una copia profunda de la lista de servicios
    lista_servicios_copia = copy.deepcopy(lista_servicios)
    
    for servicio in lista_servicios_copia:
        # Normalizar id_servicio
        if servicio["id_servicio"]:
            servicio["id_servicio"] = int(servicio["id_servicio"])
        
        # Normalizar tipo
        if servicio["tipo"]:
            servicio["tipo"] = int(servicio["tipo"])
        
        # Normalizar precioUnitario
        if servicio["precioUnitario"]:
            servicio["precioUnitario"] = float(servicio["precioUnitario"])
    
        # Normalizar cantidad
        if servicio["cantidad"]:
            servicio["cantidad"] = int(servicio["cantidad"])

        # Normalizar totalServicio
        if servicio["totalServicio"]:
            servicio["totalServicio"] = int(servicio["totalServicio"])

    return lista_servicios_copia



# ---------------------------- 4 -------------------------------------------

def filtrar_por_tipo(servicios:list, tipo:int) -> list:
    """
    Filtra los servicios por el tipo especificado y devuelve una lista con los servicios que coinciden.
    
    Args:
        servicios (list): Una lista de diccionarios que contiene la información de los servicios.
        tipo (int): El tipo de servicio a filtrar.
    
    Returns:
        list: Una lista de diccionarios que contiene los servicios del tipo especificado.
    """

    lista_filtrada = list(filter(lambda servicio: servicio["tipo"] == tipo, servicios))

    return lista_filtrada



# ---------------------------- 4 y 6 -------------------------------------------

def escribir_archivo(servicios_filtrados:list, nombre_archivo_salida:str):
    """
    Escribe los servicios filtrados en un archivo JSON con formato adecuado.
    
    Args:
        servicios_filtrados (list): Una lista de diccionarios que contiene los servicios filtrados.
        nombre_archivo_salida (str): El nombre del archivo en el que se escribirán los servicios filtrados.
    """

    with open(nombre_archivo_salida, 'w', encoding='utf-8') as archivo_salida:
        json.dump(servicios_filtrados, archivo_salida, indent=4)
    
    print(f"Servicios filtrados escritos en el archivo {nombre_archivo_salida}.")




# --------------------------- 5 ----------------------------------------------
 
def ordenar_servicios(servicios:list) -> list:
    """
    Ordena los servicios por descripción de manera ascendente y devuelve la lista ordenada.
    
    Args:
        servicios (list): Una lista de diccionarios que contiene la información de los servicios.
    
    Returns:
        list: Una lista de diccionarios que contiene los servicios ordenados por descripción de manera ascendente.
    """

    servicios_ordenados = sorted(servicios, key=lambda x: x["descripcion"])
    
    return servicios_ordenados
