"""Simulador de alarma por consola con control de flujo y pausas temporales.

Este script implementa un bucle temporizado que simula el funcionamiento
de una alarma segundo a segundo, utilizando el módulo time para dar efecto visual,
el operador módulo para omitir ciclos específicos y controlando la salida
con break y continue.
"""


import time


def simulador_alarma(tiempo_total):
    """Simula el conteo de una alarma y gestiona las pausas o saltos de ciclo.

    Args:
        tiempo_total (int): Duración total de la simulación en segundos.
    """
    segundo_actual = 0
    while segundo_actual < tiempo_total:
        segundo_actual += 1

        if segundo_actual == tiempo_total:
            print(f"Alarma desactivada en el segundo {segundo_actual}\nGracias por usar la alarma.")
            break
        if segundo_actual % 10 == 0:
            print(f"Omitiendo alarma en segundo {segundo_actual}")
            continue
        print(f"Alarma activada, segundo actual {segundo_actual}")
        time.sleep(0.5)


def main():
    """Ejecuta la interfaz de entrada por consola para el simulador de alarma."""
    tiempo_total = int(input("Inserta el tiempo total (segundos): "))
    simulador_alarma(tiempo_total)


if __name__ == "__main__":
    main()
