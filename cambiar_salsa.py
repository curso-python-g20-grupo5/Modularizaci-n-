def cambiar_salsa(salsas):
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
