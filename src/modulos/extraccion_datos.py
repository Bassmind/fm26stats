"""
Módulo de Extracción de Datos
==============================
Responsabilidades:
- Por cada fila de data, extraer:
  * Data normal
  * Mejores 3 posiciones, para IP y OOP
"""
from src.modulos.excel import corregir_nombre

from ..config import POSICIONES, HEADERS_DICT
from .util import obtener_logger

log = obtener_logger(__name__)

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

def obtener_rating_actual(jugador, jugador_info, jugadores_por_posicion):
    """
    Obtiene el rating actual del jugador para cada posicion potencial y lo agrega al diccionario de jugadores total
    
    Args:
        jugador (dict): Datos del jugador.
        
    Returns:
        object: jugadores_por_posicion actualizado.
    """

    valor_actual_GK = calcular_valor_pos(jugador, HEADERS_DICT['GK-IP-C'], HEADERS_DICT['GK-OOP-C'])
    valor_actual_FB = calcular_valor_pos(jugador, HEADERS_DICT['FB-IP-C'], HEADERS_DICT['FB-OOP-C'])
    valor_actual_DFCo = calcular_valor_pos(jugador, HEADERS_DICT['DFCo-IP-C'], HEADERS_DICT['DFC-OOP-C'])
    valor_actual_DFCi = calcular_valor_pos(jugador, HEADERS_DICT['DFCi-IP-C'], HEADERS_DICT['DFC-OOP-C'])
    valor_actual_DM = calcular_valor_pos(jugador, HEADERS_DICT['DM-IP-C'], HEADERS_DICT['DM-OOP-C'])
    valor_actual_MPd = calcular_valor_pos(jugador, HEADERS_DICT['MPd-IP-C'], HEADERS_DICT['MP(RL)-OOP-C'])
    #valor_actual_MPi = calcular_valor_pos(jugador, HEADERS_DICT['MPi-IP-C'], HEADERS_DICT['MP(RL)-OOP-C'])
    valor_actual_MPc = calcular_valor_pos(jugador, HEADERS_DICT['MPc-IP-C'], HEADERS_DICT['MPc-OOP-C'])

    jugadores_por_posicion[POSICIONES['GK']].append((jugador_info, valor_actual_GK))
    jugadores_por_posicion[POSICIONES['FB']].append((jugador_info, valor_actual_FB))
    jugadores_por_posicion[POSICIONES['DFCo']].append((jugador_info, valor_actual_DFCo))
    jugadores_por_posicion[POSICIONES['DFCi']].append((jugador_info, valor_actual_DFCi))
    jugadores_por_posicion[POSICIONES['DM']].append((jugador_info, valor_actual_DM))
    jugadores_por_posicion[POSICIONES['MPd']].append((jugador_info, valor_actual_MPd))
    #jugadores_por_posicion[POSICIONES['MPi']].append((jugador_info, valor_actual_MPi))
    jugadores_por_posicion[POSICIONES['MPc']].append((jugador_info, valor_actual_MPc))


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


def filtrar_jugadores(jugadores, posiciones_deseadas):
    """
    Funcion para remover cualquier jugador que no pase del umbral minimo
    
    :param jugadores: Lista de jugadores procesados del CSV con sus mejores posiciones
    :param posiciones_deseadas: Valores minimos por posicion
    """
    # Convertir la entrada de posiciones en una lista
    posiciones_lista = [pos.strip() for pos in posiciones_deseadas.split(",")]

    # Crear mapa de posiciones con su valor minimo
    posiciones_minimas_valores = {
        POSICIONES['GK']: posiciones_lista[0],
        POSICIONES['FB']: posiciones_lista[1],
        POSICIONES['DFCo']: posiciones_lista[2],
        POSICIONES['DFCi']: posiciones_lista[3],
        POSICIONES['DM']: posiciones_lista[4],
        POSICIONES['MPd']: posiciones_lista[5],
        POSICIONES['MPi']: posiciones_lista[6],
        POSICIONES['MPc']: posiciones_lista[7],
    }

    jugadores_filtrados = []

    for jugador in jugadores:
        tuplas_aprobadas = []
        
        # Revisar cada tupla de las mejores posiciones para ver si alguna pasa el filtro
        for pos, val in jugador['best_pos_pot']:
            if pos in posiciones_minimas_valores:
                valor_minimo = float(posiciones_minimas_valores[pos]) #Valor minimo para esa posicion

                #Si pasa el filtro, agregar a la lista de aprobados
                if val >= valor_minimo:
                    tuplas_aprobadas.append((pos, val))

        #Si alguna posicion paso el filtro, agregar el jugador a la lista final
        if tuplas_aprobadas:
            jugador['best_pos_pot'] = tuplas_aprobadas

            #Remover tuplas actuales si no estan en las aprobadas
            tuplas_actuales_aprobadas = []
            for pos, val in jugador['best_pos_current']:
                for pos_aprobada, _ in tuplas_aprobadas:
                    if pos == pos_aprobada:
                        tuplas_actuales_aprobadas.append((pos, val))

            jugador['best_pos_current'] = tuplas_actuales_aprobadas
            jugadores_filtrados.append(jugador)
    
    return jugadores_filtrados


def obtener_mejores_jugadores(jugadores, cantidad=10):
    """
    Obtiene los mejores jugadores basados en su mejor posición actual.
    
    Args:
        jugadores (list): Lista de jugadores procesados.
        cantidad (int): Número de mejores jugadores a obtener.
        
    Returns:
        list: Lista de los mejores jugadores.
    """
    
    #Create object from POSICIONES with key as position and value as list of jugadores with that position as best_pos_pot
    jugadores_por_posicion = {pos: [] for pos in POSICIONES.values()}

    #Obtener rating de cada jugador para cada posicion
    for jugador in jugadores:
        #Invirtiendo el nombre de "Jurado, Sebastian" a "Sebastian Jurado" para mejor display y busqueda en excel
        nombre_corregido = corregir_nombre(jugador['Name'])

        jugador_info = nombre_corregido + " - " + jugador['Club']
        obtener_rating_actual(jugador, jugador_info, jugadores_por_posicion)

    #Obtener los mejores X jugadores para cada posicion
    mejores_jugadores_por_posicion = {}
    for pos, jugadores_list in jugadores_por_posicion.items():
        mejores_jugadores_por_posicion[pos] = sorted(jugadores_list, key=lambda x: x[1], reverse=True)[:10]
    
    return mejores_jugadores_por_posicion