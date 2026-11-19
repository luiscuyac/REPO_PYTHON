"""
Módulo de análisis de frecuencias de texto.
Demostración de lectura y escritura de archivos utilizando open() y close()
de forma explícita, como paso previo metodológico al uso de gestores de contexto (with open).
"""

from os import strerror


def analizar_frecuencia_letras(nombre_archivo_entrada: str, nombre_archivo_salida: str) -> None:
    """Lee un archivo de texto, cuenta letras (ignorando mayúsculas) y guarda el histograma ordenado.

    Nota técnica: Se utiliza open() y close() de forma explícita e intencionada 
    como ejercicio y paso previo a la implementación con gestores de contexto (with).
    """
    try:
        data = open(nombre_archivo_entrada, "r", encoding="utf-8")
        
        my_keys = {}
        for line in data:
            for letter in line:
                if letter.isalpha():
                    letter_lower = letter.lower()
                    my_keys[letter_lower] = my_keys.get(letter_lower, 0) + 1

        data.close()

        if not my_keys:
            print("⚠️ El archivo está vacío o no contiene letras alfabéticas.")
            return

        new_data = open(nombre_archivo_salida, "w", encoding="utf-8")
        
        for key, value in sorted(my_keys.items(), key=lambda par: par[1], reverse=True):
            new_data.write(f"{key} --> {value}\n")

        new_data.close()
        print(f"✅ Archivo de histograma '{nombre_archivo_salida}' generado correctamente.")

    except IOError as e:
        print(f"❌ ERROR de E/S: {strerror(e.errno)}")


if __name__ == "__main__":
    archivo_entrada = "text.txt"
    archivo_salida = "text.txt.hist"

    analizar_frecuencia_letras(archivo_entrada, archivo_salida)
