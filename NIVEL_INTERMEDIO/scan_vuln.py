"""Módulo de auditoría y gestión de vulnerabilidades en dispositivos de red.

Permite registrar, buscar y mitigar vulnerabilidades mediante un sistema
orientado a objetos administrado por consola.
"""


class Vuln:
    """Representa una vulnerabilidad detectada en un dispositivo de red.

    Atributos de clase:
        contador (int): Autoincremental para generar identificadores únicos.
    """
    contador = 0

    def __init__(self, dispositivo, ip, falla, nivel):
        """Inicializa una nueva instancia de vulnerabilidad.

        Args:
            dispositivo (str): Nombre o hostname del equipo afectado.
            ip (str): Dirección IP del dispositivo.
            falla (str): Descripción detallada de la vulnerabilidad.
            nivel (str): Criticidad del fallo (Bajo/Medio/Alto/Crítico).
        """
        Vuln.contador += 1
        self._id = f"V-{Vuln.contador:03d}"
        self._dispositivo = dispositivo
        self._ip = ip
        self._falla = falla
        self._nivel = nivel
        self._estado = "ACTIVA"

    @property
    def id(self):
        """str: Retorna el identificador único de la vulnerabilidad."""
        return self._id

    @property
    def dispositivo(self):
        """str: Retorna el nombre del dispositivo afectado."""
        return self._dispositivo

    @property
    def ip(self):
        """str: Retorna la dirección IP asociada."""
        return self._ip

    @property
    def falla(self):
        """str: Retorna la descripción de la falla."""
        return self._falla

    @property
    def nivel(self):
        """str: Retorna el nivel de criticidad."""
        return self._nivel

    @property
    def estado(self):
        """str: Retorna el estado actual de la vulnerabilidad (ACTIVA/MITIGADA)."""
        return self._estado

    def cambio_estado(self):
        """Cambia el estado de la vulnerabilidad de ACTIVA a MITIGADA.

        Returns:
            str: Mensaje descriptivo con el resultado del cambio de estado.
        """
        if self.estado == "ACTIVA":
            self._estado = "MITIGADA"
            return f"La vulnerabilidad {self.id} ha cambiado a {self.estado}"
        return f"La vulnerabilidad {self.id} ya está {self.estado}"

    def __str__(self):
        """Retorna una representación formateada en texto de la vulnerabilidad."""
        return f"ID: {self.id} | Dispositivo: {self.dispositivo} | IP: {self.ip} | Falla: {self.falla} | Nivel: {self.nivel} | Estado: {self.estado}"


class Scanner:
    """Gestiona la colección de vulnerabilidades detectadas y sus operaciones."""
    def __init__(self):
        """Inicializa el escáner con una lista vacía de vulnerabilidades."""
        self._listavuln = []

    @property
    def listavuln(self):
        """list: Retorna la lista completa de objetos Vuln registrados."""
        return self._listavuln

    def iniciar_scan(self, dispositivo, ip, falla, nivel):
        """Registra una nueva vulnerabilidad y la añade al sistema.

        Args:
            dispositivo (str): Nombre del equipo.
            ip (str): Dirección IP.
            falla (str): Descripción del problema.
            nivel (str): Nivel de riesgo.

        Returns:
            str: Mensaje de alerta del nuevo registro.
        """
        nuevo = Vuln(dispositivo, ip, falla, nivel)
        self._listavuln.append(nuevo)
        return f"¡ALERTA!: El dispositivo {nuevo.dispositivo} con ip {nuevo.ip} tiene una vulnerabilidad."

    def buscar_disp(self, buscar_ip):
        """Busca si un dispositivo con una IP específica está registrado.

        Args:
            buscar_ip (str): Dirección IP a rastrear.

        Returns:
            str: Estado de la búsqueda.
        """
        for dato in self.listavuln:
            if dato.ip == buscar_ip:
                return f"La ip {dato.ip} está actualmente siendo revisada."
        return f"La ip {buscar_ip} no se encuentra en la lista de vulnerabiliades."

    def mitigar_falla(self, ip_mitigar):
        """Busca una vulnerabilidad por IP y procede a mitigarla si existe.

        Args:
            ip_mitigar (str): Dirección IP del dispositivo a mitigar.

        Returns:
            str: Mensaje con el resultado de la mitigación.
        """
        for dato in self.listavuln:
            if dato.ip == ip_mitigar:
                cambiar = dato.cambio_estado()
                return cambiar
        return f"No se puede mitigar: La IP {ip_mitigar} no existe en el registro."


def menu():
    """Despliega el menú principal por consola y captura la opción del usuario.

    Returns:
        str: Opción seleccionada.
    """
    print("\n" + "=" * 30)
    print(" SISTEMA DE AUDITORÍA v1.0 ")
    print("=" * 30)
    print("1. Registrar Vulnerabilidad")
    print("2. Buscar por IP")
    print("3. Mostrar todas las alertas")
    print("4. Mitigar Vulnerabilidad")
    print("5. Salir")
    return input("\nSeleccione una opcion: ")


def main():
    """Función principal que controla el flujo de ejecución interactivo del script."""
    mi_scanner = Scanner()

    while True:
        opcion = menu()

        if opcion == "1":
            disp = input("Dispositivo: ")
            ip = input("IP: ")
            falla = input("Descripción del fallo: ")
            nivel = input("Nivel - (Bajo/Madio/Alto/Crítico) - :")
            print(mi_scanner.iniciar_scan(disp, ip, falla, nivel))
            print(f"Dispositivo {disp} agregado correctamente.")
        
        elif opcion == "2":
            buscar_ip = input("Ingrese la IP a rastrear: ")
            print(mi_scanner.buscar_disp(buscar_ip))

        elif opcion == "3":
            print("\n--- REPORTE GENERAL ---")
            for d in mi_scanner.listavuln:
                print(d)

        elif opcion == "4":        
            ip_mitigar = input("Ingresa la IP de la Vulnerabilidad a cerrar: ")
            mensaje = mi_scanner.mitigar_falla(ip_mitigar)
            print(mensaje)
        
        elif opcion == "5":
            print("Cerrando la sesión de auditoría... ¡Buen trabajo!")
            break

        else:
            print("Opción no válida, intente e nuevo.")


if __name__ == "__main__":
    main()
