def mostrar_ingredientes_disponibles(ingredientes_disponibles):
    print("\n--- Ingredientes Disponibles ---")
    for i, ingrediente in enumerate(ingredientes_disponibles, start=1):
        print(f"{i}. {ingrediente}")
