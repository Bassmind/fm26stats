"""
Módulo de Menú Principal
=========================
Responsabilidades:
- Mostrar menú principal
- Gestionar opciones del usuario
- Dirigir el flujo del programa
"""

import sys
from .carga_archivos import cargar_archivo, procesar_datos
from .extraccion_datos import procesar_registro
from .display_datos import mostrar_tabla_jugadores


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
    print("\n[Analizando equipo propio...]")
    # 1. Cargar archivos
    datos = cargar_archivo()
    # 2. Extracción de datos
    # 3. Display de datos
    pass


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
    print("Check:" + valores_entrada)

    # cargar_archivo()
    # extraer_datos()
    # filtrar_data()
    # mostrar tabla / exportar archivo

    sys.exit(0)
    pass


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
