"""
Sistema de Gestión de Inventario de Red (POO).

Descripción:
    Implementa un sistema orientado a objetos para registrar, almacenar, 
    buscar y mostrar nodos/dispositivos dentro de una red informática, 
    utilizando identificadores únicos autoincrementales y encapsulamiento.

Arquitectura y Clases:
    - Nodo: Modela un dispositivo individual con su IP y un ID único formateado.
    - Inventario: Actúa como gestor contenedor para registrar y consultar nodos.
    
Estándares:
    - Aplicación de Programación Orientada a Objetos (POO).
    - Uso de decoradores (@property) y métodos especiales (__str__).
"""


class Nodo:
    """Modela un nodo o dispositivo conectado a la red con autoincremento de ID."""

    id_red = 0

    def __init__(self, ip):
        Nodo.id_red += 1
        self._ip = ip
        self._id = f"{Nodo.id_red:04d}"

    @property
    def ip(self):
        """Devuelve la dirección IP del nodo de forma protegida."""
        return self._ip

    @property
    def id(self):
        """Devuelve el identificador único del nodo de forma protegida."""
        return self._id

    def __str__(self):
        """Representación en cadena oficial del objeto Nodo."""
        return f"{self.ip} (Dispositivo): {self.id} (Puerto: Private) [Acceso: Restringido]"


class Inventario:
    """Gestiona el almacenamiento y búsqueda de múltiples nodos en la red."""

    def __init__(self):
        self.dispositivos = []

    def agregar_disp(self, ip):
        """Crea una nueva instancia de Nodo y la añade al inventario."""
        nuevo = Nodo(ip)
        self.dispositivos.append(nuevo)

    def buscar_disp(self, id_buscar):
        """Busca y devuelve un nodo específico según su ID formateado."""
        for i in self.dispositivos:
            if i.id == id_buscar:
                return i
        return None

    def mostrar_invent(self):
        """Imprime por consola el listado completo de dispositivos registrados."""
        print("\n", "-" * 65, sep="")
        print(" " * 14, "LISTADO DE DISPOSITIVOS EN RED")
        print("-" * 65)
        for equipo in self.dispositivos:
            print(equipo)
        print("-" * 65)


def main():
    """Función principal para ejecutar la interacción del inventario de red."""
    dispositivo = Inventario()
    dispositivo.agregar_disp("192.168.1.1")
    dispositivo.agregar_disp("10.0.0.1")

    id_buscar = input("Inserta el ID: ")
    busqueda = dispositivo.buscar_disp(id_buscar)
    if busqueda:
        print(f"ID {busqueda.id} encontrada.")
    else:
        print(f"ID {id_buscar} no encontrada.")

    dispositivo.mostrar_invent()


if __name__ == "__main__":
    main()
