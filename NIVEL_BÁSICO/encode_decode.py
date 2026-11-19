"""
Fundamentos - Codificación y Decodificación Hexadecimal con Type Hints

Descripción:
    Transforma una cadena de texto a su representación en formato 
    hexadecimal y permite revertir el proceso a su estado original. 
    Aplica anotaciones de tipo (Type Hints) para documentar el flujo de datos.

Metodología y Desarrollo:
    Estructura modular desarrollada por el autor. Se utilizó IA como 
    herramienta de consulta para adaptar la terminología técnica 
    (codificación vs. cifrado), integrar Type Hints y aplicar PEP 8.

Aplicación en Redes:
    - Inspección y lectura de payloads en tramas de red (Wireshark).
    - Conversión de datos en texto plano a formatos binarios/hexadecimales.
"""


def codificar_a_hex(texto: str) -> str:
    """Convierte una cadena de texto a su representación en hexadecimal."""
    datos_bytes = texto.encode("utf-8")
    return datos_bytes.hex()


def decodificar_desde_hex(texto_hex: str) -> str:
    """Convierte una cadena hexadecimal de vuelta a texto plano."""
    datos_bytes = bytes.fromhex(texto_hex)
    return datos_bytes.decode("utf-8")


# --- Bloque Principal ---
if __name__ == "__main__":
    entrada = input("Inserta el texto a codificar: ")

    # Proceso de codificación
    resultado_hex = codificar_a_hex(entrada)
    print(f"Representación Hexadecimal: {resultado_hex}")

    # Proceso de decodificación
    texto_original = decodificar_desde_hex(resultado_hex)
    print(f"Texto recuperado: {texto_original}")
