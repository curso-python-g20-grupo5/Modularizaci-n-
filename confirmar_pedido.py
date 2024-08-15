def confirmar_pedido(ingredientes):
    """
    Calcula el tiempo estimado de preparación de la pizza y permite al usuario confirmar o cancelar el pedido.

    La función estima el tiempo de preparación basado en un tiempo base de 20 minutos, 
    más 2 minutos adicionales por cada ingrediente. Luego, solicita al usuario que confirme 
    o cancele el pedido. Si el usuario confirma, se muestra un mensaje de agradecimiento; 
    si no, se indica que el pedido ha sido cancelado.

    Args:
        ingredientes (list): Lista de ingredientes añadidos a la pizza.

    """
    tiempo_preparacion = 20 + 2 * len(ingredientes)
    print(f"El tiempo estimado de preparación es de {tiempo_preparacion} minutos.")
    confirmar = input("¿Desea confirmar su pedido? (s/n): ")
    if confirmar.lower() == 's':
        print("¡Pedido confirmado! Gracias por elegir Pizza JAT.")
    else:
        print("Pedido cancelado.")