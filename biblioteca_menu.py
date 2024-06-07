def pedir_opcion() -> int:
      """
      Muestra un menú de opciones y solicita al usuario que ingrese una opción.
      
      Returns:
            int: La opción seleccionada por el usuario.
      """
      
      print("\n1) Cargar archivo: Se pedirá el nombre del archivo y se cargarán en una lista los elementos "
            "del mismo."
            "\n2) Imprimir lista: Se imprimirá por pantalla la tabla (en forma de columnas) con los datos "
            "de los servicios."
            "\n3) Asignar totales: Se deberá hacer uso de una función lambda que asignará a cada servicio el "
            "total calculado (totalServicio) de la siguiente forma: cantidad x precioUnitario."
            "\n4) Filtrar por tipo: Se deberá generar un archivo igual al original, pero donde solo aparezcan "
            "servicios del tipo seleccionado."
            "\n5) Mostrar servicios: Se deberá mostrar por pantalla un listado de los servicios ordenados por "
            "descripción de manera ascendente."
            "\n6) Guardar servicios: Se deberá guardar el listado del punto anterior en un archivo de tipo json."
            "\n7) Salir")
      
      # Solicita al usuario que ingrese su opción y la convierte a entero
      opcion = int(input("Ingrese su opcion: "))

      # Retorna el entero ingresado
      return opcion



def pedir_respuesta() -> str:
      """
      Solicita al usuario una respuesta (SI/NO) y la convierte a mayúsculas.
      Mantiene solicitando la respuesta hasta que el usuario ingrese "SI" o "NO".
      
      Returns:
            str: La respuesta del usuario en mayúsculas ("SI" o "NO").
      """

      # Solicita al usuario que ingrese su respuesta y la vuelve en mayusculas
      respuesta = input("¿Quiere continuar? (SI/NO) ").upper()

      # Continúa solicitando una respuesta hasta que el usuario ingrese "SI" o "NO"
      while respuesta != "SI" and respuesta != "NO":
            respuesta = input("\nRespuesta incorrecta. ¿Quiere continuar? (SI/NO) ").upper()

      # Retorna la respuesta ingresada
      return respuesta
