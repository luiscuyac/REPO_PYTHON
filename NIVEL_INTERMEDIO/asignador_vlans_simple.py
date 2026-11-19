"""
Automatización de Redes - Configuración Dinámica de VLANs

Descripción:
    Permite el ingreso continuo de IDs de VLAN, validando que se encuentren dentro del 
    rango estándar, evitando duplicados y actualizando la base de datos local en tiempo real.

Metodología:
    Desarrollado de forma autónoma utilizando Inteligencia Artificial como guía 
    para la optimización del formateo de salida de datos numéricos ordenados.

Aplicación en Redes:
    - Simulación de aprovisionamiento masivo de VLANs en un switch.
    - Generación de reportes limpios y ordenados de la base de datos de VLANs activas.
"""

vlans_config = [1, 99]
try:
    while True:
        try:
            vlan = int(input("Presiona \"-1\" para terminar o inserta el número de Vlan: "))
            if vlan == -1:
                print("Has terminado.")
                break
            elif vlan in vlans_config:
                print(f"La Vlan {vlan} ya existe")
                continue            
            elif 1 <= vlan <= 4094:
                print(f"Vlan {vlan} configurada correctamente")
                vlans_config.append(vlan)
            else:
                print("Vlan debe ser entre (1-4094)")                
            
        except ValueError:
            print("Inserta un número entero")

except KeyboardInterrupt:
    print("\nPrograma cancelado por el usuario")

vlan_strings = ", ".join(map(str, sorted(vlans_config)))
print(f"La lista actualizada de vlans es: {vlan_strings}")
