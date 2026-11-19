"""
Fundamentos - Implementación Personal de la Función Split

Descripción:
    Replica el comportamiento básico del método .split() de Python mediante 
    un algoritmo de análisis de caracteres y control de estados (máquina de estados), 
    separando las palabras de una cadena basándose en los espacios en blanco.

Metodología y Desarrollo:
    Lógica algorítmica desarrollada mediante bucles condicionales y banderas de control 
    (start_word) para gestionar la transición entre palabras y espacios. 
    Se estructuró bajo el estándar PEP 8.

Aplicación:
    - Procesamiento de cadenas y parsing de texto a nivel fundamental.
    - Comprensión profunda de cómo operan internamente las funciones nativas de Python.
"""


def my_personal_split(strgs):
    """
    Divide una cadena de texto en una lista de palabras usando los espacios como delimitadores.

    Args:
        strgs (str): Cadena de texto a procesar.

    Returns:
        list o str: Lista con las palabras encontradas, o un mensaje si está vacía.
    """
    if not strgs or strgs.isspace():
        return "La lista está vacía o solo contiene espacios."

    my_list = []
    word = ""
    start_word = not strgs[0].isspace()

    for w in strgs:
        if start_word:
            if not w.isspace():
                word += w
            else:
                my_list.append(word)
                start_word = False
        else:
            if not w.isspace():
                word = w
                start_word = True
            else:
                pass

    if start_word:
        my_list.append(word)
    
    return my_list


if __name__ == "__main__":
    phrase = input("Inserta una frase: ")
    print(my_personal_split(phrase))
