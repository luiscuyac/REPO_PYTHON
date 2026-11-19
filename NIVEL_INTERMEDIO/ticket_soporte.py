"""
Sistema interactivo de asignación de tickets de soporte técnico y redes.

Diseñado y desarrollado por mí como práctica de Programación Orientada a
Objetos (herencia, composición, propiedades y decoradores) en Python, con
apoyo puntual de IA durante el desarrollo.
"""


def elegante(func_ticket):
    """Enmarca la salida del método decorado con líneas separadoras."""
    def wrapper(self):
        print("-" * 80)
        func_ticket(self)
        print("-" * 80)
    return wrapper
    

class Tecnico:
    """Representa los datos básicos de un técnico."""


    def __init__(self, nombre, codigo, telefono):
        self._nombre = nombre
        self._codigo = codigo
        self._telefono = telefono

    @property
    def nombre(self):
        return self._nombre

    @property
    def codigo(self):
        return self._codigo

    @property
    def telefono(self):
        return self._telefono


class Soporte:
    """Asocia un técnico con su nivel de soporte y especialidad."""


    def __init__(self, tecnico, nivel, tecnologia):
        self._tecnico = tecnico
        self._nivel = nivel
        self._tecnologia = tecnologia

    @property
    def tecnico(self):
        return self._tecnico

    @property
    def nivel(self):
        return self._nivel

    @property
    def tecnologia(self):
        return self._tecnologia

    def ficha(self):
        """Muestra la información de soporte y los ratios esperados."""
        print("\n⏰ Los técnicos tienen que cumplir con los ratios de respuesta y solución.")
        print()
        print(f"El técnico es {self.tecnico.nombre} su código es {self.tecnico.codigo} y su teléfono {self.tecnico.telefono}.")
        print(f"El nivel que corresponde con el técnico {self.tecnico.codigo} es el {self.nivel}.")
        print(f"Especialidad del técnico: {self.tecnologia}.")


class Zona(Soporte):
    """Extiende Soporte añadiendo la ciudad de despliegue del técnico."""


    def __init__(self, tecnico, nivel, tecnologia, ciudad):
        super().__init__(tecnico, nivel, tecnologia)
        self._ciudad = ciudad

    @property
    def ciudad(self):
        return self._ciudad

    def ficha(self):
        """Muestra la ficha de soporte incluyendo la zona asignada."""
        super().ficha()
        print(f"La zona de despliegue del técnico es {self.ciudad}.")


class Ticket:
    """Representa un ticket y el técnico asignado según su prioridad."""


    def __init__(self, ticket, prioridad, asignacion_tecnico):
        self._ticket = ticket
        self._prioridad = prioridad
        self._asignacion_tecnico = asignacion_tecnico

    @property
    def ticket(self):
        return self._ticket

    @property
    def prioridad(self):
        return self._prioridad

    @property
    def asignacion_tecnico(self):
        return self._asignacion_tecnico
    
    @elegante
    def asignacion(self):
        """Confirma la asignación del ticket y muestra la ficha del técnico."""
        print("El ticket se asignó correctamente. Datos del técnico: ")
        self.asignacion_tecnico.ficha()
        

datos_1 = Tecnico("Luis", 2030, 139873657)
datos_2 = Tecnico("Marco", 2031, 123456789)
datos_3 = Tecnico("Jose", 2032, 123456456)

inventario = [
     Zona(datos_1, "Nivel_1", "Cisco", "Madrid"),
     Zona(datos_2, "Nivel_2", "Fortinet", "Barcelona"),
     Zona(datos_3, "Nivel_3", "Check Point", "Valencia")
]

print("=" * 37)
print("    Menú de asignación de Tickets")
print("=" * 37)
print("Prioridad Alta:   Inserte 1")
print("Prioridad Media:  Inserte 2")
print("Prioridad Baja:   Inserte 3")
print("=" * 37)
print()

numero_ticket = input("Inserta el número de Ticket: ")

while True:
    prioridad = input("Inserta la Prioridad (1-3): ")
    
    if prioridad == "1":
        asignar_tecnico = inventario[0]
        break
    elif prioridad == "2":
        asignar_tecnico = inventario[1]
        break
    elif prioridad == "3":
        asignar_tecnico = inventario[2]
        break
    else:
        print("Tiene que ser un número entre 1-3")
    
datos_ticket = Ticket(numero_ticket, prioridad, asignar_tecnico)

datos_ticket.asignacion()
