"""
Módulo de Extracción de Datos
==============================
Responsabilidades:
- Por cada fila de data, extraer:
  * Nombre
  * CA y PA
  * Atributos Ocultos
  * Mejores 3 posiciones, con C,P, para IP y OOP
"""

def extraer_nombre(registro):
    """
    Extrae el nombre del jugador de un registro.
    
    Args:
        registro (dict): Registro del jugador.
        
    Returns:
        str: Nombre del jugador.
    """
    pass


def extraer_ca_pa(registro):
    """
    Extrae la Capacidad Actual (CA) y Potencial (PA) del jugador.
    
    Args:
        registro (dict): Registro del jugador.
        
    Returns:
        tuple: (ca, pa)
    """
    pass


def extraer_atributos_ocultos(registro):
    """
    Extrae los atributos ocultos del jugador.
    
    Args:
        registro (dict): Registro del jugador.
        
    Returns:
        dict: Diccionario con atributos ocultos.
    """
    pass


def extraer_mejores_posiciones(registro):
    """
    Extrae las 3 mejores posiciones con sus valores C,P para IP y OOP.
    
    Args:
        registro (dict): Registro del jugador.
        
    Returns:
        list: Lista de tuplas (posicion, c, p, ip, oop)
    """
    pass


def procesar_registro(registro):
    """
    Procesa un registro completo extrayendo toda la información relevante.
    
    Args:
        registro (dict): Registro del jugador.
        
    Returns:
        dict: Diccionario con datos extraídos del jugador.
    """
    datos_procesados = {
        'nombre': extraer_nombre(registro),
        'ca': extraer_ca_pa(registro)[0],
        'pa': extraer_ca_pa(registro)[1],
        'atributos_ocultos': extraer_atributos_ocultos(registro),
        'mejores_posiciones': extraer_mejores_posiciones(registro)
    }
    return datos_procesados
