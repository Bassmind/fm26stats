"""
Módulo de Menú Principal
=========================
Responsabilidades:
- Mostrar menú principal
- Gestionar opciones del usuario
- Dirigir el flujo del programa
"""

import sys
from .carga_archivos import cargar_archivo
from .extraccion_datos import obtener_mejores_jugadores, procesar_registro, filtrar_jugadores
from .display_datos import persistir_info, persistir_info_seleccion
from .text_file import actualizar_text_file

def elegir_juego():
    """
    Muestra el menú para elegir juego.
    """
    print("\n" + "="*50)
    print("FM26 STATS - Analizador de Datos de GenieScout")
    print("="*50)
    print("\nQue juego quieres analizar:")
    print("(1) FM26")
    print("(2) FM17")
    print("(0) Salir")
    print("-"*50)

def mostrar_menu_principal():
    """
    Muestra el menú principal del programa.
    """
    print("\n" + "="*50)
    print("FM17/26 STATS - Analizador de Datos de GenieScout")
    print("="*50)
    print("\nSelecciona una opción:")
    print("(1) Analizar equipo propio")
    print("(2) Analizar talentos")
    print("(3) Analizar selección")
    print("(0) Salir")
    print("-"*50)


def analizar_equipo_propio():
    """
    Ejecuta el flujo para analizar el equipo propio.
    """
    print("\n[Analizando equipo propio...]\n=====================")
    # 1. Cargar archivos
    datos = cargar_archivo()
    
    # 2. Procesar datos
    jugadores_procesados = procesar_registro(datos)

    # 3. Display de datos/crear archivo
    persistir_info(jugadores_procesados)

    # 4. Actualizar Excel
    # Preguntar si desea actualizar el archivo Excel, con warning
    respuesta = input("¿Actualizaste las columnas de GenieScout, eliminaste F13_bak, backupeaste, cerraste archivos, preparaste nuevos jugadores y agregaste 0's a columnnas (s/n): ").strip().lower()
    if respuesta == 's':
        respuesta = input("¿Deseas actualizar el archivo Excel con los datos procesados? (s/n): ").strip().lower()
        if respuesta == 's':
            from .excel import actualizar_excel
            actualizar_excel(jugadores_procesados)

            # 5. Actualizar Archivo de texto con valores
            actualizar_text_file(jugadores_procesados)

    print("=====================\nAnálisis de equipo propio completado.\n")

    sys.exit(0)


def analizar_fm17():
    """
    Menu para FM17
    """
    print("\n[FM17-Analizando equipo propio...]\n=====================")
    # 1. Cargar archivos
    datos = cargar_archivo(FM="FM17")


def analizar_talentos():
    """
    Flujo para analizar talentos de otros equipos, y definir variables iniciales para posiciones.
    """
    print("\nAnalizando talentos de otros equipos...")
    print("""Ingresa las posiciones a analizar (separadas por comas):
          - GK
          - FB(RL)
          - DFCo
          - DFCi
          - DM
          - MPd
          - MPi
          - MPc
          """)
    valores_entrada = input("Posiciones: ").strip()

    # 1. Cargar archivos
    datos = cargar_archivo()
    
    # 2. Procesar datos
    jugadores_procesados = procesar_registro(datos)

    # 3. Filtrar jugadores
    jugadores_filtrados = filtrar_jugadores(jugadores_procesados, valores_entrada)

    # Display de datos/crear archivo
    persistir_info(jugadores_filtrados)

    print("=====================\nAnálisis de talentos completado.\n")

    sys.exit(0)

def analizar_seleccion():
    """
    Analizar los mejores jugadores actuales para selección nacional
    """
    print("\n[Analizando selección nacional...]\n=====================")
    # 1. Cargar archivos
    datos = cargar_archivo()
    
    # 2. Obtener mejores jugadores
    jugadores_procesados = obtener_mejores_jugadores(datos)

    # 3. Display de datos/crear archivo
    persistir_info_seleccion(jugadores_procesados)

    print("=====================\nAnálisis de selección completado.\n")

    sys.exit(0)

def analizar_talentos_fm17():
    """
    Analizar Talentos para FM17
    """

def menu_principal():
    """
    Ejecuta el bucle principal del programa.
    """
    while True:
        elegir_juego()
        opcion_juego = input("Juego a elegir: ").strip()
        
        #FM26
        if opcion_juego == "1":
            while True:
                mostrar_menu_principal()
                opcion = input("Ingresa tu opción: ").strip()
                
                if opcion == "1":
                    analizar_equipo_propio()
                elif opcion == "2":
                    analizar_talentos()
                elif opcion == "3":
                    analizar_seleccion()
                elif opcion == "0":
                    print("\n¡Hasta luego!")
                    sys.exit(0)
                    break
                else:
                    print("\n[ERROR] Opción no válida. Intenta de nuevo.")
        #FM17
        elif opcion_juego == "2":
            while True:
                mostrar_menu_principal()
                opcion = input("Ingresa tu opción: ").strip()
                
                if opcion == "1":
                    analizar_fm17()
                elif opcion == "2":
                    analizar_talentos_fm17()
                elif opcion == "0":
                    print("\n¡Hasta luego!")
                    sys.exit(0)
                    break
                else:
                    print("\n[ERROR] Opción no válida. Intenta de nuevo.")
        elif opcion_juego == "0":
            print("\n¡Hasta luego!")
            break
        else:
            print("\n[ERROR] Opción no válida. Intenta de nuevo.")
