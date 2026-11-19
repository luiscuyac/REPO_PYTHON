"""
Monitorización de Red - Escáner de Dispositivos y Registro de Incidencias (Logging)

Descripción:
    Carga un inventario de red desde un archivo CSV/TXT local, ejecuta pruebas 
    de conectividad ICMP (Ping) multiplataforma en tiempo real y registra 
    las caídas de servicio en un archivo de log persistente con marcas de tiempo.

Metodología y Desarrollo:
    Lógica de red y estructura modular diseñadas por el autor. Se contó con el 
    apoyo de IA como herramienta de consulta para validar el manejo seguro de 
    archivos (with open), desempaquetado de tuplas y adherencia a PEP 8.

Aplicación en Redes:
    - Monitorización básica de disponibilidad (Up/Down) para routers, switches y servidores.
    - Generación automática de reportes de fallos para auditorías o alertas del equipo NOC.
"""

import os
import platform
from datetime import datetime


def cargar_inventario(archivo_inventario):
    nuevo_inventario = {}
    with open(archivo_inventario, "r", encoding="utf-8") as nuevo:
        for fila in nuevo:
            trozos = fila.strip().split(",")
            if len(trozos) == 3:
                ip = trozos[0]
                nombre = trozos[1]
                ubicacion = trozos[2]
                nuevo_inventario[ip] = (nombre, ubicacion)
    return nuevo_inventario


def ejecutar_monitoreo(lista_equipos, registro_fallos):
    print(f"--- Iniciando chequeo de {len(lista_equipos)} dispositivos ---")
    for ip, (nombre, lugar) in lista_equipos.items():
        if platform.system() == "Windows":
            comando = f"ping -n 2 {ip} > nul"
        else:
            comando = f"ping -c 2 {ip} > /dev/null"

        hora = datetime.now().strftime("[%Hh: %Mm: %Ss] - [%d-%m-%Y]")
        ping = os.system(comando)
        if ping == 0:
            print(f"El dispositivo {nombre} con la ip \"{ip}\" está operativo {hora}")
        else:
            with open(registro_fallos, "a") as informe:
                informe.write(f"En {hora} el dispositivo {nombre} situado en {lugar} con ip \"{ip}\" esta caído\n")
            print(f"El dispositivo {nombre} con la ip \"{ip}\" está caído {hora}")

inventario_1 = r"C:\Users\Usuario\Desktop\PRUEBAS\inventario.txt"
ruta_log = r"C:\Users\Usuario\Desktop\PRUEBAS\Registro_Fallos.txt"

cliente_oslo = cargar_inventario(inventario_1)

ejecutar_monitoreo(cliente_oslo, ruta_log)
