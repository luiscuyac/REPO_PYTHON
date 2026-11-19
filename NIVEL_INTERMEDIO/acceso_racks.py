"""
Seguridad de Red - Control de Acceso a Racks por Niveles de Soporte

Descripción:
    Evalúa el nivel de un técnico (1-3) y determina a qué racks físicos
    tiene permiso de acceso dentro del Data Center.

Metodología:
    Desarrollado de forma autónoma utilizando Inteligencia Artificial como guía 
    para estructurar el control de excepciones y la lógica de diccionarios.

Aplicación en Redes:
    - Simulación de políticas de seguridad física (IAM básica para técnicos).
    - Gestión de inventario de infraestructura (Racks de servidores, distribución y acceso).
"""

def level_number(level):
    if 0 < level < 4:
        return level
    return None


def access_technician(level):
    level_value = level_number(level)
    if level_value is None:
        print("Valor no reconocible, no pertences a soporte")
        return
    
    rack_number = {
        1: "Rack_server",
        2: "Rack_perimetral",
        3: "Rack_distribution",
        4: "Rack_access",
        5: "Rack_terminals"
    }

    if level_value == 1:
        print(f"Tienes acceso a {rack_number[5]}")
    elif level_value == 2:
        print(f"Tienes acceso a {rack_number[3]}, {rack_number[4]}, {rack_number[5]}")
    else:
        list_total = rack_number.values()
        list_unit = ", ".join(list_total)
        print(f"El nivel 3 tiene acceso total a: {list_unit}")

try:
    level_technician = int(input("¿A qué grupo de soporte pertences, marca del (1-3): "))
    access_technician(level_technician)
except ValueError:
    print("Debes insertar un número entero")
finally:
    print(f"\n{"=" * 65}\nEl acceso o nivel no autorizado están sujetos a sanciones legales\n{"=" * 65}")
