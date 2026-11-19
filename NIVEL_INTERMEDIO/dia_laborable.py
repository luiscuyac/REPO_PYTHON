"""
Seguridad - Control de Acceso por Calendario e Introspección

Descripción:
    Verifica los permisos de acceso evaluando el día de la semana ingresado.
    Utiliza el módulo `calendar` y la función de introspección `getattr`
    para consultar dinámicamente las constantes numéricas de los días,
    restringiendo el acceso a días laborables (lunes a viernes).

Metodología:
    Introspección dinámica (getattr), control de flujo con manejo de excepciones
    (AttributeError) y normalización de cadenas de texto (.upper()).
"""

import calendar

def entrance(daywork):
    try:
        permission = getattr(calendar, daywork)
        if 0 <= permission <= 4:
            print("✅ Puedes entrar, día laborable.")
        else:
            print("🚦 Acceso denegado, no es día laborable.")
    except AttributeError:
        print("❌ No existe.")

daywork = input("Ingresa el día: ").upper() # En inglés.

entrance(daywork)
