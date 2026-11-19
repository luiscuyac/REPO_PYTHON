"""
Fundamentos - Juego de Adivinanza con Límite de Intentos y Control Defensivo

Descripción:
    Implementa un juego interactivo de adivinanza de números con un número 
    máximo de intentos permitidos. Cuenta con validación estricta de entradas 
    numéricas, gestión de excepciones por teclado y control de flujo seguro.

Metodología y Desarrollo:
    Lógica basada en bucles condicionales con control de intentos decrecientes, 
    captura de errores de tipo (ValueError) y cierre controlado mediante bloques 
    try-except-finally. Adaptado al estándar PEP 8.

Aplicación:
    - Creación de pequeños minijuegos de consola interactivos.
    - Control de límites de reintentos en credenciales o entradas de usuario.
"""

NUMERO_MAGICO = 100
MAX_INTENTOS = 5


def jugar_adivinanza():
    """
    Ejecuta la lógica del juego de adivinar el número con un límite de intentos.
    """
    intentos_restantes = MAX_INTENTOS

    while intentos_restantes > 0:
        try:
            print(f"\nTienes {intentos_restantes} intentos restantes.")
            entrada = input("Inserta el número mágico (o 100 para salir): ")
            numero = int(entrada)

            if numero == NUMERO_MAGICO:
                print("¡Has insertado la clave / acertado el número mágico!")
                break
            elif numero < NUMERO_MAGICO:
                print("Es muy pequeño.")
            else:
                print("Es muy grande.")

            intentos_restantes -= 1

        except ValueError:
            print("Error: No has insertado un número válido. Inténtalo de nuevo.")

    if intentos_restantes == 0:
        print(f"\nHas superado los {MAX_INTENTOS} intentos permitidos.")


if __name__ == "__main__":
    try:
        jugar_adivinanza()
    except KeyboardInterrupt:
        print("\n\nPrograma cancelado por el usuario.")
    finally:
        print("Gracias por participar.")
