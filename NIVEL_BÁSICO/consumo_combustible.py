"""
Fundamentos - Conversor de Consumo de Combustible (MPG <-> L/100km)

Descripción:
    Calcula la conversión entre el sistema imperial (Millas por Galón) 
    y el sistema métrico (Litros por cada 100 km) utilizando constantes físicas.

Metodología:
    Uso de funciones independientes con parámetros/argumentos definidos 
    y formateo de números flotantes.
"""

MILLA = 1609.344    # Metros por milla
GALON = 3.785411784 # Litros por galón


def litros_100km_a_millas_galon(litros):
    km_100 = 100 / (MILLA / 1000)
    consumo_galon = litros / GALON
    millas_galon = km_100 / consumo_galon
    return millas_galon


def millas_galon_a_litros_100km(millas):
    recorrido_km = millas * (MILLA / 1000)
    consumo_litros = (GALON / recorrido_km) * 100
    return consumo_litros
    

consumo_millas = float(input("Inserta el consumo en millas por galón (MPG): "))
litros = millas_galon_a_litros_100km(consumo_millas)

print(f"Se consumió {litros:.2f} litros cada 100 km.")
