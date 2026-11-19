"""
Fundamentos - Detector Secuencial de Palíndromos

Descripción:
    Verifica si una cadena de texto introducida por el usuario es un palíndromo
    (se lee igual al derecho que al revés), ignorando mayúsculas, minúsculas 
    y espacios en blanco.

Metodología:
    Diseñado de forma secuencial (sin funciones), utilizando bucles for, 
    manipulación de índices simultáneos y validación de casos borde (espacios vacíos).
"""


text = input("Inserta un texto: ")

if text == "":
    print("El texto no puede estar vacío.")
else:    
    text_number = len(text)
    text_normal = ""
    text_rev = ""

    for i in range(text_number):
        pre_text = text[i].upper()
        if not pre_text.isspace():
            text_normal += pre_text

        pre_text_rev = text[text_number - 1 - i].upper()
        if not pre_text_rev.isspace():
            text_rev += pre_text_rev

    print(text_normal)
    print(text_rev)

    if text_normal and text_normal == text_rev:
        print("Es un Palíndromo.")
    else:
        print("No es un Palíndromo.")
