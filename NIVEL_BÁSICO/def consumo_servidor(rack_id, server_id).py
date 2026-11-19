"""
Fundamentos - Cálculo de Consumo por Rack y Servidor

Descripción:
    Calcula el consumo acumulado de ancho de banda (Mbps) en racks de red.
    Los racks impares contienen servidores de alto consumo (500 Mbps)
    y los pares contienen servidores estandár (100 Mbps).
"""


def es_rack_alto_consumo(rack_id: int):
    """Devuelve True si el rack es impar (alto consumo), False si es par, o None si está fuera de rango."""
    if not (1 <= rack_id <= 10):
        return None
    return rack_id % 2 != 0


def obtener_consumo_servidor(rack_id: int, server_id: int):
    """Retorna el consumo individual del servidor según el tipo de rack."""
    es_alto = es_rack_alto_consumo(rack_id)
    if es_alto is None or not (1 <= server_id <= 5):
        return None

    consumo_alto = 500
    consumo_estandar = 100

    return consumo_alto if es_alto else consumo_estandar


def calcular_consumo_total(rack_id: int, server_id: int):
    """Calcula el consumo acumulado hasta el número de servidor indicado."""
    consumo_unitario = obtener_consumo_servidor(rack_id, server_id)
    if consumo_unitario is None:
        return None

    return consumo_unitario * server_id


# --- Bloque Principal ---
try:
    rack_id = int(input("Inserta el número de rack (1-10): "))
    server_id = int(input("Inserta el número de servidor (1-5): "))

    total = calcular_consumo_total(rack_id, server_id)

    if total is None:
        print("❌ Error: Parámetros fuera de rango.")
    else:
        print(f"El consumo acumulado hasta el servidor {server_id} es de {total} Mbps.")

except ValueError:
    print("❌ Error: Debe ingresar números enteros válidos.")
