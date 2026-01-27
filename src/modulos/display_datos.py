"""
Módulo de Display de Datos
===========================
Responsabilidades:
- Guardar la data en archivo de texto
"""
from ..config import RUTA_EXPORTACION

def persistir_info(data):
    """
    Guarda la información procesada en un archivo de texto.
    
    Args:
        data (list): Lista de diccionarios con los datos procesados.
    """
    
    print(f"Guardando datos procesados en {RUTA_EXPORTACION}...")
    
    with open(RUTA_EXPORTACION, mode='w', encoding='ansi') as file:
        for jugador in data:
            linea = ', '.join([f"{clave}: {valor}" for clave, valor in jugador.items()])
            file.write(linea + '\n')
    
    print("Datos guardados exitosamente.")