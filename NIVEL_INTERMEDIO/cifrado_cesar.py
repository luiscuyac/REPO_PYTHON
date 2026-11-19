"""
Ciberseguridad - Cifrado César por Desplazamiento (Caesar Cipher)

Descripción:
    Implementa el algoritmo clásico de cifrado por sustitución monoalfabética.
    Solicita un texto y un factor de desplazamiento (1-25) para transformar cada
    letra mediante operaciones aritméticas sobre la tabla ASCII, preservando
    mayúsculas, minúsculas y caracteres no alfabéticos.

Metodología:
    Desarrollado de forma autónoma aplicando validación de entradas de usuario,
    métodos de inspección de cadenas (isalpha, isupper, islower) y conversión
    dinámica ASCII mediante las funciones nativas ord() y chr().

Aplicación en Redes y Ciberseguridad:
    - Fundamentos de criptografía y teoría de la información.
    - Entendimiento de algoritmos de sustitución y sanitización/ofuscación básica de payloads.
"""

text = input("Ingresa tu texto: ")
cipher = ""

while True:
    salt = input("Inserta un número de salto entre 1 y 25: ")
    if salt.isdigit():
        if 1 <= int(salt) <= 25:
            salt = int(salt)
            break
        else:
            print("Fuera de rango: 1 - 25")
    else:
        print("Opción no válida, inserta un número entre 1 y 25")

for char in text:
    result = ord(char) + salt
    if char.isalpha():
        if char.isupper():
            if result > ord("Z"):
                new_salt = salt - (ord("Z") - ord(char))
                new_char = ord("A") + new_salt - 1
                cipher += chr(new_char)
            else:
                cipher += chr(result)
        
        elif char.islower():
            if result > ord("z"):
                new_salt = salt - (ord("z") - ord(char))
                new_char = ord("a") + new_salt - 1
                cipher += chr(new_char)
            else:
                cipher += chr(result)
    else:
        cipher += char

print(f"Mi texto cifrado es: {cipher}")
