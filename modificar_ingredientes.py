def modificar_ingredientes(ingredientes_actuales, ingredientes_disponibles):
    """
    Permite al usuario agregar o eliminar ingredientes de la pizza actual.

    La función muestra los ingredientes que ya están en la pizza y ofrece dos opciones:
    1. Agregar un nuevo ingrediente de la lista de ingredientes disponibles.
    2. Eliminar un ingrediente que ya esté en la pizza.

    Si el usuario selecciona agregar, se le mostrará la lista de ingredientes disponibles
    y podrá elegir uno para añadir a la pizza, siempre que no esté ya en la lista. 
    Si selecciona eliminar, deberá ingresar el nombre del ingrediente que desea quitar.

    Args:
        ingredientes_actuales (list): Lista de ingredientes que ya están en la pizza.
        ingredientes_disponibles (list): Lista de todos los ingredientes disponibles para agregar.

    """
    print("Ingredientes actuales:", ingredientes_actuales)
    print("1. Agregar ingrediente")
    print("2. Eliminar ingrediente")
    try:
        eleccion = int(input("Seleccione una opción: "))
        if eleccion == 1:
            print("Ingredientes disponibles para agregar:")
            for i, ing in enumerate(ingredientes_disponibles, start=1):
                print(f"{i}. {ing}")
            ingr = int(input("Seleccione un ingrediente para agregar: "))
            if 1 <= ingr <= len(ingredientes_disponibles):
                ingrediente = ingredientes_disponibles[ingr - 1]
                if ingrediente not in ingredientes_actuales:
                    ingredientes_actuales.append(ingrediente)
                    print(f"Ingrediente {ingrediente} agregado.")
                else:
                    print("El ingrediente ya está en la lista.")
            else:
                print("Opción no válida")
        elif eleccion == 2:
            ingr = input("Ingrese el nombre del ingrediente a eliminar: ")
            if ingr in ingredientes_actuales:
                ingredientes_actuales.remove(ingr)
                print(f"Ingrediente {ingr} eliminado.")
            else:
                print("Ingrediente no encontrado.")
        else:
            print("Opción no válida")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")
