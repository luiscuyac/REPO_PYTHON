"""Módulo de validación de nombres de host (Hostnames).

Demuestra el lanzamiento explícito de excepciones (raise), control de flujos
con bucles interactivos y gestión robusta de interrupciones de usuario,
utilizando formato dinámico de cadenas y tipado estático opcional.
"""


def validar_hostname(nombre: str) -> str:
    """Valida las reglas de sintaxis, tipo y longitud para un hostname de red.

    Args:
        nombre (str): Cadena de texto introducida como hostname.

    Returns:
        str: Mensaje de éxito formateado si el hostname es válido.

    Raises:
        TypeError: Si el argumento proporcionado no es de tipo texto.
        ValueError: Si el nombre es demasiado corto o contiene espacios.
    """
    if not isinstance(nombre, str):
        raise TypeError("El hostname debe ser texto.")
    if len(nombre) < 3:
        raise ValueError("Nombre demasiado corto (mínimo 3) ó inválido.")
    if " " in nombre:
        raise ValueError("No se permiten espacios en el hostname.")    
    return f"\n¡Hostname validado con éxito!: {nombre}"


def main() -> None:
    """Ejecuta el flujo principal del programa y el bucle interactivo de validación."""
    name_title = "Validador de Hostname"
    print(f"{'=' * len(name_title)} \n{name_title} \n{'=' * len(name_title)}")

    try:
        while True:
            try:
                nombre = input("Inserta un nombre para el host: ")
                print(validar_hostname(nombre))
                break            
            except ValueError as e:
                print(f"Error de validación: {e}")
            except TypeError as e:
                print(f"Error de tipo: {e}")
    except KeyboardInterrupt:
        print("\n\nPrograma cancelado por el usuario")
    finally:
        print("\nGracias por usar la herramienta de asignación de nombres.")


if __name__ == "__main__":
    main()
