"""Identificador de clases de direcciones IPv4.

Este script solicita una dirección IP por consola, valida su formato 
(octetos numéricos y cantidad correcta) y determina a qué clase tradicional 
pertenece (Clase A, B, C, D, E, Loopback o Broadcast).
"""


def main():
    """Ejecuta el flujo principal del clasificador de direcciones IP."""
    try:    
        direccion_ip = input("\nInserta tu número de dirección ip: ")
        print()

        octetos_verif = True
        for o in direccion_ip.split("."):
            if not o.isdigit():
                octetos_verif = False
                break

        if octetos_verif:
            octetos_for = [int(o) for o in direccion_ip.split(".")]

            if len(octetos_for) == 4:
                primer_octeto = octetos_for[0]
                segundo_octeto = octetos_for[1]
                tercer_octeto = octetos_for[2]
                cuarto_octeto = octetos_for[3]

                if primer_octeto == 0:
                    print("Esta red es de origen/DHCP: No pertenece a ningún host.")
                elif primer_octeto >= 1 and primer_octeto <= 126:
                    print("Esta red es Clase A.")
                elif primer_octeto == 127:
                    print("Esta red es de la pila TCP (Loopback): ip interna del host.")
                elif primer_octeto >= 128 and primer_octeto <= 191:
                    print("Esta red es Clase B.")
                elif primer_octeto >= 192 and primer_octeto <= 223:
                    print("Esta red es Clase C.")
                elif primer_octeto >= 224 and primer_octeto <= 239:
                    print("Esta red es Clase D, es exclusiva para multicast y no tiene máscara.")
                elif primer_octeto >= 240 and primer_octeto <= 255:
                    print("Esta red es Clase E: Red experimental, no se asigna a hosts y no tiene máscara\nCaso especial: 255.255.255.255 (Broadcast).")
                else:
                    print("¡ERROR! IP no válida, fuera de rango.")

            else:
                print("Una dirección IP (32 bits), debe tener 4 octetos.")

        else:
            print("Solo puede contener numeros enteros positivos y puntos como separador.")

    except KeyboardInterrupt:
        print("\nPrograma cancelado por el usuario.")

    except:
        print("Error desconocido: Vuelve a ejecutar el programa.")

    finally:
        print("\nGracias por usar el seleccionador de clases de IP.")


if __name__ == "__main__":
    main()
