"""
Monitorización de Red - Escáner ICMP Resiliente con Control de Excepciones

Descripción:
    Carga un inventario de dispositivos desde un archivo externo y ejecuta pruebas 
    de conectividad ICMP (Ping) en tiempo real. Aplica programación defensiva para 
    capturar errores de lectura/escritura en el sistema de archivos sin interrumpir el servicio.

Metodología y Desarrollo:
    Lógica de red y diseño estructurado desarrollados por el autor. Se utilizó IA como 
    herramienta de consulta y revisión técnica para la optimización de patrones de 
    resiliencia (try-except específicos, cláusulas de guarda) y cumplimiento de PEP 8.

Aplicación en Redes:
    - Monitorización continua de infraestructura crítica (NOC).
    - Registro de incidencias tolerante a fallos de permisos o carpetas inexistentes.
"""

import os
import platform
from datetime import datetime


def cargar_inventario(archivo_inventario):
    nuevo_inventario = {}
    try:
        with open(archivo_inventario, "r", encoding="utf-8") as nuevo:
            for fila in nuevo:
                trozos = fila.strip().split(",")
                if len(trozos) == 3:
                    ip = trozos[0]
                    nombre = trozos[1]
                    ubicacion = trozos[2]
                    nuevo_inventario[ip] = (nombre, ubicacion)
        return nuevo_inventario
    
    except FileNotFoundError:
        print(f"ERROR: No se encontró el archivo de inventario en: {archivo_inventario}")
        return {}
    except Exception as e:
        print(f"ERROR INESPERADO al cargar inventario: {e}")
        return {}


def ejecutar_monitoreo(lista_equipos, registro_fallos):
    if not lista_equipos:
        print("No hay dispositivos para monitorear. Abortando chequeo.")
        return
    
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
            try:
                with open(registro_fallos, "a") as informe:
                    informe.write(f"En {hora} el dispositivo {nombre} situado en {lugar} con ip \"{ip}\" esta caído\n")
            except FileNotFoundError:
                print(f"ADVERTENCIA: No se pudo escribir en el log. La carpeta no existe.")
            except Exception as e:
                print(f"Cierra el archivo o agrega permisos de escritura para añadir al reporte: {e}")
            print(f"El dispositivo {nombre} con la ip \"{ip}\" está caído {hora}")

inventario_1 = r"C:\Users\Usuario\Desktop\PRUEBAS\inventario.txt"
ruta_log = r"C:\Users\Usuario\Desktop\PRUEBAS\Registro_Fallos.txt"

cliente_oslo = cargar_inventario(inventario_1)

ejecutar_monitoreo(cliente_oslo, ruta_log)
