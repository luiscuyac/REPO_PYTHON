"""
Módulo de gestión de inventario de dispositivos de red.
Permite generar un archivo base y filtrar equipos específicos.
"""


def generar_inventario(nombre_archivo: str) -> None:
    """Crea un archivo de texto con un listado inicial de dispositivos de red.

    Args:
        nombre_archivo (str): Ruta o nombre del archivo donde se guardarán los datos.
    """
    dispositivos = [
        "ROUTER_Cisco",
        "SWITCH_Nexo",
        "ROUTER_Juniper",
        "PC_Admin"
    ]

    with open(nombre_archivo, "w", encoding="utf-8") as file:
        file.write("\n".join(dispositivos) + "\n")


def filtrar_routers(nombre_archivo: str) -> set:
    """Lee el inventario y filtra únicamente los routers normalizados a minúsculas.

    Args:
        nombre_archivo (str): Ruta del archivo a leer.

    Returns:
        set: Conjunto con los nombres de los routers únicos en minúsculas.
    """
    with open(nombre_archivo, "r", encoding="utf-8") as file:
        lineas = file.read().splitlines()
    
    routers = {linea.lower() for linea in lineas if "router" in linea.lower()}
    return routers


if __name__ == "__main__":
    archivo_inventario = "dispositivos.txt"
    generar_inventario(archivo_inventario)
    resultado = filtrar_routers(archivo_inventario)
    print("Inventario filtrado de routers: ", resultado)
