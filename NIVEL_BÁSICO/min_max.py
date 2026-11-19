"""
Fundamentos - Validación Entrada de Datos y Manejo de Excepciones

Descripción:
    Solicita y valida una entrada numérica por consola asegurando que el dato 
    sea un entero válido dentro de un rango especificado (mínimo y máximo). 
    Captura excepciones de tipo ValueError mediante bloques try/except.

Metodología y Desarrollo:
    Lógica basada en ejercicios de control de flujo. Se utilizó IA como 
    herramienta de apoyo para optimizar nombres de variables reservadas, 
    eliminar redundancias y estructurar el docstring PEP 8.

Aplicación:
    - Entrada segura de datos en scripts de automatización e interfaces por CLI.
    - Prevención de caídas de programa (crashes) por datos erróneos de usuario.
"""


def validar_numero_en_rango(pregunta, min, max):
    while True:
        try:
            numero = int(input(pregunta))
            if min <= numero <= max:
                return f"El número es: {numero}"
            else:
                print( f"El valor no está dentro del rango permitido {min} y {max})")
        except ValueError:
            print(f"Error: entrada incorrecta.")


if __name__ == "__main__":
    resultado = validar_numero_en_rango("Inserta un número entre -10 y 10: ", -10, 10)
    print(resultado)
