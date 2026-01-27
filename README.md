# fm26stats
Proyecto Personal para copiar data de GenieScout y ver cambios de parametros

Idea del proyecto:

Al abrir, ejecutar un menu para hacer alguna de las siguientes opciones:
* (1)Analizar equipo propio
* (1)Analizar talentos

(1)Analizar equipo propio
- Llamar a Modulo de carga de archivos
- Llamar a Modulo de Extraccion de Data
- Llamar a Modulo de Display Data


(2)Analizar talentos
- Definir variables iniciales para cada posiciones, para filtros.
- Definir atributos ocultos (CANCELADO - No vienen en archivo)
- Llamar a Modulo de carga de archivos
- Llamar a Modulo de Extraccion de Data
- Filtrar data por posiciones/minimos  (CANCELADO: "por atributos ocultos")
- Llamar a Modulo de Display Data

===========================
Modulo de carga de archivos
===========================
- Leer data de archivo (Desde nombre predeterminado o quizas para abrir archivo).
    *Este archivo ya debe haber sido exportado desde FM Genie Scout   
- Reconocer las columnas y eliminar la(s) primera(s) fila(s) que no sirven.
- Regresar un arreglo/mapa con cada fila y su data

Por cada registro de jugadores, el programa debe de:
- Poder activar o desactivar una bandera que defina si estamos con shortlist del mismo equipo, o buscando jugadores

===========================
Modulo de Extraccion de Data:
===========================
- Por cada fila de data, extraer:
    * Nombre
    * CA y PA (CANCELADO - No vienen en archivo)
    * Atributos Ocultos (CANCELADO - No vienen en archivo)
    * Mejores 3 posiciones, con C,P, para IP y OOP

===========================
- Llamar a Modulo de Display Data
===========================
- Mostrar cada fila con su info:
    * Nombre
    * CA y PA (CANCELADO - No vienen en archivo)
    * Atributos Ocultos (CANCELADO - No vienen en archivo)
    * Mejores 3 posiciones, con C,P, para IP y OOP