"""
Automatización de Redes - Asignador y Validador de VLANs

Descripción:
    Solicita un ID de VLAN al usuario y valida que cumpla con los estándares de red
    (rango 1-4094 y no reservada/usada) antes de proceder con su asignación.

Metodología:
    Desarrollado de forma autónoma utilizando Inteligencia Artificial como guía 
    para estructurar el control de excepciones anidadas y excepciones personalizadas.

Aplicación en Redes:
    - Validación automatizada de inputs en herramientas de aprovisionamiento de switches.
    - Prevención de errores humanos al evitar la asignación de la VLAN 1 (nativa/administración).
"""

def validar_vlan(id_vlan, lista_asignadas):
    if id_vlan < 1 or id_vlan > 4094:
        raise ValueError("Vlan fuera de rango.")
    if id_vlan == 1:
        raise ValueError("Vlan 1 reservada para administración local (no usable por seguridad).")

    if id_vlan in lista_asignadas:
        raise ValueError("Vlan no disponible")

    return f"Vlan {id_vlan} asignada al usuario."


vlans_configuradas = [10, 20, 30, 100]

try:
    while True:
        try:
            nueva_vlan = int(input("Inserta el número de vlan que solicitas: "))
            vlan_asignar = validar_vlan(nueva_vlan, vlans_configuradas)
            print(vlan_asignar)
            break

        except ValueError as e:
            if "invalid literal" in str(e):
                print("Inserta un número entero.")
            else:
                print(e)

except KeyboardInterrupt:
    print("\nPrograma cancelado por el cliente.")

finally:
    print("Gracias por usar el asignador de Vlans.")
    