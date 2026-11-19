"""
Decoradores y Closures para Conexión SSH.

Descripción:
    Implementa un decorador de funciones que añade una capa de lógica 
    previa (simulación de reintentos interactivos y retardos de red) 
    a una función de conexión SSH básica.

Conceptos aplicados:
    - Funciones de orden superior (Higher-Order Functions).
    - Closures (funciones anidadas que recuerdan el ámbito exterior).
    - Uso del módulo time para pausas simuladas.
"""

import time


def intentos_ssh(recoger_funcion):
    """Decorador que añade una simulación de intentos interactivos antes de ejecutar la función original."""

    def wrapper(ip):
        """Función envoltorio (wrapper) que procesa los reintentos y llama a la función original."""
        intentos = int(input("Ingresa el número de intentos: "))
        for i in range(intentos):
            time.sleep(2)
            print(f"Intento {i + 1}: Conectando {ip}...")
        
        funcion_original = recoger_funcion(ip)
        print(funcion_original)
        return funcion_original    
    return wrapper


def conectar_ssh(ip):
    """Función original que simula el establecimiento de una conexión SSH a una IP."""
    time.sleep(2)
    return f"Conexión correcta: ip {ip} conectada."


if __name__ == "__main__":
    dato = "192.168.1.1"

    ssh_formateada = intentos_ssh(conectar_ssh)

    ssh_formateada(dato)
