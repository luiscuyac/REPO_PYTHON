"""
Fundamentos - Mapeador Dinámico de Cursos y Aulas

Descripción:
    Genera las combinaciones posibles de años escolares y letras de aula,
    gestionando manualmente la inserción de la 'ñ' en el abecedario.

Metodología:
    Uso de la función chr() para conversión ASCII, manipulación de listas
    (insert y pop), condicionales de validación y bucles anidados con tuplas.
"""

def grados(curso):
    numero_curso = []
    if curso > 0 and curso < 6:
        for g in range(1, curso + 1):
            numero_curso.append(g)
        return numero_curso
    return False


def aula(salon):
    if salon > 0 and salon < 28:
        letra_salon = []
        for l in range(salon):
            letra_salon.append(chr(97 + l))
        if len(letra_salon) >= 14:
            letra_salon.insert(14, "ñ")
            letra_salon.pop()
        return letra_salon
    return False


curso = int(input("¿Hasta que año se enseña en este colegio? (1-5): "))
total_cursos = grados(curso)
letras = int(input("¿Cuántas aulas hay por cada curso? (1-27): "))
total_aulas = aula(letras)


if total_cursos and total_aulas:
    total_cursos_aulas = []
    for g in total_cursos:
        for a in total_aulas:
            total_cursos_aulas.append((g, a))

    total = []
    for elemento in total_cursos_aulas:
        subtotal = (str(elemento[0]) + elemento[1])
        total.append(subtotal)

    print("Este centro tiene el siguiente listado de aulas: ", end="")
    print(*total, sep=", ")

else:
    print("Fuera de Rango")
    