"""
Módulo de Carga de Archivos
============================
Responsabilidades:
- Leer data de archivo (desde nombre predeterminado o abrir archivo)
- Reconocer las columnas y eliminar las primeras filas que no sirven
- Regresar un arreglo/mapa con cada fila y su data
- Permitir activar/desactivar bandera para shortlist o búsqueda de jugadores
"""

def cargar_archivo(ruta_archivo=None):
    """
    Carga un archivo exportado desde FM Genie Scout.
    
    Args:
        ruta_archivo (str, optional): Ruta del archivo a cargar.
        
    Returns:
        list: Lista de diccionarios con los datos de los jugadores.
    """
    pass


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
