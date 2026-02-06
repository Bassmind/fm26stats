"""
Modulo para actualizar el archivo de texto FM13.txt con los valores actuales de los parámetros
"""

from src.config import RUTA_TEXT_FILE, RUTA_TEXT_FILE_BAK
from .util import obtener_logger
import os

log = obtener_logger(__name__)

def actualizar_text_file(jugadores_procesados):
    """Actualiza el archivo de texto con los parámetros dados."""
    #Rename existing file as backup
    log.info("Iniciando proceso de actualización del archivo de texto.")

    if os.path.exists(RUTA_TEXT_FILE):
        os.rename(RUTA_TEXT_FILE, RUTA_TEXT_FILE_BAK)

    #Preparar diccionario de jugadores procesados para búsqueda rápida
    jugadores_dict = preparar_diccionario_jugadores(jugadores_procesados)

    #Cargar info del archivo y crear nuevo archivo con datos actualizados
    try:
        with open(RUTA_TEXT_FILE_BAK, 'r', encoding='utf-8') as file:
            with open(RUTA_TEXT_FILE, 'w', encoding='utf-8') as new_file:
                #Bandera que indica si estamos en la sección de actualización
                actualizacion_en_proceso = True
                rol_jugador = ""

                for line in file:
                    #Modificacion termina cuando se encuentra una línea que comienza con '='
                    if line[0] == '=':
                        actualizacion_en_proceso = False

                    if(actualizacion_en_proceso):
                        if line[0] == '*' or line[0] == '' or line[0] == '\n':
                            #Actualizando Rol
                            if line[0] == '*':
                                rol_jugador = line[1:5].replace('-','')

                                if rol_jugador == 'FBd' or rol_jugador == 'FBi':
                                    rol_jugador = 'FB'
                            
                            new_file.write(line)
                        else:
                            log.info(f"Procesando línea para actualización: {line.strip()}")
                            line_to_print = get_correct_line(line, rol_jugador, jugadores_dict)
                            new_file.write(line_to_print)
                    else:
                        # Si no estamos en la sección de actualización, escribimos la línea tal cual
                        new_file.write(line)

            
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta especificada: {RUTA_TEXT_FILE}")
        return
    pass


def preparar_diccionario_jugadores(jugadores_procesados):
    """
    Prepara un diccionario de jugadores para búsqueda rápida por nombre corregido.
    Estructura: {nombre_corregido: {CA:{..pos.. : value}, PA:{..pos.. : value}}}
    
    Args:
        jugadores_procesados (list): Lista de jugadores procesados.
        
    Returns:
        dict: Diccionario con nombres corregidos como claves y datos de jugadores como valores.
    """
    jugadores_dict = {}
    for jugador in jugadores_procesados:
        nombre_jugador = jugador['nombre']
        nombre_corregido = corregir_nombre(nombre_jugador)

        #Creando CA dict y PA dict
        ca_dict = {}
        pa_dict = {}

        ca_dict = jugador['best_pos_current']
        pa_dict = jugador['best_pos_pot']

        jugadores_dict[nombre_corregido] = {
            'CA': ca_dict,
            'PA': pa_dict
        }

    return jugadores_dict


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


def get_correct_line(line, rol_jugador, jugadores_dict):
    """
    Obtiene la línea correcta para escribir en el nuevo archivo, actualizando los valores si el jugador y rol coinciden.
    
    Args:
        line (str): Línea original del archivo.
        rol_jugador (str): Rol actual del jugador.
        jugadores_dict (dict): Diccionario de jugadores procesados.

    Returns:
        str: Línea actualizada o original según corresponda.
    """
    string_to_return = ''

    #Para jugadores en loan, ignorar tab inicial
    if line[0] == '\t':
        string_to_return += '\t'
        line = line[1:]
    
    #Obtener nombre del jugador en base al primer tab, y quitando parentesis
    jugador_en_archivo = line.split('\t', 1)[0]

    #Si hay parentesis, quitarlo junto a su valor encerrado
    index_of_parenthesis = jugador_en_archivo.find('(')
    if index_of_parenthesis != -1:
        jugador_en_archivo = jugador_en_archivo[:index_of_parenthesis] + jugador_en_archivo[index_of_parenthesis + 3:]

    #Con el nombre del jugador, buscar en el diccionario el CA y PA acorde al rol
    ca_for_player = None
    pa_for_player = None

    log.info(f"Buscando datos para jugador: '{jugador_en_archivo}' con rol '{rol_jugador}'")
    if jugador_en_archivo in jugadores_dict:
        ca_dict = jugadores_dict[jugador_en_archivo]['CA']
        pa_dict = jugadores_dict[jugador_en_archivo]['PA']

        for item in ca_dict:
            if rol_jugador in item:
                ca_for_player = item[1]
                break

        for item in pa_dict:
            if rol_jugador in item:
                pa_for_player = item[1]
                break
        
        log.info(f"Datos nuevos encontrados en GenieScout file para '{jugador_en_archivo}': CA={ca_for_player}, PA={pa_for_player}")
    else:
        log.warning(f"No se encontró el jugador '{jugador_en_archivo}' en los datos procesados.")
        print(f"ADVERTENCIA: No se encontró el jugador '{jugador_en_archivo}' en los datos procesados.")
    
    #Crear la string a retornar basado en formato
    #   Helge Johan Brendesæter(B)	71.25		73.19
    i = 0   #Contador para los caracteres de la línea
    skip_count = 5 #Digitos a saltar cuando se encuentra un número (incluye el punto decimal y dos decimales)
    var_ca_pa = 0 #Contador para saber si se está en CA (0) o PA (1)

    while i < len(line):
        char = line[i]

        if char.isdigit() and var_ca_pa < 2:
            i += skip_count  # Saltar los caracteres del número actual
            if var_ca_pa == 0:
                string_to_return += f"{ca_for_player:.2f}"
            elif var_ca_pa == 1:
                string_to_return += f"{pa_for_player:.2f}"

            var_ca_pa += 1
        else:
            string_to_return += char
            i += 1

    return string_to_return