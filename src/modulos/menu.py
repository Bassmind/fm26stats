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
from .extraccion_datos import procesar_registro, filtrar_jugadores
from .display_datos import persistir_info


def mostrar_menu_principal():
    """
    Muestra el menú principal del programa.
    """
    print("\n" + "="*50)
    print("FM26 STATS - Analizador de Datos de GenieScout")
    print("="*50)
    print("\nSelecciona una opción:")
    print("(1) Analizar equipo propio")
    print("(2) Analizar talentos")
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
    respuesta = input("¿Actualizaste las columnas de GenieScout? (s/n): ").strip().lower()
    if respuesta == 's':
        respuesta = input("¿Deseas actualizar el archivo Excel con los datos procesados? (s/n): ").strip().lower()
        if respuesta == 's':
            from .excel import actualizar_excel
            actualizar_excel(jugadores_procesados)

    print("=====================\nAnálisis de equipo propio completado.\n")

    

    sys.exit(0)


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


def menu_principal():
    """
    Ejecuta el bucle principal del programa.
    """
    while True:
        mostrar_menu_principal()
        opcion = input("Ingresa tu opción: ").strip()
        
        if opcion == "1":
            analizar_equipo_propio()
        elif opcion == "2":
            analizar_talentos()
        elif opcion == "0":
            print("\n¡Hasta luego!")
            break
        else:
            print("\n[ERROR] Opción no válida. Intenta de nuevo.")
