# BillboardApp

BillboardApp es una aplicación en Python diseñada para analizar y visualizar listas de éxitos musicales (Billboard), tanto en inglés como en español. Permite cargar datos de canciones desde archivos CSV, generar gráficas de popularidad y explorar estadísticas de los artistas y canciones.

## Características

- Lectura y manejo de archivos CSV con información de canciones.
- Gráficas de popularidad por artista, año y género.
- Interfaz gráfica interactiva usando PySimpleGUI o Dash (si aplica).
- Soporte para la lista de 500 canciones incluida en el repositorio.  
- Exportación de resultados y gráficos.

## Requisitos

Se recomienda crear un entorno virtual e instalar las dependencias usando:

```bash
pip install -r requirements.txt
```

Dependencias principales:

- pandas
- matplotlib
- seaborn
- plotly
- numpy
- PySimpleGUI (opcional)
- dash (opcional)

## Uso

1. El archivo CSV con las 500 canciones ya está incluido en el repositorio: `canciones_billboard_500.csv`.
2. Ejecuta los scripts según necesites:

```bash
python "cartelera (1).py"
python "consola_billboard (1).py"
```

3. Explora las gráficas y estadísticas generadas.  
4. Si usas la interfaz gráfica (si aplica), sigue las instrucciones en pantalla.

## Estructura del proyecto

```
BillboardApp/
│
├─ cartelera (1).py       # Script principal para análisis y gráficos
├─ consola_billboard (1).py  # Script alternativo o consola
├─ canciones_billboard_500.csv  # Archivo CSV con 500 canciones
├─ requirements.txt       # Dependencias del proyecto
├─ README.md              # Este archivo
└─ utils.py               # Funciones auxiliares (si aplica)
```

## Mejoras futuras

- Función de búsqueda avanzada por artista o canción.
- Exportar gráficas como imágenes.
- Soporte para más formatos de archivo (Excel, JSON).

## Autores

- Daniel Avellaneda  
- Luis Rico  
- Andrés Vargas
