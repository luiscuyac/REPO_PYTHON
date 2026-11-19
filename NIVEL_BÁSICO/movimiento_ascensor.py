"""
Fundamentos - Simulación de Ascensor con Control Temporal

Descripción:
    Modela el comportamiento dinámico de un ascensor desplazándose entre plantas.
    Utiliza bucles de estado y pausas temporales (módulo time) para simular el 
    tiempo de tránsito entre pisos de forma secuencial.

Metodología y Desarrollo:
    Lógica basada en control de flujo dinámico con retroalimentación en consola.
    Se utilizó IA como herramienta de apoyo para estructurar el docstring 
    bajo el estándar PEP 8 y optimizar la jerarquía de retornos.

Aplicación:
    - Simulación de máquinas de estados finitos (FSM) básicas.
    - Manejo de retardo en la ejecución mediante time.sleep() para scripts interactivos.
"""

import time


def mover_ascensor(piso_actual, piso_deseado):
    """
    Simula el movimiento de un ascensor imprimiendo el progreso piso por piso.

    Args:
        piso_actual (int): Número del piso de origen.
        piso_deseado (int): Número del piso de destino.

    Returns:
        str: Mensaje indicando la llegada o la confirmación del piso.
    """
    if piso_actual == piso_deseado:
        return "Ya te encuentras en el piso deseado."
    
    while piso_actual != piso_deseado:
        if piso_actual < piso_deseado:
            print(f"Subiendo al piso {piso_deseado}, piso actual: {piso_actual}")
            piso_actual += 1
        elif piso_actual > piso_deseado:
            print(f"Bajando al piso {piso_deseado}, piso actual: {piso_actual}")
            piso_actual -= 1
        time.sleep(2)
    
    return f"Hemos llegado al piso {piso_deseado}"


if __name__ == "__main__":
    piso_actual = int(input("Pon el piso actual: "))
    piso_deseado = int(input("Pon el piso deseado: "))

    print(mover_ascensor(piso_actual, piso_deseado))
