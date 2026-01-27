"""
FM26 STATS - Analizador de Datos de Football Manager 26 desde GenieScout
=========================================================================

Proyecto Personal para copiar data de GenieScout y ver cambios de parámetros.

Al abrir, ejecuta un menú para hacer alguna de las siguientes opciones:
1. Analizar equipo propio
2. Analizar talentos
"""

import sys
from src.modulos.menu import menu_principal


def main():
    """Carga y ejecuta el menú principal del programa."""
    try:
        menu_principal()
    except KeyboardInterrupt:
        print("\n\n[Interrupción del usuario. Programa finalizado.]")
        sys.exit(0)
    except Exception as e:
        print(f"\n[ERROR] Ha ocurrido un error inesperado: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()