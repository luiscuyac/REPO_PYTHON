def informar_datos(datos):
    """ Recoge información de dispositivo """
    def wrapper(self):
        print("=" * 37)
        print("     Información de Dispositivo")
        print("=" * 37)
        datos(self)
        print("=" * 37)    
    return wrapper


class Dispositivo:
    """
    Clase padre:
    Args:
    Nombre: Como se llama el dispositivo en la red
    IP: Dirección lógica del dispositivo
    Marca: Fabricante del dispositivo

    """
    def __init__(self, nombre, ip, marca):
        self._nombre = nombre
        self._ip = ip
        self._marca = marca

    @property
    def nombre(self):
        return self._nombre

    @property
    def ip(self):
        return self._ip

    @property
    def marca(self):
        return self._marca

    def informacion(self):
        print("El nombre del dispositivo es {}".format(self.nombre))
        print("La dirección ip es {}".format(self.ip))
        print("La marca del dispositivo es {}".format(self.marca))


class Router(Dispositivo):
    """
    Clase hija:
    Args:
    Todos del padre: 'Dispositivo'
    Enrutamiento: El protocolo de enrutamiento
    Conexión: Tipo físico de conexión

    """
    def __init__(self, nombre, ip, marca, enrutamiento, conexion):
        """
        Agregamos al padre y complementamos con los nuevos atributos
           
        """
        super().__init__(nombre, ip, marca)
        self._enrutamiento = enrutamiento
        self._conexion = conexion

    @property
    def enrutamiento(self):
        return self._enrutamiento

    @property
    def conexion(self):
        return self._conexion

    @informar_datos
    def informacion(self):
        super().informacion()
        print("El protocolo de enrutamiento es {}".format(self.enrutamiento))
        print("La conexión es mediante {}".format(self.conexion))

    
class AccessPoint(Dispositivo):
    """
    Clase hija:
    Args:
    Todos del padre: 'Dispositivo'
    SSID: Nombre de la Wlan
    Canal: Canal de transferencia de datos

    """
    def __init__(self, nombre, ip, marca, ssid, canal):
         """
         Agregamos al padre y complementamos con los nuevos atributos
         
         """
         super().__init__(nombre, ip, marca)
         self._ssid = ssid
         self._canal = canal

    @property
    def ssid(self):
        return self._ssid

    @property
    def canal(self):
        return self._canal

    @informar_datos
    def informacion(self):
        super().informacion()
        print(f"Red Inalámbrica: {self.ssid}")
        print(f"Canal: {self.canal}")


inventario = [
    Router("R1", "192.168.1.1", "Cisco", "RIP", "5G"),
    AccessPoint("A1", "10.0.0.1", "Ubiquiti", "WLAN_10", "3")
]

for indice, equipo in enumerate(inventario, start=1):
    print("\n")
    print("=" * 37)
    print(f"Equipo: {indice}")
    equipo.informacion()
    