"""
Fundamentos - Validador Optimizado de Números Primos y Secuencia Dinámica

Descripción:
    Determina si un número introducido por el usuario es primo aplicando 
    filtros defensivos eficientes (descarte de no válidos y pares mayores a 2) 
    y optimización matemática mediante la raíz cuadrada (O(sqrt(n))). 
    Además, genera e imprime dinámicamente la secuencia de todos los primos 
    hasta el número ingresado.

Metodología y Desarrollo:
    Modularización mediante funciones de responsabilidad única, control de 
    flujo con rangos dinámicos y protección del único número primo par (el 2). 
    Estructurado bajo el estándar PEP 8 y bloques de ejecución principal.

Aplicación:
    - Teoría de números y algoritmos de optimización de rendimiento básico.
    - Estructuración de scripts limpios y profesionales para portafolio.
"""


def numero_no_uno(numero):
    """Verifica si el número es mayor que 1."""
    if numero <= 1:
        return False
    return True


def numero_no_par(numero):
    """Filtra y rechaza números pares estrictamente mayores que 2."""
    if numero > 2 and numero % 2 == 0:
        return False
    return True
    

def numero_divisible(numero):
    """
    Valida si un número es primo utilizando guardas defensivas y 
    reduciendo el límite de búsqueda hasta su raíz cuadrada.
    """
    if not numero_no_uno(numero) or not numero_no_par(numero):
        return False
    limite = int(numero ** 0.5) + 1
    for n in range(2, limite):
       if numero % n == 0:
        return False
    return True


if __name__ == "__main__":
    numero = int(input("Inserta un numero: "))

    numero_primo = numero_divisible(numero)

    if numero_primo:
        print(f"El número {numero} es primo.")
    else:
        print(f"El número {numero} no es primo.")

    for p in range(1, numero):
        if numero_divisible(p + 1):
            print(p + 1, end=" ")
    print()
