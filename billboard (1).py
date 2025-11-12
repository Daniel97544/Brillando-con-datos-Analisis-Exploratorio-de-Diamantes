def cargar_canciones(ruta_archivo: str) -> list:
    lista_canciones = []

    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        archivo.readline()  # Saltar encabezados
        for linea in archivo:
            info = linea.strip().split(',')
            if len(info) < 5:
                continue  # Evitar líneas vacías o incompletas
            cancion = {
                'posicion': info[0],
                'nombre_cancion': info[1],
                'nombre_artista': info[2],
                'anio': int(info[3]),
                'letra': info[4]
            }
            lista_canciones.append(cancion)
    return lista_canciones


def buscar_cancion(lista_canciones: list, nombre_cancion: str, anio: int) -> list:
    return [c for c in lista_canciones if c['nombre_cancion'] == nombre_cancion and c['anio'] == anio]


def canciones_anio(lista_canciones: list, anio: int) -> list:
    return [{'posicion': c['posicion'], 'nombre_cancion': c['nombre_cancion'], 'nombre_artista': c['nombre_artista']}
            for c in lista_canciones if c['anio'] == anio]


def canciones_artista_periodo(lista_canciones: list, artista: str, anio_inicial: int, anio_final: int) -> list:
    return [c for c in lista_canciones
            if c['nombre_artista'] == artista and anio_inicial <= c['anio'] <= anio_final]


def todas_canciones_artista(lista_canciones: list, artista: str) -> list:
    return [c for c in lista_canciones if c['nombre_artista'] == artista]


def todos_artistas_cancion(lista_canciones: list, cancion: str) -> list:
    return [c['nombre_artista'] for c in lista_canciones if c['nombre_cancion'] == cancion]


def artistas_mas_populares(lista_canciones: list, cantidad_minima: int = 1) -> dict:
    diccionario_artistas = {}
    for c in lista_canciones:
        artista = c['nombre_artista']
        diccionario_artistas[artista] = diccionario_artistas.get(artista, 0) + 1
    # Filtrar por cantidad mínima
    return {artista: count for artista, count in diccionario_artistas.items() if count >= cantidad_minima}


def artista_estrella(lista_canciones: list) -> str:
    dic_artistas = artistas_mas_populares(lista_canciones)
    return max(dic_artistas, key=dic_artistas.get) if dic_artistas else None


def artistas_y_sus_canciones(lista_canciones: list) -> dict:
    diccionario = {}
    for c in lista_canciones:
        diccionario.setdefault(c['nombre_artista'], []).append(c)
    return diccionario


def promedio_canciones_por_artista(lista_canciones: list) -> float:
    diccionario = artistas_y_sus_canciones(lista_canciones)
    total_canciones = len(lista_canciones)
    total_artistas = len(diccionario)
    return total_canciones / total_artistas if total_artistas > 0 else 0
