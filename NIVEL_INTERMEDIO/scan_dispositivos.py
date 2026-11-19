"""
Módulo de Monitoreo de Red Automatizado.

Este script permite verificar el estado operativo de una lista de dispositivos
mediante comandos de ping multiplataforma (Windows/Linux), imprimiendo los resultados
en pantalla y registrando automáticamente los fallos en un archivo de texto.
"""

import os
import platform
from datetime import datetime

# Inventario de red: IP como clave, tupla (Hostname, Ubicación) como valor
dispositivos = {
    "10.0.2.100": ("Router_Core", "Centro de Datos"),
    "172.16.0.1": ("Switch_Acceso_1", "Oficina Planta 1"),
    "172.16.0.5": ("Servidor_Backup", "Sótano"),
    "127.0.0.1": ("Localhost", "Mi propio equipo"), # Útil para pruebas
    "8.8.8.8": ("DNS_Google", "Internet Exterior"),
    "192.168.179.1": ("Router_Home", "Planta 2")
}


def ejecutar_monitoreo(lista_equipos):
    """
    Ejecuta un chequeo de conectividad (ping) a un diccionario de dispositivos.

    Parámetros:
    - lista_equipos (dict): Diccionario donde la clave es la IP y el valor 
      es una tupla con (Nombre_del_Host, Ubicación).
    """
    print(f"--- Iniciando chequeo de {len(lista_equipos)} dispositivos ---")

    for ip, data in lista_equipos.items():
        if platform.system() == "Windows":
            comando = f"ping -n 2 {ip} > nul"
        else:
            comando = f"ping -c 2 {ip} > /dev/null"

        hora = datetime.now().strftime("[%Hh: %Mm: %Ss] - [%d-%m-%Y]")
        ping = os.system(comando)

        if ping == 0:
            print(f"La ip {data[0]} \"{ip}\" está operativa {hora}")
        else:
            with open(r"C:\Users\Usuario\Desktop\PRUEBAS\Registro_Fallos.txt", "a") as informe:
                informe.write(f"En {hora} el dispositivo {data[0]} situado en {data[1]} con ip \"{ip}\" esta caído\n")
            print(f"La ip {data[0]} \"{ip}\" está caída {hora}")


if __name__ == "__main__":
    ejecutar_monitoreo(dispositivos)
