def confirmar_pedido(ingredientes):
    tiempo_preparacion = 20 + 2 * len(ingredientes)
    print(f"El tiempo estimado de preparación es de {tiempo_preparacion} minutos.")
    confirmar = input("¿Desea confirmar su pedido? (s/n): ")
    if confirmar.lower() == 's':
        print("¡Pedido confirmado! Gracias por elegir Pizza JAT.")
    else:
        print("Pedido cancelado.")