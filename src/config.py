"""
Configuración del proyecto
===========================
Variables de configuración globales del proyecto.
"""

# Rutas predeterminadas
RUTA_DATOS_PREDETERMINADA = "C:\\Users\\david\\Downloads\\testfm.csv"
RUTA_EXCEL_FILE = "C:\\Users\\david\\OneDrive\\Documentos\\FM-Jovenes.xlsx"
RUTA_EXPORTACION = "C:\\Users\\david\\Downloads\\testfm_results.txt"
RUTA_TEXT_FILE = "C:\\Users\\david\\OneDrive\\Documentos\\F13.txt"
RUTA_TEXT_FILE_BAK = "C:\\Users\\david\\OneDrive\\Documentos\\F13_bak.txt"
RUTA_LOGGER = "C:\\Users\\david\\Downloads\\fm13_log.log"

# Posiciones disponibles en FM26
POSICIONES = {
    "GK": "GK",
    "FB": "FB",
    "DFCo": "DFCo",
    "DFCi": "DFCi",
    "DM": "DM",
    "MPd": "MPd",
    "MPi": "MPi",
    "MPc": "MPc",
}

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

HEADERS_DICT = {
    "Gen": "Gen",
    "Name": "Name",
    "Nation": "Nation",
    "Club": "Club",
    "Age": "Age",
    "Value": "Value",
    "SaleValue": "Sale Value",
    "BestPotRating": "Best Pot Rating",
    "GK-IP-C": "GK - Ball-Playing Goalkeeper - IP",
    "GK-IP-P": "GK - Ball-Playing Goalkeeper - IP (Pot)",
    "GK-OOP-C": "GK - Sweeper Keeper - OOP",
    "GK-OOP-P": "GK - Sweeper Keeper - OOP (Pot)",
    "FB-IP-C": "WB - Advanced Wing-Back - IP",
    "FB-IP-P": "WB - Advanced Wing-Back - IP (Pot)",
    "FB-OOP-C": "D (RL) - Full-Back - OOP",
    "FB-OOP-P": "D (RL) - Full-Back - OOP (Pot)",
    "DFCo-IP-C": "D (C) - Overlapping Centre-Back - IP",
    "DFCo-IP-P": "D (C) - Overlapping Centre-Back - IP (Pot)",
    "DFCi-IP-C": "D (C) - Ball-Playing Centre-Back - IP",
    "DFCi-IP-P": "D (C) - Ball-Playing Centre-Back - IP (Pot)",
    "DFC-OOP-C": "D (C) - Centre-Back - OOP",
    "DFC-OOP-P": "D (C) - Centre-Back - OOP (Pot)",
    "DM-IP-C": "M (C) - Attacking Midfielder - IP",
    "DM-IP-P": "M (C) - Attacking Midfielder - IP (Pot)",
    "DM-OOP-C": "DM - Defensive Midfielder - OOP",
    "DM-OOP-P": "DM - Defensive Midfielder - OOP (Pot)",
    "MPd-IP-C": "AM (RL) - Inside Winger - IP",
    "MPd-IP-P": "AM (RL) - Inside Winger - IP (Pot)",
    "MPi-IP-C": "AM (RL) - Inside Forward - IP",
    "MPi-IP-P": "AM (RL) - Inside Forward - IP (Pot)",
    "MP(RL)-OOP-C": "AM (RL) - Winger - OOP",
    "MP(RL)-OOP-P": "AM (RL) - Winger - OOP (Pot)",
    "MPc-IP-C": "AM (C) - Second Striker - IP",
    "MPc-IP-P": "AM (C) - Second Striker - IP (Pot)",
    "MPc-OOP-C": "AM (C) - Attacking Midfielder - OOP",
    "MPc-OOP-P": "AM (C) - Attacking Midfielder - OOP (Pot)",
    # Agregar más según sea necesario
}