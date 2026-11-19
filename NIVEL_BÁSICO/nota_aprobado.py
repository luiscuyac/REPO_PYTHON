"""
Fundamentos - Clasificador de Notas con Tuplas y Manejo Defensivo

Descripción:
    Clasifica una nota numérica de un alumno asociándola a un color y un criterio 
    mediante tuplas. Implementa control defensivo de entradas decimales (soporte 
    para comas y puntos), gestión robusta de excepciones de valor (ValueError) 
    y captura de interrupciones de usuario (KeyboardInterrupt).

Metodología y Desarrollo:
    Estructura basada en bucles interactivos infinitos controlados, desempaquetado 
    de tuplas y cierre seguro de ejecución con bloques finally. Código adaptado 
    al estándar PEP 8.

Aplicación:
    - Sistemas interactivos por consola con validación de entradas de usuario.
    - Procesamiento de datos numéricos con tolerancia a errores de formato regional.
"""


COLORES = ("Rojo", "Amarillo", "Verde")

print(
    "\nRojo = Tienes que volver a examinarte."
    "\nAmarillo = Puedes volver a examinarte para mejorar tu nota."
    "\nVerde = Excelente, opcional volver a examinarte, pero no necesario.\n"
)


def nota_alumno(n):
    """
    Clasifica una calificación numérica y devuelve una tupla con su categoría y valor.

    Args:
        n (float): Calificación numérica del alumno.

    Returns:
        tuple: (color_asociado, valor_nota) o un mensaje de error si el rango no es válido.
    """
    if n >= 0 and n < 5:
        desaprobado = (COLORES[0], n)
        return desaprobado
    elif n >= 5 and n < 8:
        aprobado_medio = (COLORES[1], n)
        return aprobado_medio
    elif n >= 8 and n <= 10:
        aprobado_alto = (COLORES[2], n)
        return aprobado_alto
    else:
        error = ("No hay color", f"{n}: no es válido.")
        return error

        
try:
    while True:
        try:
            numero_parcial = input("Inserta tu nota (1-10): ")
            numero = float(numero_parcial.replace(",", "."))
            color, valor = nota_alumno(numero)
            
            if color == "No hay color":
                print(f"{numero} No es válido.")
                continue
            else:
                print(f"{color}: Tu nota es {valor}")
                break

        except ValueError:
            print("No has Insertado un número válido.")
except KeyboardInterrupt:
        print("\nPrograma cancelado por el usuario.")
finally:
        print("Gracias por usar el programa.")
