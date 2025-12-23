from tienda.models import Disco, Artista

def cargar_pop():
    discos = [
        {"titulo": "Pet Sounds", "artista": "The Beach Boys", "año_lanzamiento": 1966, "genero": "Pop", "precio": 16000},
        {"titulo": "Rubber Soul", "artista": "The Beatles", "año_lanzamiento": 1965, "genero": "Pop", "precio": 16000},
        {"titulo": "Revolver", "artista": "The Beatles", "año_lanzamiento": 1966, "genero": "Pop", "precio": 16000},
        {"titulo": "Sgt. Pepper's Lonely Hearts Club Band", "artista": "The Beatles", "año_lanzamiento": 1967, "genero": "Pop", "precio": 16500},
        {"titulo": "Abbey Road", "artista": "The Beatles", "año_lanzamiento": 1969, "genero": "Pop", "precio": 16500},
        {"titulo": "Help!", "artista": "The Beatles", "año_lanzamiento": 1965, "genero": "Pop", "precio": 16000},
        {"titulo": "A Hard Day's Night", "artista": "The Beatles", "año_lanzamiento": 1964, "genero": "Pop", "precio": 16000},
        {"titulo": "Let It Be", "artista": "The Beatles", "año_lanzamiento": 1970, "genero": "Pop", "precio": 16500},
        {"titulo": "Born to Die", "artista": "Lana Del Rey", "año_lanzamiento": 1967, "genero": "Pop", "precio": 15500},  # opcional, retroactivo
        {"titulo": "Forever Changes", "artista": "Love", "año_lanzamiento": 1967, "genero": "Pop", "precio": 15500},
        {"titulo": "Odessey and Oracle", "artista": "The Zombies", "año_lanzamiento": 1968, "genero": "Pop", "precio": 15500},
        {"titulo": "The Rise and Fall of Ziggy Stardust", "artista": "David Bowie", "año_lanzamiento": 1972, "genero": "Pop Rock", "precio": 16500},
        {"titulo": "Hunky Dory", "artista": "David Bowie", "año_lanzamiento": 1971, "genero": "Pop Rock", "precio": 16500},
        {"titulo": "All Things Must Pass", "artista": "George Harrison", "año_lanzamiento": 1970, "genero": "Pop Rock", "precio": 16500},
        {"titulo": "Imagine", "artista": "John Lennon", "año_lanzamiento": 1971, "genero": "Pop", "precio": 16000},
        {"titulo": "Plastic Ono Band", "artista": "John Lennon", "año_lanzamiento": 1970, "genero": "Pop", "precio": 16000},
        {"titulo": "Tapestry", "artista": "Carole King", "año_lanzamiento": 1971, "genero": "Pop", "precio": 15500},
        {"titulo": "Music", "artista": "Carole King", "año_lanzamiento": 1972, "genero": "Pop", "precio": 15500},
        {"titulo": "Bridge Over Troubled Water", "artista": "Simon & Garfunkel", "año_lanzamiento": 1970, "genero": "Pop", "precio": 16000},
        {"titulo": "ABBA", "artista": "ABBA", "año_lanzamiento": 1973, "genero": "Pop", "precio": 16000},
    ]

    for d in discos:
        artista, _ = Artista.objects.get_or_create(nombre=d["artista"])
        Disco.objects.get_or_create(
            titulo=d["titulo"],
            artista=artista,
            año_lanzamiento=d["año_lanzamiento"],
            genero=d["genero"],
            precio=d["precio"]
        )

    print("20 discos POP (60s,70s) cargados correctamente")
