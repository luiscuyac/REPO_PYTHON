"""
Fundamentos - Operaciones Básicas de Lectura y Escritura de Archivos

Descripción:
    Demuestra el ciclo completo de manipulación de archivos de texto en Python: 
    creación y escritura inicial (modo 'w'), adición de nuevo contenido 
    sin sobreescribir (modo 'a'), y lectura secuencial línea por línea 
    con un contador de líneas (modo 'r').

Metodología y Desarrollo:
    Lógica desarrollada por el autor. Se utilizó IA como herramienta de apoyo 
    para estructurar el docstring y aplicar el formato PEP 8.

Aplicación:
    - Almacenamiento persistente local y generación de registros (logs).
    - Procesamiento, lectura y análisis iterativo de archivos de texto plano.
"""


archivo = open("manejo_archivos_2.txt", "w")
archivo.write("Este es un archivo que no existía")
archivo.close()

archivo = open("manejo_archivos_2.txt", "a")
archivo.write("\nEsta es la línea que se agrega")
archivo.close()

archivo = open("manejo_archivos_2.txt", "r")

count = 0
for line in archivo:
    count += 1
    print(f"Línea {str(count) + " " + line}", end="")
print()
archivo.close()
