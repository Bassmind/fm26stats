"""
Módulo de Carga de Archivos
============================
Responsabilidades:
- Leer data de archivo (desde nombre predeterminado o abrir archivo)
- Reconocer las columnas y eliminar las primeras filas que no sirven
- Regresar un arreglo/mapa con cada fila y su data
- Permitir activar/desactivar bandera para shortlist o búsqueda de jugadores

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
* D (C) - Ball-Playing Centre-Back - IP (REQUIRED)
* D (C) - Ball-Playing Centre-Back - IP (Pot) (REQUIRED)
* D (C) - Overlapping Centre-Back - IP (REQUIRED)
* D (C) - Overlapping Centre-Back - IP (Pot) (REQUIRED)
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

import csv
from ..config import RUTA_DATOS_PREDETERMINADA

def cargar_extraccion_archivo(ruta_archivo=None):
    """
    Carga un archivo exportado desde FM Genie Scout y se extrae la data
    
    Args:
        ruta_archivo (str, optional): Ruta del archivo a cargar.
        
    Returns:
        list: Lista de diccionarios con los datos de los jugadores.
    """

    print("Comienza extracción de datos desde archivo...")
    print("=============================================")

    data = []

    with open(ruta_archivo or RUTA_DATOS_PREDETERMINADA, mode='r', newline='', encoding='ANSI') as file:
        lector = csv.reader(file)

        try:
            #Skipping first line
            next(lector)
        except StopIteration:
            print("[ERROR] El archivo está vacío o no tiene suficientes líneas.")
            return []
        
        for row in lector:
            data.append(row)

    print(data)

    return data


def reconocer_columnas(datos_raw):
    """
    Reconoce las columnas del archivo y limpia las filas innecesarias.
    
    Args:
        datos_raw (list): Datos crudos del archivo.
        
    Returns:
        tuple: (columnas, datos_limpios)
    """
    pass


def procesar_datos(datos_raw):
    """
    Procesa los datos crudos del archivo.
    
    Args:
        datos_raw (list): Datos crudos del archivo.
        
    Returns:
        list: Lista de diccionarios con datos procesados.
    """
    pass
