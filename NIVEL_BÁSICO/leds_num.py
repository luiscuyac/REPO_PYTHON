"""
Fundamentos - Simulador de Display LED por Matriz de Caracteres

Descripción:
    Toma una cadena numérica ingresada por el usuario y la dibuja en la 
    consola estilo matriz LED (tipo pixel art), imprimiendo los caracteres 
    renglón por renglón con un efecto visual de barrido.

Metodología y Desarrollo:
    Lógica algorítmica y diseño de patrones desarrollados por el autor. 
    Se utilizó IA como herramienta de apoyo para estructurar el docstring 
    y aplicar el formato PEP 8.

Aplicación:
    - Manipulación avanzada de diccionarios como tablas de búsqueda (Lookup Tables).
    - Uso de bucles anidados para procesamiento de datos en dos dimensiones.
    - Simulación visual en interfaces de texto plano.
"""


import time


def leds(patron):
    if patron == "":
        print("Sigue apagado.")
    else:
        for n in range(5):
            linea_completa = ""
            linea_vacia = ""

            for p in patron:
                if p.isdigit():
                    fila = patrones[p][n]
                    linea_completa += fila + " "
            time.sleep(0.5)
            if linea_completa != "":
                print(linea_completa)
            else:
                linea_vacia += linea_completa
        
        if linea_vacia == "" and linea_completa == "":
            print("Inserta mínimo un número.")


patrones = {
    "1": ["  #", "  #", "  #", "  #", "  #"],
    "2": ["###", "  #", "###", "#  ", "###"],
    "3": ["###", "  #", "###", "  #", "###"],
    "4": ["# #", "# #", "###", "  #", "  #"],
    "5": ["###", "#  ", "###", "  #", "###"],
    "6": ["#  ", "#  ", "###", "# #", "###"],
    "7": ["###", "  #", "  #", "  #", "  #"],
    "8": ["###", "# #", "###", "# #", "###"],
    "9": ["###", "# #", "###", "  #", "  #"],
    "0": ["###", "# #", "# #", "# #", "###"]
}


if __name__ == "__main__":
    encender = input("Inserta un número: ")
    leds(encender)
