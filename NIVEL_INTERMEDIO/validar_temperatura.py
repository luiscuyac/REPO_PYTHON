"""Módulo de monitorización de temperatura para racks y cuartos de telecomunicaciones.

Este script simula un sistema de control periférico que adquiere lecturas de
sensores de temperatura distribuidos en un rack, evaluando umbrales críticos 
para la prevención de incidencias térmicas en infraestructura de red.
"""


def generar_alertas(lecturas: list, umbral: float = 30.0) -> str:
    """Evalúa las lecturas de los sensores del rack y determina el estado de la incidencia.

    Analiza si todos los valores son idénticos (posible fallo de bucle o bloqueo),
    si la temperatura es totalmente estable sin anomalías, o si existe una incidencia
    menor por valores repetidos.

    Args:
        lecturas (list): Lista de números decimales con las temperaturas capturadas en los sensores.
        umbral (float, optional): Límite de temperatura de referencia en grados. Por defecto es 30.0.

    Returns:
        str: Un mensaje formateado con iconos y el diagnóstico técnico de la infraestructura.
    """
    if len(set(lecturas)) == 1:
        return f"\n❌ Alerta Crítica: Comportamiento anómalo, todos los sensores reportan idéntica temperatura."
    elif len(lecturas) == len(set(lecturas)):
        return f"\n✅ Temperatura estable: CPD/Rack operando dentro de parámetros normales."
    return f"\n🟠 Incidencia menor: Múltiples sensores registran valores coincidentes."


def main():
    """Función principal que controla el flujo de adquisición de datos de los sensores.

    Gestiona la entrada interactiva de los valores de temperatura por consola,
    valida la integridad de los datos numéricos, comprueba umbrales críticos de seguridad
    para abortar la ejecución ante emergencias y maneja interrupciones del operador.
    """
    try:
        sensores = 3
        lecturas = []
        flag = True

        print("--- INICIANDO SISTEMA DE TELEMETRÍA DE RACKS ---\n")

        for n in range(sensores):
            if not flag:
                break

            while flag:
                try:
                    sensor = input(f"Ingresa la temperatura del sensor {n + 1}: ")
                    temperatura = float(sensor)
                    if temperatura > 30:
                        print(f"\n🚦 EMERGENCIA TÉRMICA: Sensor {n + 1} marca {temperatura}°C. ¡Accionando protocolo de refrigeración / Llamar a soporte!")
                        flag = False                
                    else:
                        lecturas.append(float(sensor))
                        break
                except ValueError:
                    print("⚠️ Error: Inserta un valor numérico decimal válido separado por punto (.).")
                except Exception:
                    print("⚠️ Error desconocido en la lectura del puerto del sensor.")
    
        if sensores == len(lecturas):
            estado_sistema = generar_alertas(lecturas)
            print(estado_sistema)

    except KeyboardInterrupt:
        print("\n\n⚠️ Monitoreo cancelado manualmente por el operador de sistemas.")
    finally:
        print("\n[Cerrando sockets de sensores y finalizando programa de telemetría].")


if __name__ == "__main__":
    main()
