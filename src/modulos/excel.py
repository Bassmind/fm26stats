"""
Actualización de archivo Excel con los datos procesados
============================
Responsabilidades:
- Leer data de excel y actualizar con los nuevos datos procesados
"""

import openpyxl

def actualizar_excel(jugadores_procesados):
    """
    # Abrir archivo Excel existente
    # Por cada jugador:
        # Comparar si existe (Col A)
        # Si:
            # Obtener Rol (Col D)
            # Actualizar Pot (Col G)
            # Actualizar Actual (Col Q-Y)
        # No:
            #  Agregar jugador a lista de excepciones para tratar manualmente
    
    :param jugadores_procesados: Jugadores procesados con sus mejores roles
    """


    print("Excel actualizado correctamente.")
    pass