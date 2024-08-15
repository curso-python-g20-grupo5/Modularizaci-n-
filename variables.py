"""
Variables de configuración y estado globales para la personalización de pizzas.

Estas variables almacenan las opciones disponibles para la masa, salsa, y 
los ingredientes, así como el estado actual de la pizza que el usuario está 
personalizando.

Variables:
    masas (list): Lista de tipos de masa disponibles en la pizzería.
    salsas (list): Lista de tipos de salsa disponibles en la pizzería.
    ingredientes_disponibles (list): Lista de todos los ingredientes que se pueden agregar a la pizza.
    masa_actual (str): Tipo de masa actualmente seleccionado para la pizza.
    salsa_actual (str): Tipo de salsa actualmente seleccionada para la pizza.
    ingredientes_actuales (list): Lista de ingredientes que actualmente están en la pizza.
"""
masas = ["Masa Tradicional", "Masa Delgada", "Masa con Bordes de Queso"]
salsas = ["Salsa de Tomate", "Salsa Alfredo", "Salsa Barbecue", "Salsa Pesto"]
ingredientes_disponibles = [
    "Tomate",
    "Champiñones",
    "Aceituna",
    "Cebolla",
    "Pollo",
    "Jamón",
    "Carne",
    "Tocino",
    "Queso",
]

# Estado actual de la pizza
masa_actual = masas[0]
salsa_actual = salsas[0]
ingredientes_actuales = []
