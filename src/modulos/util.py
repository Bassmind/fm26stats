import logging
import os
from ..config import RUTA_LOGGER

def configurar_logging(nombre_archivo=RUTA_LOGGER):
    """
    Configura el sistema de logging para enviar mensajes a un archivo.
    """
    # Eliminar archivo LOG existente para empezar limpio cada vez
    if os.path.exists(nombre_archivo):
        os.remove(nombre_archivo)
        print("Logger eliminado exitosamente")
    else:
        print("El archivo no existe")

    logging.basicConfig(
        filename=nombre_archivo,
        filemode='a', # 'a' para anexar, 'w' para sobrescribir
        format='%(levelname)s - %(message)s',
        level=logging.INFO # Nivel base: DEBUG, INFO, WARNING, ERROR, CRITICAL
    )

def obtener_logger(nombre):
    """
    Crea y retorna un logger para un módulo específico.
    """
    return logging.getLogger(nombre)

# Opcional: Configurar automáticamente si este archivo se importa
configurar_logging()