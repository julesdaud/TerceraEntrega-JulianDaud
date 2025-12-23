from tienda.models import Disco, Artista

def cargar_jazz():
    discos = [
        {"titulo": "Kind of Blue", "artista": "Miles Davis", "año_lanzamiento": 1959, "genero": "Jazz", "precio": 18000},
        {"titulo": "Bitches Brew", "artista": "Miles Davis", "año_lanzamiento": 1970, "genero": "Jazz Fusion", "precio": 18500},
        {"titulo": "A Love Supreme", "artista": "John Coltrane", "año_lanzamiento": 1965, "genero": "Jazz", "precio": 17500},
        {"titulo": "Blue Train", "artista": "John Coltrane", "año_lanzamiento": 1957, "genero": "Jazz", "precio": 17000},
        {"titulo": "Mingus Ah Um", "artista": "Charles Mingus", "año_lanzamiento": 1959, "genero": "Jazz", "precio": 17000},
        {"titulo": "The Black Saint and the Sinner Lady", "artista": "Charles Mingus", "año_lanzamiento": 1963, "genero": "Jazz", "precio": 17500},
        {"titulo": "Time Out", "artista": "Dave Brubeck", "año_lanzamiento": 1959, "genero": "Jazz", "precio": 16500},
        {"titulo": "Take Five", "artista": "Dave Brubeck", "año_lanzamiento": 1959, "genero": "Jazz", "precio": 16500},
        {"titulo": "Empyrean Isles", "artista": "Herbie Hancock", "año_lanzamiento": 1964, "genero": "Jazz", "precio": 17000},
        {"titulo": "Maiden Voyage", "artista": "Herbie Hancock", "año_lanzamiento": 1965, "genero": "Jazz", "precio": 17000},
        {"titulo": "Head Hunters", "artista": "Herbie Hancock", "año_lanzamiento": 1973, "genero": "Jazz Fusion", "precio": 18000},
        {"titulo": "Getz/Gilberto", "artista": "Stan Getz", "año_lanzamiento": 1964, "genero": "Bossa Nova", "precio": 17500},
        {"titulo": "Birth of the Cool", "artista": "Miles Davis", "año_lanzamiento": 1957, "genero": "Jazz", "precio": 17000},
        {"titulo": "Out to Lunch!", "artista": "Eric Dolphy", "año_lanzamiento": 1964, "genero": "Avant-Garde Jazz", "precio": 17500},
        {"titulo": "Speak No Evil", "artista": "Wayne Shorter", "año_lanzamiento": 1966, "genero": "Jazz", "precio": 17500},
        {"titulo": "JuJu", "artista": "Wayne Shorter", "año_lanzamiento": 1964, "genero": "Jazz", "precio": 17000},
        {"titulo": "Cantaloupe Island", "artista": "Herbie Hancock", "año_lanzamiento": 1964, "genero": "Jazz", "precio": 17000},
        {"titulo": "Somethin' Else", "artista": "Cannonball Adderley", "año_lanzamiento": 1958, "genero": "Jazz", "precio": 16500},
        {"titulo": "Saxophone Colossus", "artista": "Sonny Rollins", "año_lanzamiento": 1956, "genero": "Jazz", "precio": 16500},
        {"titulo": "Way Out West", "artista": "Sonny Rollins", "año_lanzamiento": 1957, "genero": "Jazz", "precio": 16500},
        {"titulo": "Cool Struttin'", "artista": "Sonny Clark", "año_lanzamiento": 1958, "genero": "Jazz", "precio": 16500},
        {"titulo": "The Sidewinder", "artista": "Lee Morgan", "año_lanzamiento": 1964, "genero": "Jazz", "precio": 17000},
        {"titulo": "Idle Moments", "artista": "Grant Green", "año_lanzamiento": 1963, "genero": "Jazz", "precio": 17000},
        {"titulo": "Point of Departure", "artista": "Andrew Hill", "año_lanzamiento": 1964, "genero": "Avant-Garde Jazz", "precio": 17500},
        {"titulo": "The Blues and the Abstract Truth", "artista": "Oliver Nelson", "año_lanzamiento": 1961, "genero": "Jazz", "precio": 17000},
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

    print("25 discos JAZZ (60s,70s) cargados correctamente")
