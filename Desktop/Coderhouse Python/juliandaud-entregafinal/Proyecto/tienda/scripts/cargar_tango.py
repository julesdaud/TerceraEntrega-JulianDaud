from tienda.models import Disco, Artista

def cargar_tango():
    discos = [
        {"titulo": "El tango de hoy", "artista": "Aníbal Troilo", "año_lanzamiento": 1952, "genero": "Tango Argentino", "precio": 14000},
        {"titulo": "A Buenos Aires", "artista": "Astor Piazzolla", "año_lanzamiento": 1961, "genero": "Tango Argentino", "precio": 15000},
        {"titulo": "Tangos para bailar", "artista": "Carlos Di Sarli", "año_lanzamiento": 1955, "genero": "Tango Argentino", "precio": 13500},
        {"titulo": "Reencuentro con Gardel", "artista": "Carlos Gardel", "año_lanzamiento": 1935, "genero": "Tango Argentino", "precio": 15000},
        {"titulo": "Tango y sentimiento", "artista": "Osvaldo Pugliese", "año_lanzamiento": 1960, "genero": "Tango Argentino", "precio": 14500},
        {"titulo": "Mi Buenos Aires querido", "artista": "Roberto Goyeneche", "año_lanzamiento": 1963, "genero": "Tango Argentino", "precio": 15000},
        {"titulo": "A fuego lento", "artista": "Horacio Salgán", "año_lanzamiento": 1967, "genero": "Tango Argentino", "precio": 15500},
        {"titulo": "Tango contemporáneo", "artista": "Astor Piazzolla", "año_lanzamiento": 1970, "genero": "Tango Argentino", "precio": 16000},
        {"titulo": "El bandoneón de Troilo", "artista": "Aníbal Troilo", "año_lanzamiento": 1965, "genero": "Tango Argentino", "precio": 15000},
        {"titulo": "Caminito", "artista": "Edmundo Rivero", "año_lanzamiento": 1962, "genero": "Tango Argentino", "precio": 14000},
        {"titulo": "Tango moderno", "artista": "Osvaldo Pugliese", "año_lanzamiento": 1972, "genero": "Tango Argentino", "precio": 15500},
        {"titulo": "Buenos Aires noche y día", "artista": "Raúl Garello", "año_lanzamiento": 1975, "genero": "Tango Argentino", "precio": 15000},
        {"titulo": "Volver al 900", "artista": "Aníbal Troilo", "año_lanzamiento": 1970, "genero": "Tango Argentino", "precio": 15000},
        {"titulo": "Tango sentimental", "artista": "Carlos Di Sarli", "año_lanzamiento": 1968, "genero": "Tango Argentino", "precio": 14500},
        {"titulo": "Piazzolla en Nueva York", "artista": "Astor Piazzolla", "año_lanzamiento": 1977, "genero": "Tango Argentino", "precio": 16000},
        {"titulo": "Orquesta típica", "artista": "Horacio Salgán", "año_lanzamiento": 1974, "genero": "Tango Argentino", "precio": 15500},
        {"titulo": "Tangos inolvidables", "artista": "Roberto Goyeneche", "año_lanzamiento": 1971, "genero": "Tango Argentino", "precio": 15000},
        {"titulo": "El patio de mi casa", "artista": "Edmundo Rivero", "año_lanzamiento": 1970, "genero": "Tango Argentino", "precio": 14000},
        {"titulo": "Tango de hoy y siempre", "artista": "Raúl Garello", "año_lanzamiento": 1980, "genero": "Tango Argentino", "precio": 15500},
        {"titulo": "Piazzolla clásico", "artista": "Astor Piazzolla", "año_lanzamiento": 1982, "genero": "Tango Argentino", "precio": 16000},
    ]

    for d in discos:
        artista = Artista.objects.filter(nombre=d["artista"]).first()
        if not artista:
            artista = Artista.objects.create(nombre=d["artista"])
        Disco.objects.get_or_create(
            titulo=d["titulo"],
            artista=artista,
            año_lanzamiento=d["año_lanzamiento"],
            genero=d["genero"],
            precio=d["precio"]
        )

    print("20 discos de TANGO cargados correctamente")
