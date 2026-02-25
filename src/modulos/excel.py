"""
Actualización de archivo Excel con los datos procesados
============================
Responsabilidades:
- Leer data de excel y actualizar con los nuevos datos procesados
"""

import openpyxl
from ..config import RUTA_EXCEL_FILE

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
    #Loading excel file
    workbook = openpyxl.load_workbook(filename=RUTA_EXCEL_FILE)
    #sheet = workbook['At. Madrid(V2)']
    #sheet = workbook['Kochi']
    sheet = workbook['Leon']
    contador_jugadores_fallados = 0

    for jugador in jugadores_procesados:
        nombre_jugador = jugador['nombre']
        nombre_corregido = corregir_nombre(nombre_jugador)

        fila_jugador = find_excel_row(sheet, nombre_corregido)

        if fila_jugador:
            rol = obtener_rol(fila_jugador, sheet)

            #Actualizar datos del jugador
            nuevo_ca = obtener_valor_de_jugador(rol, jugador, 'best_pos_current')
            nuevo_pa = obtener_valor_de_jugador(rol, jugador, 'best_pos_pot')

            #Actualizar Pot (Col G)
            sheet.cell(row=fila_jugador, column=7).value = nuevo_pa

            #Obtener celda a actualizar para CA
            #NOTA: Programa está modificado para actualizar desde Celda 17(Q) hasta Celda 38(AL), modificar Celda final si se requiere
            cell_column_number = obtener_celda_a_modificar(fila_jugador, columna_inicial=17, columna_final=38, sheet=sheet)

            if cell_column_number is not None:
                sheet.cell(row=fila_jugador, column=cell_column_number).value = nuevo_ca
        else:
            contador_jugadores_fallados += 1
            print(f"Jugador {nombre_jugador} no encontrado en el Excel. Requiere revisión manual.")
        
    print(f"Total de jugadores no encontrados en el Excel: {contador_jugadores_fallados}")
    workbook.save(RUTA_EXCEL_FILE)
    print("Excel actualizado correctamente.")


def corregir_nombre(nombre):
    """
    Corrige el nombre del jugador para mejorar la búsqueda en Excel.
    
    Args:
        nombre (str): Nombre original del jugador.
        
    Returns:
        str: Nombre corregido.
    """
    # Implementar reglas de corrección según sea necesario
    nombre_sin_comillas = nombre.strip()[1:-1]
    nombre_redireccionado = [x.strip() for x in nombre_sin_comillas.split(',')]
    nombre_volteado = ' '.join(reversed(nombre_redireccionado))

    return nombre_volteado


def obtener_rol(fila_jugador, sheet):
    """
    Obtener el rol del jugador desde la hoja de Excel.
    
    :param jugador: Jugador a buscar
    :param fila_jugador: Fila del excel del jugador
    :param sheet: Hoja de cálculo de Excel

    Returns:
        str: Rol del jugador
    """
    rol = sheet.cell(row=fila_jugador, column=4).value  # Columna D
    rol = rol.strip()
    rol = rol.replace("W", "").replace("X", "").replace("Y", "").replace("Z", "")

    #Limpiando rol si es FB
    if rol == "FBi" or rol == "FBd":
        rol = "FB"
    
    return rol


def obtener_valor_de_jugador(rol, jugador, cadena_a_checar):
    """
    Obtener el CA/PA del jugador basado en su rol.
    
    :param rol: Rol del jugador segun excel
    :param jugador: Diccionario del jugador con sus datos procesados

    Returns:
        float: CA del jugador para el rol especificado
    """
    
    #Obtener CA del diccionario
    player_roles = jugador.get(cadena_a_checar, [])

    #Buscar el valor correspondiente al rol
    for posicion, valor in player_roles:
        if posicion == rol:
            return valor
    return None


def find_excel_row(sheet, nombre_jugador):
    """
    Busca la fila del jugador en el Excel por su nombre.
    
    Args:
        sheet (Worksheet): Hoja de cálculo de Excel.
        nombre_jugador (str): Nombre del jugador a buscar.
        
    Returns:
        int: Número de fila del jugador o None si no se encuentra.
    """
    for row in range(2, sheet.max_row + 1):  # Asumiendo que la primera fila es el encabezado
        cell_value = sheet.cell(row=row, column=1).value  # Columna A
        if cell_value == nombre_jugador:
            return row
    return None


def obtener_celda_a_modificar(fila_jugador, columna_inicial, columna_final, sheet):
    """
    Obtiene la celda a modificar en la hoja de Excel, buscando la primera celda del rango con valor blanco.
    
    Args:
        fila_jugador (int): Número de fila del jugador.
        columna_inicial (int): Columna inicial desde donde buscar.
        columna_final (int): Columna final hasta donde buscar.
        sheet (Worksheet): Hoja de cálculo de Excel.

    Returns:
        int: Número de columna de la celda a modificar o None si no se encuentra.
    """
    for col in range(columna_inicial, columna_final + 1):
        cell = sheet.cell(row=fila_jugador, column=col)
        if cell.value is None:
            return col
    return None