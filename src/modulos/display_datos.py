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


def persistir_info_seleccion(data):
    """
    Guarda la información procesada en un archivo de texto.
    
    Args:
        data (list): Lista de mejores jugadores por posicion.
    """
    
    print(f"Guardando datos procesados en {RUTA_EXPORTACION}...")

    with open(RUTA_EXPORTACION, mode='w', encoding='ansi') as file:
        for posicion, jugadores in data.items():
            # Escribir el encabezado de la posición
            file.write(f"{posicion}:\n")
            
            # Escribir cada jugador (si la lista no está vacía)
            if jugadores:
                for jugador, puntuacion in jugadores:
                    # Limpiar el formato: eliminar comillas dobles extra si existen
                    jugador_limpio = jugador.replace('"', '')
                    file.write(f"{jugador_limpio}, {puntuacion}\n")
            else:
                file.write("(No hay datos disponibles)\n")
            
            # Línea en blanco entre posiciones
            file.write("\n")
    
    print("Datos guardados exitosamente.")