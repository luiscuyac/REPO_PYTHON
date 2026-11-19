"""
Ciberseguridad y POO - Sistema de Gestión de Dispositivos y Persistencia de Estado

Descripción:
    Modelado orientado a objetos para la administración segura de dispositivos (alarmas/nodos).
    Implementa hashing de contraseñas con SHA-256, captura oculta en consola, validación 
    de atributos mediante setters/getters y persistencia de configuración en JSON (NVRAM).

Metodología:
    Arquitectura, diseño modular y flujo lógico concebidos y desarrollados de forma autónoma,
    utilizando Inteligencia Artificial como herramienta de apoyo técnico para la implementación
    de patrones de POO, hashing criptográfico y gestión defensiva de excepciones.

Aplicación en Redes y Ciberseguridad:
    - Simulación de autenticación local AAA y gestión de credenciales en equipos de red.
    - Serialización y restauración de estados de configuración (estilo startup-config/running-config).
"""

import hashlib
import getpass
import os
import json


class Alarm:
    DISTRIBUIDOR = "Secur Pro"
    def __init__(self, marca, modelo, tipo, clave, soporte, estado="Apagada"):
        self._marca = marca
        self._modelo = modelo
        self._tipo = tipo
        self._clave = clave
        self._soporte = soporte
        self._estado = estado


    @property
    def marca(self):
        return self._marca


    @property
    def modelo(self):
        return self._modelo


    @property
    def tipo(self):
        return self._tipo


    @property
    def soporte(self):
        return self._soporte


    @soporte.setter
    def soporte(self, nuevo_numero):
        try:
            int_numero = int(nuevo_numero)
            if int_numero >= 0:
                if len(str(nuevo_numero)) == 9:
                    print(f"Nuevo número de soporte: {nuevo_numero}")
                    self._soporte = nuevo_numero
                else:
                    print("Cambio no realizado: El número tiene que ser de 9 dígitos")
            else:
                print("No puede ser un número negativo")
        except ValueError:
            print("Cambio no realizado: Tienes que insertar números enteros positivos")
        

    @property
    def estado(self):
        return self._estado

    
    def encender(self):
        if self.estado == "Encendida":
            print(f"La alarma {self.marca} ya está encendida.")
        else:
            contador = 0
            while contador < 3:
                contador += 1
                palabra_plana = getpass.getpass(f"Ingresa la clave secreta para la alarma {self.marca} (máximo 3 intentos): ")
                palabra = hashlib.sha256(palabra_plana.encode()).hexdigest()
                if palabra == self.clave:
                    self._estado = "Encendida"
                    print(f"La alarma {self.marca} está ahora {self.estado}")
                    print("Nota: Es importante cambiar la clave cada 3 meses.")
                    break
                else:
                    print("Clave equivocada")
                    if contador == 3:
                        print(f"Has superado el límite de intentos para la alarma {self.marca}")
                        print(f"Contacta con soporte técnico: {self.soporte}")


    def apagar(self):
        if self.estado == "Apagada":
            print(f"La alarma {self.marca} ya está apagada.")
        else:
            contador = 0
            while contador < 3:
                contador += 1
                palabra_plana = getpass.getpass(f"Ingresa la clave secreta para la alarma {self.marca} (máximo 3 intentos): ")
                palabra = hashlib.sha256(palabra_plana.encode()).hexdigest()
                if palabra == self.clave:
                    self._estado = "Apagada"
                    print(f"La alarma {self.marca} está ahora {self.estado}")
                    print("Nota: Es importante cambiar la clave cada 3 meses.")
                    break
                else:
                    print("Clave equivocada")
                    if contador == 3:
                        print(f"Has superado el límite de intentos para la alarma {self.marca}")
                        print(f"Contacta con soporte técnico: {self.soporte}")


    @property
    def clave(self):
        return self._clave


    def cambiar_clave(self):
        print(f"\n --- Gestor de contraseñas: {self.marca} ---")
        seguridad_plana = getpass.getpass("Ingresa la contraseña actual: ")
        seguridad = hashlib.sha256(seguridad_plana.encode()).hexdigest()
        
        if seguridad == self.clave:
            nueva_clave_plana = getpass.getpass("Inserta la nueva clave: ")
            if not nueva_clave_plana:
                print("La clave no puede estar vacía")
            elif 4 <= len(nueva_clave_plana) <= 8:
                nueva_clave = hashlib.sha256(nueva_clave_plana.encode()).hexdigest()
                if nueva_clave != self.clave:
                    confirma_nueva_clave_plana = getpass.getpass("Confirma la nueva nueva clave: ")
                    confirma_nueva_clave = hashlib.sha256(confirma_nueva_clave_plana.encode()).hexdigest()
                    if nueva_clave == confirma_nueva_clave:
                        self._clave = nueva_clave
                        print(f"✅ Cambio de clave confirmada.")
                    else:
                        print(f"❌ Las claves no coinciden, cambio no realizado.")
                else:
                    print("La clave no puede ser igual a la anterior")
            else:
                print("La contraseña tiene que ser entre 4 y 8 dígitos")
        else:
            print("La contraseña actual no es correcta: Acceso denegado")


    def a_diccionario(self):
        return {
            "marca": self.marca,
            "modelo": self.modelo,
            "tipo": self.tipo,
            "clave": self.clave,
            "soporte": self.soporte,
            "estado": self.estado
        }


