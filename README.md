# Modulación
En este repositorio se presenta el desarrollo para la actividad Modularización de la unidad Estructuras de datos y funciones.

### Objetivo
El objetivo de esta actividad consiste en dividir las distintas partes de nuestro proyecto en módulos. El por qué de ésta se encuentra en la idea de poner en práctica la idea de que los módulos de un proyecto deben estar separados en diversos scripts de Python, con el objetivo de que éstos se centren en resolver un problema en específico. Esto, normalmente, se encuentra encalpusalo en una función que será llamada desde un script maestro llamado ```main.py```.

## Descripción del proyecto
Pizza JAT, una empresa de pizzería a nivel mundial que desea automatizar su proceso de solicitud de Pizzas. Para ello, se le solicita generar un prototipo rápido que abarque elementos básicos para que el usuario pueda pedir su pizza.

Requerimientos
Debes crear un programa modularizado y que respete las buenas prácticas que incluya:
1. Un menú interactivo que permita al usuario personalizar su Pizza. Este debe:
a. Permitir cambiar el tipo de masa.
b. Permitir cambiar el tipo de salsa.
c. Permitir modificar ingredientes.
Este programa también debe mostrar los ingredientes que actualmente tiene la pizza. Además, debe ser capaz de mostrar una estimación temporal de lo que tomará preparar la pizza y, asimismo, ofrecer la posibilidad de confirmar si es que el cliente desea ordenar. En caso de confirmar, el tiempo para estar lista serán 20 minutos más 2 minutos por cada ingrediente, excluyendo masa y salsa. 
2. Una estimación de tiempo que tomará en que la pizza esté lista, y ofrezca la posibilidad de confirmar si es que desea ordenar. El tiempo para estar lista serán 20 minutos + 2 minutos por cada ingrediente, excluyendo masa y salsa.
3. Una opción que permita mostrar los ingredientes que actualmente tiene la pizza. 

## Archivos del Proyecto
Este repositorio está compuesto por 10 archivos, los cuales corresponden a los distintos módulos que componen el proyecto de modularización Pizza JAT:

  - ```__pycache__```
  - ```cambiar_masa.py```
  - ```cambiar_salsas.py```
  - ```confirmar_pedido.py```
  - ```main.py```
  - ```modificar_ingredientes.py```
  - ```mostrar_ingredientes_actuales.py```
  - ```mostrar_ingredientes_disponibles.py```
  - ```mostrar_menu.py```
  - ```variables.py```
En ello, cada módulo alojará cada función correspondiente

## Ejecución del proyecto
Una vez construido cada módulo, estos deben ser invocados desde el archivo principal (```main.py```). Para ello, se invocan como si fuesen librerias:

```
# Importar las funciones y variables necesarias
from variables import masas, salsas, ingredientes_disponibles
from mostrar_menu import mostrar_menu
from cambiar_masa import cambiar_masa
from cambiar_salsa import cambiar_salsa
from modificar_ingredientes import modificar_ingredientes
from mostrar_ingredientes_actuales import mostrar_ingredientes_actuales
from confirmar_pedido import confirmar_pedido
from mostrar_ingredientes_disponibles import mostrar_ingredientes_disponibles
```


## Autores y Autoras

- [Rosa Rubio](https://github.com/PaulinaRubioP)
- [Valery Maragaño](https://github.com/Valyxp)
- [Marco Alvarado](https://github.com/7pixel-cl)
- [Esteban Hernández](https://github.com/stivhc)
- [Claudia Aguayo](https://github.com/aguayo40)

⌨️ con ❤️ por el Grupo 5 - G20 😊
