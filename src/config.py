"""
Configuración del proyecto
===========================
Variables de configuración globales del proyecto.
"""

# Rutas predeterminadas
RUTA_DATOS_PREDETERMINADA = "data/datos.csv"
RUTA_EXPORTACION = "data/resultados/"

# Posiciones disponibles en FM26
POSICIONES_DISPONIBLES = [
    "POR",  # Portero
    "DEF",  # Defensa
    "MC",   # Mediocampista
    "DEL",  # Delantero
]

# Encabezados esperados en el archivo
ENCABEZADOS_ESPERADOS = [
    "Nombre",
    "CA",
    "PA",
    # Agregar más según sea necesario
]

# Modo de búsqueda
MODO_SHORTLIST = True  # True = shortlist del equipo, False = búsqueda de jugadores
