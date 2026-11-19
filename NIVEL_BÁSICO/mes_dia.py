"""
Fundamentos - Validador de Fechas y Cálculo de Día del Año

Descripción:
    Implementa un sistema modular para verificar si un año es bisiesto 
    según el calendario gregoriano, calcula los días exactos de cualquier mes 
    y determina qué número de día del año representa una fecha específica.

Metodología y Desarrollo:
    Lógica algorítmica basada en el curso de Cisco Python Essentials. 
    Se utilizó IA como herramienta de apoyo para estructurar el docstring 
    y aplicar el formato PEP 8.

Aplicación:
    - Validación robusta de datos temporales y calendarios.
    - Resolución de problemas algorítmicos mediante descomposición modular de funciones.
"""


def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def days_in_month(year, month):    
    if month < 1 or month > 12:
        return None

    number_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month == 2 and is_year_leap(year):
        return 29

    return number_day[month-1]


def day_of_year(year, month, day):
    if month < 1 or month > 12:
        return None
    
    dias_test = days_in_month(year, month)
    if day < 1 or day > dias_test:
        return None

    contador = 0
    for m in range(1, month):
        contador += days_in_month(year, m)
    day += contador
    return day


if __name__ == "__main__":
    year = int(input("Inserta un año: "))
    month = int(input("Inserta un mes: "))
    day = int(input("Inserta un día: "))

    total_day = day_of_year(year, month, day)

    print("El día del año es", total_day)
