"""
Fundamentos - Cálculo del Dígito de Vida (Numerología)

Descripción:
    Suma de forma iterativa las cifras de una fecha de nacimiento (DDMMAAAA) 
    mediante un bucle while hasta reducir el resultado a un solo dígito (1-9).

Metodología y Desarrollo:
    Lógica algorítmica diseñada por el autor. Se contó con el apoyo de IA como 
    herramienta de consulta para la estructuración de docstrings y formato PEP 8.

Aplicación:
    - Uso de bucles condicionales (while) para reducciones iterativas.
    - Conversión y manipulación de tipos de datos (str e int) dentro de iteraciones.
"""

number_date = input("Ingresa tu fecha de nacimiento (DDMMAAAA): ")
limit = True

while limit:
    magic_digit = 0
    for number in number_date:
        magic_digit += int(number)
    number_date = str(magic_digit)
    if magic_digit < 10:
        limit = False

print(f"\nMi dígito de vida es {magic_digit}")
