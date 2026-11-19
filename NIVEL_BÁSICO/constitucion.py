"""
Fundamentos - Mapeo de Estructuras Anidadas (Listas Bidimensionales)

Descripción:
    Recorre una matriz/lista bidimensional de tamaño variable para generar 
    coordenadas numéricas (tuplas) y procesar elementos anidados.

Metodología:
    Desarrollado para comparar dos técnicas de iteración en estructuras anidadas:
    1. Acceso por índices manuales usando range(len()) para construir tuplas (base 1).
    2. Iteración idiomática con enumerate() para extraer directamente los valores.

Aplicación en Redes:
    - Indexación de jerarquías de red (por ejemplo: Racks y Slots, Routers e Interfaces).
    - Mapeo de topologías jerárquicas (Número de Red -> Número de Host).
"""

constitucion = [["a", "b", "c", "d"], ["a", "b"], ["a", "b", "c", "d", "e", "f"], ["a", "b", "c"]]

ley = []

for articulo in range(len(constitucion)):
    for inciso in range(len(constitucion[articulo])):
        ley.append((articulo + 1, inciso + 1))

print(ley)

ley = []

for articulo, inciso in enumerate(constitucion, start=1):
    for _, l_inciso in enumerate(inciso):
        print(f"Artículo: {articulo}, Inciso: {l_inciso}")
