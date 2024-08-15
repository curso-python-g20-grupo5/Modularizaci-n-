def mostrar_ingredientes_actuales(masa, salsa, ingredientes):
    """
    Muestra la configuración actual de la pizza, incluyendo el tipo de masa, salsa y los ingredientes seleccionados.

    La función imprime la masa, salsa y una lista de ingredientes que actualmente tiene la pizza. 
    Si no se han agregado ingredientes, indica "Ninguno".

    Args:
        masa (str): El tipo de masa seleccionado.
        salsa (str): El tipo de salsa seleccionado.
        ingredientes (list): Lista de ingredientes actualmente en la pizza.

    """
    print("Pizza actual:")
    print(f"- Masa: {masa}")
    print(f"- Salsa: {salsa}")
    print("- Ingredientes:", ", ".join(ingredientes) if ingredientes else "Ninguno")
