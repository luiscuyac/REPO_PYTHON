"""
Manipulación de Texto - Detector de Anagramas

Descripción:
    Solicita dos textos, limpia los espacios en blanco e ignora las mayúsculas 
    para determinar si ambas cadenas son anagramas (contienen exactamente las mismas letras).

Metodología:
    Desarrollado de forma autónoma utilizando Inteligencia Artificial como guía 
    para optimizar la lógica de comparación mediante ordenamiento.

Aplicación en Redes:
    - Lógica básica para la verificación de integridad de datos.
    - Normalización de cadenas (sanitización de inputs) antes de procesar comandos o configuraciones.
"""

text_1 = input("Inserta el primer texto: ").upper()
text_2 = input("Inserta el segundo texto: ").upper()

text_1 = text_1.replace(" ", "")
text_2 = text_2.replace(" ", "")
if text_1 and text_2 and sorted(text_1) == sorted(text_2):
    print("ANAGRAMAS")
else:
    print("No son ANAGRAMAS")
