# Importar las funciones y variables necesarias
from variables import masas, salsas, ingredientes_disponibles
from mostrar_menu import mostrar_menu
from cambiar_masa import cambiar_masa
from cambiar_salsa import cambiar_salsa
from modificar_ingredientes import modificar_ingredientes
from mostrar_ingredientes_actuales import mostrar_ingredientes_actuales
from confirmar_pedido import confirmar_pedido
from mostrar_ingredientes_disponibles import mostrar_ingredientes_disponibles


def main():
    """
    Función principal que ejecuta el menú interactivo para la personalización de pizzas.
    
    El programa permite al usuario:
    1. Cambiar el tipo de masa.
    2. Cambiar el tipo de salsa.
    3. Modificar los ingredientes (agregar o eliminar).
    4. Mostrar los ingredientes actuales de la pizza.
    5. Confirmar el pedido y estimar el tiempo de preparación.

    El ciclo se repite hasta que el usuario decide confirmar el pedido o salir.

    Variables:
    masa_actual (str): Tipo de masa seleccionada por el usuario.
    salsa_actual (str): Tipo de salsa seleccionada por el usuario.
    ingredientes_actuales (list): Lista de ingredientes actualmente en la pizza.

    Error:
    ValueError: Si la opción ingresada por el usuario no es un número entero válido.
    """
    masa_actual = masas[0]
    salsa_actual = salsas[0]
    ingredientes_actuales = []

    while True:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                masa_actual = cambiar_masa(masas)
            elif opcion == 2:
                salsa_actual = cambiar_salsa(salsas)
            elif opcion == 3:
                mostrar_ingredientes_disponibles(ingredientes_disponibles)
            elif opcion == 4:
                modificar_ingredientes(ingredientes_actuales, ingredientes_disponibles)
            elif opcion == 5:
                mostrar_ingredientes_actuales(
                    masa_actual, salsa_actual, ingredientes_actuales
                )
            elif opcion == 6:
                confirmar_pedido(ingredientes_actuales)
            elif opcion == 7:
                print("Gracias por usar el sistema de pedidos de Pizza JAT. ¡Adiós!")
                break
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")


if __name__ == "__main__":
    main()
