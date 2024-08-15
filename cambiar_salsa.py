def cambiar_salsa(salsas):
    """
    Permite al usuario seleccionar un tipo de salsa de una lista de opciones disponibles.

    La función muestra los tipos de salsa disponibles, solicita al usuario que seleccione una opción 
    ingresando un número correspondiente, y luego devuelve el tipo de salsa seleccionado. 
    Si el usuario ingresa una opción no válida o un valor no numérico, la función mantiene 
    la salsa actual (primera en la lista) y muestra un mensaje de error.

    Args:
        salsas (list): Lista de tipos de salsa disponibles.

    Returns:
        str: El tipo de salsa seleccionado por el usuario. 
             Si la entrada es inválida, devuelve la primera salsa en la lista.
    """
    print("Tipos de salsa disponibles:")
    for i, salsa in enumerate(salsas, start=1):
        print(f"{i}. {salsa}")
    try:
        eleccion = int(input("Seleccione el tipo de salsa: "))
        if 1 <= eleccion <= len(salsas):
            salsa_actual = salsas[eleccion - 1]
            print(f"Salsa seleccionada: {salsa_actual}")
        else:
            print("Opción no válida")
            salsa_actual = salsas[
                0
            ]  # Mantener la salsa actual si la opción es inválida
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")
        salsa_actual = salsas[
            0
        ]  # Mantener la salsa actual en caso de entrada no numérica
    return salsa_actual
