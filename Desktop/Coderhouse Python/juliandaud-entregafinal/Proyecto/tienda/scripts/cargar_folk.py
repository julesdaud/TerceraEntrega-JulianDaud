from tienda.models import Disco, Artista

def cargar_folk():
    discos = [
        {"titulo": "Bringing It All Back Home", "artista": "Bob Dylan", "año_lanzamiento": 1965, "genero": "Folk", "precio": 15000},
        {"titulo": "Highway 61 Revisited", "artista": "Bob Dylan", "año_lanzamiento": 1965, "genero": "Folk Rock", "precio": 15500},
        {"titulo": "Blonde on Blonde", "artista": "Bob Dylan", "año_lanzamiento": 1966, "genero": "Folk Rock", "precio": 16000},
        {"titulo": "Bookends", "artista": "Simon & Garfunkel", "año_lanzamiento": 1968, "genero": "Folk Rock", "precio": 15500},
        {"titulo": "Parsley, Sage, Rosemary and Thyme", "artista": "Simon & Garfunkel", "año_lanzamiento": 1966, "genero": "Folk", "precio": 15000},
        {"titulo": "Chelsea Girl", "artista": "Nico", "año_lanzamiento": 1967, "genero": "Folk", "precio": 15000},
        {"titulo": "Pink Moon", "artista": "Nick Drake", "año_lanzamiento": 1972, "genero": "Folk", "precio": 16500},
        {"titulo": "Five Leaves Left", "artista": "Nick Drake", "año_lanzamiento": 1969, "genero": "Folk", "precio": 16000},
        {"titulo": "Bryter Layter", "artista": "Nick Drake", "año_lanzamiento": 1971, "genero": "Folk", "precio": 16000},
        {"titulo": "Songs of Leonard Cohen", "artista": "Leonard Cohen", "año_lanzamiento": 1967, "genero": "Folk", "precio": 15000},
        {"titulo": "Songs from a Room", "artista": "Leonard Cohen", "año_lanzamiento": 1969, "genero": "Folk", "precio": 15000},
        {"titulo": "Blue", "artista": "Joni Mitchell", "año_lanzamiento": 1971, "genero": "Folk", "precio": 16500},
        {"titulo": "Court and Spark", "artista": "Joni Mitchell", "año_lanzamiento": 1974, "genero": "Folk", "precio": 16000},
        {"titulo": "Ladies of the Canyon", "artista": "Joni Mitchell", "año_lanzamiento": 1970, "genero": "Folk", "precio": 15500},
        {"titulo": "Tea for the Tillerman", "artista": "Cat Stevens", "año_lanzamiento": 1970, "genero": "Folk", "precio": 15500},
        {"titulo": "Teaser and the Firecat", "artista": "Cat Stevens", "año_lanzamiento": 1971, "genero": "Folk", "precio": 15500},
        {"titulo": "After the Gold Rush", "artista": "Neil Young", "año_lanzamiento": 1970, "genero": "Folk Rock", "precio": 16000},
        {"titulo": "Harvest", "artista": "Neil Young", "año_lanzamiento": 1972, "genero": "Folk Rock", "precio": 16500},
        {"titulo": "Astral Weeks", "artista": "Van Morrison", "año_lanzamiento": 1968, "genero": "Folk Rock", "precio": 17000},
        {"titulo": "Moondance", "artista": "Van Morrison", "año_lanzamiento": 1970, "genero": "Folk Rock", "precio": 16500},
        {"titulo": "Sweet Baby James", "artista": "James Taylor", "año_lanzamiento": 1970, "genero": "Folk", "precio": 15500},
        {"titulo": "Mud Slide Slim and the Blue Horizon", "artista": "James Taylor", "año_lanzamiento": 1971, "genero": "Folk", "precio": 15500},
        {"titulo": "The Freewheelin' Bob Dylan", "artista": "Bob Dylan", "año_lanzamiento": 1963, "genero": "Folk", "precio": 15000},
        {"titulo": "Music from Big Pink", "artista": "The Band", "año_lanzamiento": 1968, "genero": "Folk Rock", "precio": 16000},
        {"titulo": "The Band", "artista": "The Band", "año_lanzamiento": 1969, "genero": "Folk Rock", "precio": 16000},
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

    print(" 25 discos FOLK (60s,70s) cargados correctamente")
