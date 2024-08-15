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
    Crea menú de acuerdo a opción entregada por usuario
    Con indice cero para variables masas, salsas e ingredientes
    ciclo while para determinar por condición la elección.
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
