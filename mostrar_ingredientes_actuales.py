def mostrar_ingredientes_actuales(masa, salsa, ingredientes):
    print("Pizza actual:")
    print(f"- Masa: {masa}")
    print(f"- Salsa: {salsa}")
    print("- Ingredientes:", ", ".join(ingredientes) if ingredientes else "Ninguno")
