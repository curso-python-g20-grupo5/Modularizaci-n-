def cambiar_masa(masas):
    """
    Permite al usuario seleccionar un tipo de masa de una lista de opciones disponibles.

    La función muestra los tipos de masa disponibles, solicita al usuario que seleccione una opción 
    ingresando un número correspondiente, y luego devuelve el tipo de masa seleccionado. 
    Si el usuario ingresa una opción no válida o un valor no numérico, la función mantiene 
    la masa actual (primera en la lista) y muestra un mensaje de error.

    Args:
        masas (list): Lista de tipos de masa disponibles.

    Returns:
        str: El tipo de masa seleccionado por el usuario. 
             Si la entrada es inválida, devuelve la primera masa en la lista.
    """
    print("Tipos de masa disponibles:")
    for i, masa in enumerate(masas, start=1):
        print(f"{i}. {masa}")
    try:
        eleccion = int(input("Seleccione el tipo de masa: "))
        if 1 <= eleccion <= len(masas):
            masa_actual = masas[eleccion - 1]
            print(f"Masa seleccionada: {masa_actual}")
        else:
            print("Opción no válida")
            masa_actual = masas[0]  # Mantener la masa actual si la opción es inválida
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")
        masa_actual = masas[0]  # Mantener la masa actual en caso de entrada no numérica
    return masa_actual
