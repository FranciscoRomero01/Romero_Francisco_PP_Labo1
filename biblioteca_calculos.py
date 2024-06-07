def asignar_totales(servicios:list):
    """
    Asigna el total calculado (totalServicio) a cada servicio en función de la cantidad y el precio unitario.
    
    Args:
        servicios (list): Una lista de diccionarios que contiene la información de los servicios.
    """

    for servicio in servicios:

        # Utiliza una función lambda para calcular el total de cada servicio
        servicio["totalServicio"] = (lambda s: s["cantidad"] * s["precioUnitario"])(servicio)
    
    print("Totales asignados correctamente.")
