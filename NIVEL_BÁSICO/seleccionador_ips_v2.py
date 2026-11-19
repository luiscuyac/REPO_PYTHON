"""Clasificador y validador de direcciones IPv4 por consola.

Este script solicita una dirección IP, valida su estructura de 4 octetos,
comprueba que estén en el rango válido (0-255) y determina su clase tradicional
junto con su máscara de red por defecto.
"""


def ip_clases(primer_octeto):
    """Determina la clase de red IPv4 y su máscara según el valor del primer octeto.

    Args:
        primer_octeto (int): Valor numérico del primer octeto de la IP (0-255).

    Returns:
        str: Descripción de la clase de red, máscara y características especiales.
    """
    if primer_octeto == 0:
        return "Origen/DHCP: No pertenece a ningún host y no tiene máscara."
    elif primer_octeto >= 1 and primer_octeto <= 126:
        return "Clase A y su máscara es 255.0.0.0"
    elif primer_octeto == 127:
        return "Loopback: IP interna del host y no tiene máscara."
    elif primer_octeto >= 128 and primer_octeto <=191:
        return "Clase B y su máscara es 255.255.0.0"
    elif primer_octeto >= 192 and primer_octeto <=223:
        return "Clase C y su máscara es 255.255.255.0"
    elif primer_octeto >= 224 and primer_octeto <=239:
        return "Clase D, es exclusiva para multicast y no tiene máscara."
    elif primer_octeto >= 240 and primer_octeto <=255:
        return "Clase E: Red experimental, no se asigna a hosts y no tiene máscara\nCaso especial: 255.255.255.255 (Broadcast)."
    return "¡ERROR! IP no válida, fuera de rango."


def verif_octetos(direccion_ip):
    """Valida que una cadena tenga el formato IPv4 correcto (4 octetos numéricos de 0 a 255).

    Args:
        direccion_ip (str): Cadena de texto ingresada por el usuario.

    Returns:
        bool: True si la IP es estrictamente válida, False en caso contrario.
    """
    octetos_for = direccion_ip.split(".")
    
    if len(octetos_for) != 4:
        return False
    
    for o in octetos_for:
        if not o.isdigit():
            return False
        if int(o) < 0 or int(o) > 255:
            return False
    
    return True


def main():
    """Ejecuta el flujo principal del programa de clasificación de IPs."""
    try:    
        direccion_ip = input("\nInserta una dirección ip: ")

        if verif_octetos(direccion_ip):
            octetos_for = [int(o) for o in direccion_ip.split(".")]
            primer_octeto = octetos_for[0]
            clase = ip_clases(primer_octeto)
            print(f"\nEsta red es {clase}")
        else:
            print("Tienes que insertar 4 números enteros (0-255) y separados por puntos.")

    except KeyboardInterrupt:
        print("\n\nPrograma cancelado por el usuario.")

    except:
        print("\nError desconocido: Vuelve a iniciar el programa.")

    finally:
        print("\nGracias por usar el clasificador de IPs.")


if __name__ == "__main__":
    main()
