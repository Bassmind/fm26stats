"""
Configuración del proyecto
===========================
Variables de configuración globales del proyecto.
"""

# Rutas predeterminadas
RUTA_DATOS_PREDETERMINADA = "C:\\Users\\david\\Downloads\\testfm.csv"
RUTA_EXPORTACION = "data/resultados/"

# Posiciones disponibles en FM26
POSICIONES_DISPONIBLES = [
    "POR",  # Portero
    "DEF",  # Defensa
    "MC",   # Mediocampista
    "DEL",  # Delantero
]

# Modo de búsqueda
MODO_SHORTLIST = True  # True = shortlist del equipo, False = búsqueda de jugadores

"""
ESTRUCTURA DEL ARCHIVO FM GENIE SCOUT INICIAL, (REQUIRED) = Data a extraer:
* Gen
* Name (REQUIRED) -> Nombre del jugador
* Nation
* Club (REQUIRED) -> Club actual
* Age (REQUIRED) -> Edad (Aunque puede ser incorrecta)
* Value -> Valor del jugador
* Sale Value -> Valor de venta del jugador
* Best Pot Rating -> Mejor posicion
* GK - Ball-Playing Goalkeeper - IP (REQUIRED)
* GK - Ball-Playing Goalkeeper - IP (Pot) (REQUIRED)
* GK - Sweeper Keeper - OOP (REQUIRED)
* GK - Sweeper Keeper - OOP (Pot) (REQUIRED)
* WB - Advanced Wing-Back - IP (REQUIRED)
* WB - Advanced Wing-Back - IP (Pot) (REQUIRED)
* D (RL) - Full-Back - OOP (REQUIRED)
* D (RL) - Full-Back - OOP (Pot) (REQUIRED)
* D (C) - Overlapping Centre-Back - IP (REQUIRED)
* D (C) - Overlapping Centre-Back - IP (Pot) (REQUIRED)
* D (C) - Ball-Playing Centre-Back - IP (REQUIRED)
* D (C) - Ball-Playing Centre-Back - IP (Pot) (REQUIRED)
* D (C) - Centre-Back - OOP (REQUIRED)
* D (C) - Centre-Back - OOP (Pot) (REQUIRED)
* M (C) - Attacking Midfielder - IP (REQUIRED)
* M (C) - Attacking Midfielder - IP (Pot) (REQUIRED)
* DM - Defensive Midfielder - OOP (REQUIRED)
* DM - Defensive Midfielder - OOP (Pot) (REQUIRED)
* AM (RL) - Inside Winger - IP (REQUIRED)
* AM (RL) - Inside Winger - IP (Pot) (REQUIRED)
* AM (RL) - Inside Forward - IP (REQUIRED)
* AM (RL) - Inside Forward - IP (Pot) (REQUIRED)
* AM (RL) - Winger - OOP (REQUIRED)
* AM (RL) - Winger - OOP (Pot) (REQUIRED)
* AM (C) - Second Striker - IP (REQUIRED)
* AM (C) - Second Striker - IP (Pot) (REQUIRED)
* AM (C) - Attacking Midfielder - OOP (REQUIRED)
* AM (C) - Attacking Midfielder - OOP (Pot) (REQUIRED)
"""
# Encabezados esperados en el archivo
HEADERS = [
    "Gen",
    "Name",
    "Nation",
    "Club",
    "Age",
    "Value",
    "Sale Value",
    "Best Pot Rating",
    "GK - Ball-Playing Goalkeeper - IP",
    "GK - Ball-Playing Goalkeeper - IP (Pot)",
    "GK - Sweeper Keeper - OOP",
    "GK - Sweeper Keeper - OOP (Pot)",
    "WB - Advanced Wing-Back - IP",
    "WB - Advanced Wing-Back - IP (Pot)",
    "D (RL) - Full-Back - OOP",
    "D (RL) - Full-Back - OOP (Pot)",
    "D (C) - Overlapping Centre-Back - IP",
    "D (C) - Overlapping Centre-Back - IP (Pot)",
    "D (C) - Ball-Playing Centre-Back - IP",
    "D (C) - Ball-Playing Centre-Back - IP (Pot)",
    "D (C) - Centre-Back - OOP",
    "D (C) - Centre-Back - OOP (Pot)",
    "M (C) - Attacking Midfielder - IP",
    "M (C) - Attacking Midfielder - IP (Pot)",
    "DM - Defensive Midfielder - OOP",
    "DM - Defensive Midfielder - OOP (Pot)",
    "AM (RL) - Inside Winger - IP",
    "AM (RL) - Inside Winger - IP (Pot)",
    "AM (RL) - Inside Forward - IP",
    "AM (RL) - Inside Forward - IP (Pot)",
    "AM (RL) - Winger - OOP",
    "AM (RL) - Winger - OOP (Pot)",
    "AM (C) - Second Striker - IP",
    "AM (C) - Second Striker - IP (Pot)",
    "AM (C) - Attacking Midfielder - OOP",
    "AM (C) - Attacking Midfielder - OOP (Pot)",
    # Agregar más según sea necesario
]