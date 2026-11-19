"""
Fundamentos - Verificación de Subcadena Ordenada (Algoritmo de Búsqueda)

Descripción:
    Comprueba si los caracteres del primer texto se encuentran dentro del 
    segundo texto respetando su orden relativo de aparición mediante el 
    uso del método str.find() y control manual de índices.

Metodología y Desarrollo:
    Lógica algorítmica desarrollada por el autor. Se utilizó IA como 
    herramienta de consulta para estructurar el docstring y aplicar PEP 8.

Aplicación:
    - Búsqueda y filtrado manual de patrones en cadenas de texto.
    - Manejo de índices y desplazamiento en iteraciones.
"""

text_1 = input("Inserta el TEXTO 1: ").upper()
text_2 = input("Inserta el TEXTO 2: ").upper()
text_comp = ""


if len(text_1) <= len(text_2):
    index_letter = 0
    for letter in text_1:
        my_index_look = text_2.find(letter, index_letter)
        if my_index_look == -1:
            text_comp = ""
            break
        else:
            text_comp += letter
            index_letter = my_index_look + 1
else:
    print("El 'Texto 1' tiene que ser igual o menor a 'Texto 2'")


if text_1 and text_2 and text_1 == text_comp:
    print(f"El texto {text_1} está incluido en {text_2}")
else:
    print(f"El texto {text_1} no está incluido en {text_2}")
  