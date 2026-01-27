"""
Módulo de Extracción de Datos
==============================
Responsabilidades:
- Por cada fila de data, extraer:
  * Data normal
  * Mejores 3 posiciones, para IP y OOP
"""
from ..config import POSICIONES, HEADERS_DICT

def procesar_registro(registro):
    """
    Procesa un registro completo extrayendo toda la información relevante.
    
    Args:
        registro (dict): Registro del jugador.
        
    Returns:
        list: Diccionario con datos extraídos del jugador.
    """
    datos_procesados = []
    for jugador in registro:
        jugador_dict = {}
        jugador_dict['nombre'] = jugador['Name']
        jugador_dict['club'] = jugador['Club']
        jugador_dict['edad'] = jugador['Age']
        #Extrar mejors posiciones actuales y potenciales y añadir al dict
        extraer_mejores_posiciones(jugador, jugador_dict)
        
        datos_procesados.append(jugador_dict)

    return datos_procesados


def extraer_mejores_posiciones(jugador, jugador_dict):
    """
    Extrae las 3 mejores posiciones con sus valores para IP y OOP.
    
    Args:
        jugador (dict): Datos del jugador.
        
    Returns:
        dict: Diccionario con las mejores posiciones y sus valores.
    """
    #Calcular promedio de cada posicion potencial
    valores_jugador_p = {}
    valores_jugador_p[POSICIONES['GK']] = calcular_valor_pos(jugador, HEADERS_DICT['GK-IP-P'], HEADERS_DICT['GK-OOP-P'])
    valores_jugador_p[POSICIONES['FB']] = calcular_valor_pos(jugador, HEADERS_DICT['FB-IP-P'], HEADERS_DICT['FB-OOP-P'])
    valores_jugador_p[POSICIONES['DFCo']] = calcular_valor_pos(jugador, HEADERS_DICT['DFCo-IP-P'], HEADERS_DICT['DFC-OOP-P'])
    valores_jugador_p[POSICIONES['DFCi']] = calcular_valor_pos(jugador, HEADERS_DICT['DFCi-IP-P'], HEADERS_DICT['DFC-OOP-P'])
    valores_jugador_p[POSICIONES['DM']] = calcular_valor_pos(jugador, HEADERS_DICT['DM-IP-P'], HEADERS_DICT['DM-OOP-P'])
    valores_jugador_p[POSICIONES['MPd']] = calcular_valor_pos(jugador, HEADERS_DICT['MPd-IP-P'], HEADERS_DICT['MP(RL)-OOP-P'])
    valores_jugador_p[POSICIONES['MPi']] = calcular_valor_pos(jugador, HEADERS_DICT['MPi-IP-P'], HEADERS_DICT['MP(RL)-OOP-P'])
    valores_jugador_p[POSICIONES['MPc']] = calcular_valor_pos(jugador, HEADERS_DICT['MPc-IP-P'], HEADERS_DICT['MPc-OOP-P'])
    
    #Agregar solamente las mejores posiciones potenciales
    agregar_mejores_posiciones_potenciales(valores_jugador_p, jugador_dict)

    #Calcular promedio de cada posicion actual solo para las mejores posiciones potenciales
    agregar_mejores_posiciones_actuales(jugador, jugador_dict)
    

def calcular_valor_pos(jugador, posicionIP, posicionOOP):
    """
    Calcula el valor promedio para la posicion deseada.

    Args:
        jugador (dict): Datos del jugador.

    Returns:
        float: Valor promedio calculado.
    """
    
    #Extraer valores y remover comillas dobles y porcentaje
    ip_p = float((jugador[posicionIP])[1:-2])
    oop_p = float((jugador[posicionOOP])[1:-2])

    return round((ip_p + oop_p) / 2, 2)


def agregar_mejores_posiciones_potenciales(valores_jugador, jugador_dict):
    """
    Calcula las mejores 3 posiciones basadas en los valores promedios.

    Args:
        valores_jugador (dict): Diccionario con valores promedios por posición.
        jugador_dict (dict): Diccionario del jugador donde se agregarán las mejores posiciones.
    """
    #Ordenar posiciones por valor descendente
    posiciones_ordenadas = sorted(valores_jugador.items(), key=lambda x: x[1], reverse=True)
    
    #Seleccionar las 3 mejores posiciones
    mejores_posiciones = posiciones_ordenadas[:3]
    
    jugador_dict['best_pos_pot'] = mejores_posiciones


def agregar_mejores_posiciones_actuales(jugador, jugador_dict):
    """
    Calcula el valor promedio actual basado en los mejores valores potenciales.
    
    :param jugador: Data del jugador
    :param jugador_dict: Dict final para agregar la data procesada
    """

    mejores_posiciones = jugador_dict['best_pos_pot']
    mejores_posiciones_actuales = []

    for posicion, _ in mejores_posiciones:
        if posicion == POSICIONES['GK']:
            valor_actual = calcular_valor_pos(jugador, HEADERS_DICT['GK-IP-C'], HEADERS_DICT['GK-OOP-C'])
        elif posicion == POSICIONES['FB']:
            valor_actual = calcular_valor_pos(jugador, HEADERS_DICT['FB-IP-C'], HEADERS_DICT['FB-OOP-C'])
        elif posicion == POSICIONES['DFCo']:
            valor_actual = calcular_valor_pos(jugador, HEADERS_DICT['DFCo-IP-C'], HEADERS_DICT['DFC-OOP-C'])
        elif posicion == POSICIONES['DFCi']:
            valor_actual = calcular_valor_pos(jugador, HEADERS_DICT['DFCi-IP-C'], HEADERS_DICT['DFC-OOP-C'])
        elif posicion == POSICIONES['DM']:
            valor_actual = calcular_valor_pos(jugador, HEADERS_DICT['DM-IP-C'], HEADERS_DICT['DM-OOP-C'])
        elif posicion == POSICIONES['MPd']:
            valor_actual = calcular_valor_pos(jugador, HEADERS_DICT['MPd-IP-C'], HEADERS_DICT['MP(RL)-OOP-C'])
        elif posicion == POSICIONES['MPi']:
            valor_actual = calcular_valor_pos(jugador, HEADERS_DICT['MPi-IP-C'], HEADERS_DICT['MP(RL)-OOP-C'])
        elif posicion == POSICIONES['MPc']:
            valor_actual = calcular_valor_pos(jugador, HEADERS_DICT['MPc-IP-C'], HEADERS_DICT['MPc-OOP-C'])
        
        mejores_posiciones_actuales.append((posicion, valor_actual))
    
    jugador_dict['best_pos_current'] = mejores_posiciones_actuales