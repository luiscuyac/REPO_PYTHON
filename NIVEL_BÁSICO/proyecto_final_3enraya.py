"""
Fundamentos - Tres en Raya (Tic-Tac-Toe) Interactivo contra la Máquina

Descripción:
    Implementación del clásico juego del Tres en Raya en la consola. El usuario 
    juega con fichas "O" y la máquina con fichas "X" mediante un selector 
    aleatorio inteligente de campos libres.

Metodología y Desarrollo:
    - Uso de matrices (listas de listas) de 3x3.
    - Transformación de coordenadas lineales (1-9) a bidimensionales mediante 
      operadores de división entera (//) y módulo (%).
    - Bucles de juego continuos (game loops), validación defensiva de entradas 
      y funciones de control de estado (victoria, empate y campos libres).
"""

from random import randrange


def mostrar_tablero(tablero):
    """Dibuja el tablero actual en la consola con formato de cuadrícula."""
    print("+-------" * 3 + "+")
    for fila in tablero:
        print("|       " * 3 + "|")
        for columna in fila:
            print("|   " + str(columna), end="   ")
        print("|")
        print("|       " * 3 + "|")
        print("+-------" * 3 + "+")


def ingresar_movimiento(tablero):
    """Solicita y valida el movimiento del usuario asegurando que la casilla esté libre."""
    continuar = True
    while continuar:
        mov = input("Ingresa tu movimiento (1-9): ")
        if len(mov) == 1 and "1" <= mov <= "9":
            n = int(mov) - 1
            fila = n // 3
            columna = n % 3
            if str(tablero[fila][columna]) not in ["X", "O"]:
                tablero[fila][columna] = "O"
                continuar = False
            else:
                print("Esa casilla está ocupada")
        else:
            print("Entrada no válida. Intenta de nuevo.")


def listar_campos_libres(tablero):
    """Escanea el tablero y devuelve una lista con las coordenadas (fila, col) disponibles."""
    campos_libres = []
    for f in range(3):
        for c in range(3):
            if tablero[f][c] not in ["O", "X"]:
                campos_libres.append((f, c))
    return campos_libres


def verificar_victoria(tablero, signo):
    """Comprueba si el signo indicado ha completado una línea horizontal, vertical o diagonal."""
    for f in range(3):
        if tablero[f][0] == tablero[f][1] == tablero[f][2] == signo:
            return True
    
    for c in range(3):
        if tablero[0][c] == tablero[1][c] == tablero[2][c] == signo:
            return True

    if tablero[0][0] == tablero[1][1] == tablero[2][2] == signo:
        return True
    
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == signo:
        return True
    
    return False


def turno_maquina(tablero):
    """Ejecuta el turno de la máquina seleccionando una casilla libre al azar."""
    libres = listar_campos_libres(tablero)
    if len(libres) > 0:
        hecho = False
        while not hecho:
            mov = randrange(1, 10)
            n = mov - 1
            fila = n // 3
            columna = n % 3
            if (fila, columna) in libres:
                tablero[fila][columna] = "X"
                hecho = True


if __name__ == "__main__":
    print("*" * 5, "Bienvenido a este emocionante juego", "*" * 5, "\n")

    tablero = []

    for f in range(3):
        fila = []
        for c in range(3):
            fila.append(str(3 * f + c + 1))
        tablero.append(fila)

    tablero[1][1] = "X"

    mostrar_tablero(tablero)

    while True:
        ingresar_movimiento(tablero)
        mostrar_tablero(tablero)    
        if verificar_victoria(tablero, "O"):
            print("Has ganado.")
            break
        if len(listar_campos_libres(tablero)) == 0:
            print("Es un empate.")
            break
        
        turno_maquina(tablero)
        mostrar_tablero(tablero)
        if verificar_victoria(tablero, "X"):
            print("Ha ganado la máquina.")
            break
        if len(listar_campos_libres(tablero)) == 0:
            print("Es un empate.")
            break
