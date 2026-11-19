"""
Automatización y Planificación - Simulación de Proyección de Crecimiento Compuesto

Descripción:
    Calcula la acumulación progresiva de un valor base aplicando un porcentaje 
    de incremento periódico y aportaciones adicionales fijas a lo largo del tiempo.

Metodología:
    Desarrollado de forma autónoma utilizando Inteligencia Artificial como guía 
    para la implementación de funciones de orden superior (callbacks de validación) 
    y la sanitización avanzada de entradas de usuario.

Aplicación en Redes:
    - Planificación de capacidad (Capacity Planning): Proyección de crecimiento
      de tráfico de red, consumo de ancho de banda o almacenamiento de logs.
    - Estimación de costes operativos (OpEx) y escalado presupuestario para 
      infraestructura cloud o Data Center.
"""

def funcion_capital(capital):
    capital_prov = capital.replace(",", ".")
    try:
        capital = float(capital_prov)

    except ValueError:
        raise ValueError("Inserta un número válido.")
    
    if capital <= 0:
        raise ValueError("El capital no puede ser menor o igual a 0")
    
    return capital


def funcion_aumento_capital(ingreso):
    ingreso_prov = ingreso.replace(",", ".")
    try:
        ingreso = float(ingreso_prov)

    except ValueError:
        raise ValueError("Inserta un número válido.")
        
    if ingreso <= 0:
        raise ValueError("El aumento de capital no puede ser menor o igual a 0")
        
    return ingreso


def funcion_interes(interes):
    interes_prov = interes.replace(",", ".").replace("%", "")
    try:
        interes = float(interes_prov) * 0.01

    except ValueError:
        raise ValueError("Inserta un número válido.")
    
    if interes <= 0:
        raise ValueError("El interés no puede ser menor o igual a 0")
    
    return interes


def funcion_meses(meses):
    try:
        meses = int(meses)

    except ValueError:
        raise ValueError("Inserta un número entero.")
    
    if meses <= 0:
        raise ValueError("Los meses no pueden ser menor o igual a 0")
    
    return meses


def pedir_dato(pregunta, mi_funcion):
    while True:
        try:
            dato = input(pregunta)
            return mi_funcion(dato)

        except ValueError as e:
            print(f"ERROR: {e}")


try:
    capital = pedir_dato("Inserta el capital inicial: ", funcion_capital)
    interes = pedir_dato("Inserta el interés anual: ", funcion_interes)
    meses = pedir_dato("Inserta la cantidad de meses a calcular: ", funcion_meses)

    print("¿Hay aumento de capital?")
    while True:
        try:
            aumento = input("Ingresa 0 para \"NO\" y 1 para \"SÍ\": ")
            if aumento not in ["0", "1"]:
                raise ValueError("Solo se admite 0 y 1")
            elif aumento == "0":
                aumento = 0
                break
            else:
                aumento = pedir_dato("Ingresa el aumento mensual de capital: ", funcion_aumento_capital)
                break
            
        except ValueError as e:
            print(f"ERROR: {e}")

    for m in range(1, meses + 1):
        acumulador = (capital * (interes / 12)) + capital + aumento
        capital = acumulador
        print(f"El mes {m} el resultado es {capital:,.2f}")

    print(f"""
    {"=" * 40}
           RESULTADO DE LA SIMULACIÓN
    {"=" * 40}
    Periodo:           {meses} meses
    Interés mensual:   {((interes * 100) / 12):,.2f}%
    Aumento mensual:   {aumento:,.2f}€
    {"-" * 40}
    SALDO FINAL:       {capital:,.2f}€
    {"=" * 40}
    """)

except KeyboardInterrupt:
    print("\n\n\"Programa cancelado por el usuario.\"")

finally:
    print("\nGracias por utilizar la calculadora de interés compuesto.")
