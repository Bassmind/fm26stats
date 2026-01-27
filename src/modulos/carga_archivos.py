"""
Módulo de Carga de Archivos
============================
Responsabilidades:
- Leer data de archivo (desde nombre predeterminado o abrir archivo)
- Reconocer las columnas y eliminar las primeras filas que no sirven
- Regresar un arreglo/mapa con cada fila y su data
- Permitir activar/desactivar bandera para shortlist o búsqueda de jugadores
"""

import csv
from ..config import RUTA_DATOS_PREDETERMINADA, HEADERS

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
        file_text = file.read()

        array_file = file_text.splitlines()
        data = procesar_file_info(array_file) #Recibimos una list con dicts con solo los datos necesarios 

    print(data)

    return data


def procesar_file_info(datos_raw):
    """
    Reconoce las columnas del archivo y limpia las filas innecesarias.
    
    Args:
        datos_raw (list): Datos crudos del archivo.
        
    Returns:
        tuple: (columnas, datos_limpios)
    """
    data = []
    
    datos_raw.pop(0)  # Elimina la primera fila de encabezados extra

    for item in datos_raw:
        item_list = item.split(';')
        dict_elem = procesar_datos(item_list)
        data.append(dict_elem)

    return data


def procesar_datos(datos_raw):
    """
    Procesa los datos crudos del archivo.
    
    Args:
        datos_raw (list): Una linea de datos del archivo.
        
    Returns:
        list: Lista de diccionarios con datos procesados.
    """

    datos_procesados = dict(zip(HEADERS, datos_raw)) #Crea dict basado en HEADERS y la fila del archivo
    
    # Elimina datos no necesarios del dict
    del datos_procesados["Gen"]
    del datos_procesados["Nation"]
    del datos_procesados["Value"]
    del datos_procesados["Sale Value"]
    del datos_procesados["Best Pot Rating"]

    return datos_procesados