ARCHIVO_CONFIG = "alarmas.json"

try:
    if os.path.exists(ARCHIVO_CONFIG):
        print(f"\n--- [NVRAM] Cargando configuración desde {ARCHIVO_CONFIG} ---")
        with open(ARCHIVO_CONFIG, "r") as file:
            base_datos = json.load(file)
            
            alarma_1 = Alarm(**base_datos[0])
            alarma_2 = Alarm(**base_datos[1])

    else:
        print("\n--- [SETUP] Archivo no encontrado. Cargando valores por defecto ---")

        clave_1 = hashlib.sha256("Secret01".encode()).hexdigest()
        clave_2 = hashlib.sha256("Out2026".encode()).hexdigest()

        alarma_1 = Alarm("Securitas Direct", "X1500", "5G", clave_1, "900102030")
        alarma_2 = Alarm("Prosegur", "2300G", "FTTH", clave_2, "900900200")

    while True:
        print(f"{'=' * 32}\n        Panel de control\n{'=' * 32}")
        print("1. Encender Alarmas")
        print("2. Apagar Alarmas")
        print("3. Cambiar Claves")
        print("4. Cambiar Número de Soporte")
        print("5. Salir")
        print("=" * 32)
        
        opcion = input("\nSelecciona una opción: ")
        if opcion == "1":
            alarma_1.encender()
            alarma_2.encender()
        elif opcion == "2":
            alarma_1.apagar()
            alarma_2.apagar()
        elif opcion == "3":
            alarma_1.cambiar_clave()
            alarma_2.cambiar_clave()
        elif opcion == "4":
            alarma_1.soporte = input(f"Inserta el nuevo número de soporte de {alarma_1.marca}: ")
            alarma_2.soporte = input(f"Inserta el nuevo número de soporte de {alarma_2.marca}: ")
        elif opcion == "5":
            print("\n--- [NVRAM] Guardando cambios antes de salir... ---")
            guardar_datos = [
                alarma_1.a_diccionario(),
                alarma_2.a_diccionario()
            ]

            with open(ARCHIVO_CONFIG, "w") as file:
                json.dump(guardar_datos, file, indent=4)
            
            print("✅ Configuración guardada. Cerrando sistema...")
            break
        else:
            print("Opción no válida")

    print(
        f"\nInforme final {alarma_1.marca}:"
        f"\nEstado: {alarma_1.estado}"
        f"\nModelo: {alarma_1.modelo}"
        f"\nTipo: {alarma_1.tipo}"
        f"\nSoporte: {alarma_1.soporte}"
        f"\nClave: {alarma_1.clave}"
        f"\nDistribuidor --> {Alarm.DISTRIBUIDOR}"
    )

    print(
        f"\nInforme final {alarma_2.marca}:"
        f"\nEstado: {alarma_2.estado}"
        f"\nModelo: {alarma_2.modelo}"
        f"\nTipo: {alarma_2.tipo}"
        f"\nSoporte: {alarma_2.soporte}"
        f"\nClave: {alarma_2.clave}"
        f"\nDistribuidor --> {Alarm.DISTRIBUIDOR}"
    )

except ValueError:
    print("\n❌ Has insertado un valor no válido")

except AttributeError:
    print("\n❌ Error de código: Estamos trabajando en la solución.")

except FileNotFoundError:
    print("\n❌ Fallo en el sistema de archivos: Estamos trabajando en la solución")

except Exception as e:
    print(f"\n❌ Error tipo: {type(e).__name__}")
    print(f"❌ Estamos trabajando en la solución del error: '{e}'")

except KeyboardInterrupt:
    print("\n\nPrograma cancelado por el usuario.")

finally:
    print("\n🌎 Gracias por usar el Software de Gestión de Alarmas. 🌏")
