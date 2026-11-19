"""
Seguridad - Gestor de Credenciales Hash y Encapsulamiento

Descripción:
    Implementa el hasheo de contraseñas mediante SHA-256 en objetos de red,
    utilizando encapsulamiento (@property/@setter), entrada oculta (getpass)
    y captura defensiva de errores mediante un decorador.

Metodología:
    Programación Orientada a Objetos (POO), decoradores con wrappers,
    hasheo criptográfico con hashlib y validación mediante excepciones.
"""

import hashlib
import getpass


def arreglar_formato(captura):
    """ Atrapamos la función para mejorar formato """

    def wrapper(self, clave):
        print("Iniciando proceso..........")
        
        try:
            clave_format = captura(self, clave)
            print(clave_format)
        except ValueError as e:
            print(f"❌ Error: {e}")

        print("Cerrando sistema...........")
    return wrapper


class GestorSeguridad:
    def __init__(self, nombre, clave="1234"):
        self._nombre = nombre
        self.clave = clave

    @property
    def nombre(self):
        return self._nombre

    @property
    def clave(self):
        return self._clave

    @clave.setter
    def clave(self, new_password):
        if not new_password:
            raise ValueError("La clave no puede estar vacía.")
        elif 4 <= len(new_password) <= 8:
            clave_hash = hashlib.sha256(new_password.encode())
            clave_hexa = clave_hash.hexdigest()
            self._clave = clave_hexa
        else:
            raise ValueError("La clave debe tener entre 4 y 8 caracteres.")

    @arreglar_formato
    def gestor_claves(self, clave):
        self.clave = clave
        return f"La nueva clave es: {self.clave}"


router_1 = GestorSeguridad("Router_Acceso")
new_password = getpass.getpass("Inserta la nueva clave: ")
router_1.gestor_claves(new_password)
