from tienda.models import Disco, Artista

def cargar_rock():
    discos = [
        {"titulo": "Are You Experienced", "artista": "The Jimi Hendrix Experience", "año_lanzamiento": 1967, "genero": "Rock Psicodélico", "precio": 17000},
        {"titulo": "Axis: Bold as Love", "artista": "The Jimi Hendrix Experience", "año_lanzamiento": 1967, "genero": "Rock Psicodélico", "precio": 17000},
        {"titulo": "Electric Ladyland", "artista": "The Jimi Hendrix Experience", "año_lanzamiento": 1968, "genero": "Rock Psicodélico", "precio": 17500},
        {"titulo": "In the Court of the Crimson King", "artista": "King Crimson", "año_lanzamiento": 1969, "genero": "Rock Progresivo Psicodélico", "precio": 17500},
        {"titulo": "Lizard", "artista": "King Crimson", "año_lanzamiento": 1970, "genero": "Rock Progresivo Psicodélico", "precio": 17500},
        {"titulo": "Master of Reality", "artista": "Black Sabbath", "año_lanzamiento": 1971, "genero": "Stoner Rock", "precio": 18000},
        {"titulo": "Paranoid", "artista": "Black Sabbath", "año_lanzamiento": 1970, "genero": "Stoner Rock", "precio": 18000},
        {"titulo": "Vol. 4", "artista": "Black Sabbath", "año_lanzamiento": 1972, "genero": "Stoner Rock", "precio": 18000},
        {"titulo": "Maggot Brain", "artista": "Funkadelic", "año_lanzamiento": 1971, "genero": "Psychedelic Rock", "precio": 17500},
        {"titulo": "In-A-Gadda-Da-Vida", "artista": "Iron Butterfly", "año_lanzamiento": 1968, "genero": "Rock Psicodélico", "precio": 17000},
        {"titulo": "Anthem of the Sun", "artista": "Grateful Dead", "año_lanzamiento": 1968, "genero": "Rock Psicodélico", "precio": 17000},
        {"titulo": "Aoxomoxoa", "artista": "Grateful Dead", "año_lanzamiento": 1969, "genero": "Rock Psicodélico", "precio": 17000},
        {"titulo": "The Piper at the Gates of Dawn", "artista": "Pink Floyd", "año_lanzamiento": 1967, "genero": "Rock Psicodélico", "precio": 17500},
        {"titulo": "A Saucerful of Secrets", "artista": "Pink Floyd", "año_lanzamiento": 1968, "genero": "Rock Psicodélico", "precio": 17500},
        {"titulo": "Meddle", "artista": "Pink Floyd", "año_lanzamiento": 1971, "genero": "Rock Psicodélico", "precio": 18000},
        {"titulo": "The Dark Side of the Moon", "artista": "Pink Floyd", "año_lanzamiento": 1973, "genero": "Rock Psicodélico", "precio": 18000},
        {"titulo": "Wish You Were Here", "artista": "Pink Floyd", "año_lanzamiento": 1975, "genero": "Rock Psicodélico", "precio": 18000},
        {"titulo": "Animals", "artista": "Pink Floyd", "año_lanzamiento": 1977, "genero": "Rock Psicodélico", "precio": 18000},
        {"titulo": "The Wall", "artista": "Pink Floyd", "año_lanzamiento": 1979, "genero": "Rock Psicodélico", "precio": 18500},
        {"titulo": "Larks' Tongues in Aspic", "artista": "King Crimson", "año_lanzamiento": 1973, "genero": "Rock Progresivo Psicodélico", "precio": 18000},
        {"titulo": "Red", "artista": "King Crimson", "año_lanzamiento": 1974, "genero": "Rock Progresivo Psicodélico", "precio": 18000},
        {"titulo": "Disraeli Gears", "artista": "Cream", "año_lanzamiento": 1967, "genero": "Rock Psicodélico", "precio": 17000},
        {"titulo": "Wheels of Fire", "artista": "Cream", "año_lanzamiento": 1968, "genero": "Rock Psicodélico", "precio": 17000},
        {"titulo": "Loving the Alien", "artista": "David Bowie", "año_lanzamiento": 1984, "genero": "Rock Psicodélico", "precio": 17500},
        {"titulo": "Station to Station", "artista": "David Bowie", "año_lanzamiento": 1976, "genero": "Rock Psicodélico", "precio": 17500},
        {"titulo": "Diamond Dogs", "artista": "David Bowie", "año_lanzamiento": 1974, "genero": "Rock Psicodélico", "precio": 17500},
        {"titulo": "Electric Warrior", "artista": "T. Rex", "año_lanzamiento": 1971, "genero": "Glam Rock Psicodélico", "precio": 17500},
        {"titulo": "The Slider", "artista": "T. Rex", "año_lanzamiento": 1972, "genero": "Glam Rock Psicodélico", "precio": 17500},
        {"titulo": "In Through the Out Door", "artista": "Led Zeppelin", "año_lanzamiento": 1979, "genero": "Rock Psicodélico", "precio": 18000},
        {"titulo": "Houses of the Holy", "artista": "Led Zeppelin", "año_lanzamiento": 1973, "genero": "Rock Psicodélico", "precio": 18000},
        {"titulo": "Physical Graffiti", "artista": "Led Zeppelin", "año_lanzamiento": 1975, "genero": "Rock Psicodélico", "precio": 18500},
        {"titulo": "Presence", "artista": "Led Zeppelin", "año_lanzamiento": 1976, "genero": "Rock Psicodélico", "precio": 18500},
        {"titulo": "Sabbath Bloody Sabbath", "artista": "Black Sabbath", "año_lanzamiento": 1973, "genero": "Stoner Rock", "precio": 18000},
        {"titulo": "Sabotage", "artista": "Black Sabbath", "año_lanzamiento": 1975, "genero": "Stoner Rock", "precio": 18000},
        {"titulo": "Technical Ecstasy", "artista": "Black Sabbath", "año_lanzamiento": 1976, "genero": "Stoner Rock", "precio": 18000},
        {"titulo": "Never Say Die!", "artista": "Black Sabbath", "año_lanzamiento": 1978, "genero": "Stoner Rock", "precio": 18000},
        {"titulo": "Heaven and Hell", "artista": "Black Sabbath", "año_lanzamiento": 1980, "genero": "Stoner Rock", "precio": 18000},
        {"titulo": "Mob Rules", "artista": "Black Sabbath", "año_lanzamiento": 1981, "genero": "Stoner Rock", "precio": 18000},
        {"titulo": "Born Again", "artista": "Black Sabbath", "año_lanzamiento": 1983, "genero": "Stoner Rock", "precio": 18000},
        {"titulo": "Electric Magic", "artista": "Blue Cheer", "año_lanzamiento": 1968, "genero": "Rock Psicodélico", "precio": 17000},
    ]

    for d in discos:
        # obtener artista existente o crear uno nuevo si no existe
        artista = Artista.objects.filter(nombre=d["artista"]).first()
        if not artista:
            artista = Artista.objects.create(nombre=d["artista"])

        # crear disco si no existe para evitar duplicados
        Disco.objects.get_or_create(
            titulo=d["titulo"],
            artista=artista,
            año_lanzamiento=d["año_lanzamiento"],
            genero=d["genero"],
            precio=d["precio"]
        )

    print("40 discos ROCK (late 60s - mid 80s) cargados correctamente")

