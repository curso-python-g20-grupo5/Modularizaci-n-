def cambiar_masa(masas):
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
