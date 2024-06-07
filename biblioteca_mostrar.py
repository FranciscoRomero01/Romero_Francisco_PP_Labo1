def imprimir_lista(servicios:list):
    """
    Imprime los servicios en forma de tabla con encabezados y formato predefinido.
    
    Args:
        servicios (list): Una lista de diccionarios que contiene la información de los servicios.
    """
    
    # Define los encabezados de la tabla
    encabezado = ["ID Servicio", "Descripción", "Tipo", "Precio Unitario", "Cantidad", "Total Servicio"]
    
    
    # Imprime los encabezados con un ancho fijo
    print("{:<15} {:<30} {:<10} {:<15} {:<10} {:<15}".format(*encabezado))
    print("-" * 95)

    
    # Imprime cada fila de servicios con el mismo formato
    for servicio in servicios:
        print("{:<15} {:<30} {:<10} {:<15} {:<10} {:<15}".format(
            servicio["id_servicio"], 
            servicio["descripcion"], 
            servicio["tipo"], 
            servicio["precioUnitario"], 
            servicio["cantidad"], 
            servicio["totalServicio"]
        ))
