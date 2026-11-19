"""
Sistema de Gestión de Inversiones y Trading (CLI).

Este script implementa un sistema estructurado en Programación Orientada a Objetos (POO) 
que permite administrar el saldo de una cartera, validar la exposición al riesgo de las 
operaciones (posicionamiento máximo del 10%), calcular niveles de Stop Loss y Take Profit, 
y procesar liquidaciones de mercado aplicando comisiones de broker con una interfaz de 
consola robusta y tolerante a fallos (programación defensiva).
"""


class Cartera:
    """
    Representa la cuenta de inversión principal del usuario.
    
    Gestiona de forma privada el saldo monetario y permite actualizarlo 
    de manera segura aplicando las comisiones del broker.
    """

    def __init__(self, cartera: float):
        """
        Inicializa la cartera con un saldo total disponible.
        
        Args:
            cartera (float): Dinero inicial total de la cartera de inversiones.
        """
        self.__cartera = cartera
    
    @property
    def cartera(self) -> float:
        """Devuelve el saldo actual de la cartera de forma segura."""
        return self.__cartera

    def nuevo_saldo(self, saldo_actual: float, comision: float) -> str:
        """
        Actualiza el saldo privado restando la comisión del broker.
        
        Args:
            saldo_actual (float): Saldo temporal tras liquidar la operación.
            comision (float): Coste monetario de la comisión aplicada.
            
        Returns:
            str: Mensaje con el saldo total actualizado de la cartera.
        """
        self.__cartera = saldo_actual - comision
        return f"La cartera total es: {self.cartera}"


class Trade(Cartera):
    """
    Gestiona la operativa de un activo financiero específico.
    
    Hereda de la clase Cartera para validar la exposición al riesgo,
    calcular los umbrales de Stop Loss y Take Profit, y procesar
    el cierre de la posición con sus respectivos beneficios.
    """

    def __init__(self, cartera: float, precio: float, contratos: float, stop_loss: float = None, take_profit: float = None):
        """
        Inicializa los parámetros de la operación de trading.
        
        Args:
            cartera (float): Dinero total heredado de la clase Cartera.
            precio (float): Precio de entrada al activo.
            contratos (float): Número de contratos o acciones operadas.
            stop_loss (float, optional): Porcentaje máximo de pérdida tolerado.
            take_profit (float, optional): Porcentaje objetivo de ganancia.
        """
        super().__init__(cartera)
        self.__precio = precio
        self.__contratos = contratos
        self.__stop_loss = stop_loss
        self.__take_profit = take_profit

    @property
    def precio(self) -> float:
        """Devuelve el precio de entrada del activo."""
        return self.__precio

    @property
    def contratos(self) -> float:
        """Devuelve el número de contratos de la operación."""
        return self.__contratos

    @property
    def stop_loss(self) -> float:
        """Devuelve el precio o porcentaje calculado del Stop Loss."""
        return self.__stop_loss

    @property
    def take_profit(self) -> float:
        """Devuelve el precio o porcentaje calculado del Take Profit."""
        return self.__take_profit

    def posicion(self, porcentaje: float = 0.10) -> bool:
        """
        Valida que el valor total del trade no supere el límite de riesgo permitido.
        
        Args:
            porcentaje (float): Límite máximo de riesgo por operación (por defecto 10%).
            
        Returns:
            bool: True si la posición es válida, False si excede el capital permitido.
        """
        posicion_operacion = self.cartera * porcentaje
        if posicion_operacion >= self.precio * self.contratos:
            return True
        return False

    def trade(self) -> str:
        """
        Calcula los precios absolutos de Stop Loss y Take Profit si se aprueba la posición.
        
        Returns:
            str: Resumen detallado de la operación y niveles de riesgo, o aviso de fondos insuficientes.
        """
        if self.posicion():
            total_operacion = self.precio * self.contratos
            self.__stop_loss *= self.precio / -100
            self.__stop_loss += self.precio
            self.__take_profit *= self.precio / 100
            self.__take_profit += self.precio
            return f"""
            Operación: {self.precio} (Precio) x {self.contratos} (Contratos) = {total_operacion}
            Precio Stop Loss Unidad: {self.stop_loss}
            Precio Total Stop Loss: {self.stop_loss * self.contratos}
            Precio Take Profit Unidad: {self.take_profit}
            Precio Total Take Profit: {self.take_profit * self.contratos}
            """
        return f"No hay fondos suficientes: Cartera = {self.cartera}, max. 10% por Trade = {self.cartera * 0.10}"

    def cierre(self, precio_cierre: float, comision: float = 0.01) -> str:
        """
        Evalúa el precio de salida de la operación y calcula el beneficio neto y comisiones.
        
        Args:
            precio_cierre (float): Precio al que se liquida el activo.
            comision (float): Porcentaje de comisión del broker (por defecto 1%).
            
        Returns:
            str: Mensaje con el nuevo saldo de la cartera o un aviso de error si está fuera de rango.
        """
        if self.stop_loss <= precio_cierre <= self.take_profit:
            precio_operacion = self.precio * self.contratos
            cierre = precio_cierre * self.contratos
            beneficio = cierre - precio_operacion
            saldo_actual = self.cartera + beneficio
            comision *= precio_operacion
            print(f"Resultado de la operación: {beneficio}")
            print(f"Comisión: {comision:.2f}")
            return self.nuevo_saldo(saldo_actual, comision)
        return f"El precio debe cerrarse dentro del rango Stop Loss: {self.stop_loss} - Take Profit: {self.take_profit}"
        

def main():
    """
    Función controladora principal (Interfaz CLI).
    
    Gestiona el flujo interactivo por consola, implementando programación defensiva 
    mediante bloques try-except para atrapar errores de tipo, control de interrupciones 
    por teclado y bucles de reintento para la entrada de datos.
    """
    try:
        while True:
            try:
                cartera = float(input("\nIngresa el dinero total de tu cartera de inversiones: "))
                precio = float(input("Ingresa el precio del activo: "))
                contratos = float(input("¿Con cuántos contratos/acciones vas a operar?: "))
                stop_loss = float(input("Ingresa el porcentante máximo de pérdida por trade: "))
                take_profit = float(input("Ingresa el porcentante máximo de ganancia por trade: "))
                    
                operacion = Trade(cartera, precio, contratos, stop_loss, take_profit)
                print(operacion.trade())

                if operacion.posicion():
                    while True:
                        try:
                            precio_cierre = float(input("Ingresa el precio de cierre: "))
                            cierre_final = operacion.cierre(precio_cierre)
                            print(cierre_final)
                            if "La cartera total es" in cierre_final:
                                break
                            else:
                                continue
                        except ValueError:
                            print("Error: Ingresa un número válido para el precio del cierre.")
                    break
            except ValueError:
                print("Ingresa un número entero o decimal(Usa puntos como separación).")
            except TypeError:
                print("Faltan datos o son erróneos.")
    except KeyboardInterrupt:
        print("\n\nPrograma cancelado por el usuario.")
    finally:
        print("\nGracias por usar el programa.")


if __name__ == "__main__":
    main()
