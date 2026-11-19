"""
Fundamentos - Manejo Seguro de Archivos con Context Managers (with)

Descripción:
    Implementa la apertura, escritura, adición y lectura de archivos de texto 
    utilizando la sentencia 'with', asegurando el cierre automático y seguro 
    del recurso sin necesidad de invocar .close() manualmente.

Metodología y Desarrollo:
    Lógica desarrollada por el autor. Se utilizó IA como herramienta de apoyo 
    para estructurar el docstring y aplicar el formato PEP 8.

Aplicación:
    - Generación y lectura de logs o configuraciones de red de forma segura.
    - Prevención de fugas de memoria y bloqueos de archivos en sistemas operativos.
"""


with open("manejo_archivos_3.txt", "w") as file:
    file.write("Iniciamos con esta línea")

with open("manejo_archivos_3.txt", "a") as file:
    file.write("\nAgregamos esta línea")

with open("manejo_archivos_3.txt", "a") as file:
    file.write("\nAgregamos una más")

with open("manejo_archivos_3.txt", "r") as file:
    count = 0
    for line in file:
        count += 1
        print(f"{str(count)} -----> {line}", end="")
print()
