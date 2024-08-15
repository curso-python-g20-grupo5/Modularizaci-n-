def mostrar_ingredientes_disponibles(ingredientes_disponibles):
    """
    Muestra una lista de todos los ingredientes disponibles para añadir a la pizza.

    La función imprime los ingredientes disponibles, numerados para facilitar la selección 
    en otras partes del programa.

    Args:
        ingredientes_disponibles (list): Lista de ingredientes disponibles para agregar a la pizza.

    Returns:
        None
    """
    print("\n--- Ingredientes Disponibles ---")
    for i, ingrediente in enumerate(ingredientes_disponibles, start=1):
        print(f"{i}. {ingrediente}")
