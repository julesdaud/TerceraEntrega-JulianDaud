from tienda.models import Disco, Artista

def cargar_rock_nacional():
    discos = [

        {"titulo": "Almendra I", "artista": "Almendra", "año_lanzamiento": 1969, "genero": "Rock Nacional", "precio": 15000},
        {"titulo": "Manal", "artista": "Manal", "año_lanzamiento": 1969, "genero": "Blues Rock", "precio": 15000},
        {"titulo": "Los Gatos", "artista": "Los Gatos", "año_lanzamiento": 1969, "genero": "Rock Nacional", "precio": 15000},
        {"titulo": "Vox Dei", "artista": "Vox Dei", "año_lanzamiento": 1969, "genero": "Rock Nacional", "precio": 15000},
        {"titulo": "Beat en el Mar", "artista": "Manal", "año_lanzamiento": 1968, "genero": "Blues Rock", "precio": 15000},
        {"titulo": "La Balsa", "artista": "Los Gatos", "año_lanzamiento": 1967, "genero": "Rock Nacional", "precio": 15000},

        {"titulo": "Aquelarre", "artista": "Aquelarre", "año_lanzamiento": 1972, "genero": "Progressive Rock", "precio": 16000},
        {"titulo": "Pescado 2", "artista": "Pescado Rabioso", "año_lanzamiento": 1973, "genero": "Rock Psicodélico", "precio": 16000},
        {"titulo": "Artaud", "artista": "Luis Alberto Spinetta", "año_lanzamiento": 1973, "genero": "Rock Nacional", "precio": 17000},
        {"titulo": "Pappo's Blues", "artista": "Pappo", "año_lanzamiento": 1975, "genero": "Blues Rock", "precio": 16500},
        {"titulo": "Polifemo", "artista": "Polifemo", "año_lanzamiento": 1976, "genero": "Rock Nacional", "precio": 16000},
        {"titulo": "El Jardín de los Presentes", "artista": "Invisible", "año_lanzamiento": 1976, "genero": "Rock Nacional", "precio": 16500},
        {"titulo": "Confesiones de Invierno", "artista": "Sui Generis", "año_lanzamiento": 1973, "genero": "Folk Rock", "precio": 15500},
        {"titulo": "El Reloj", "artista": "El Reloj", "año_lanzamiento": 1978, "genero": "Rock Nacional", "precio": 16000},

        {"titulo": "Divididos", "artista": "Sumo", "año_lanzamiento": 1985, "genero": "Rock Nacional", "precio": 16500},
        {"titulo": "La Argentinidad al Palo", "artista": "Patricio Rey y sus Redonditos de Ricota", "año_lanzamiento": 1986, "genero": "Rock Nacional", "precio": 16500},
        {"titulo": "Virus", "artista": "Virus", "año_lanzamiento": 1982, "genero": "New Wave", "precio": 16000},
        {"titulo": "Riff VII", "artista": "Riff", "año_lanzamiento": 1983, "genero": "Hard Rock", "precio": 16000},
        {"titulo": "Signos", "artista": "Soda Stereo", "año_lanzamiento": 1986, "genero": "Rock Nacional", "precio": 16500},
        {"titulo": "Cerati", "artista": "Gustavo Cerati", "año_lanzamiento": 1984, "genero": "Rock Nacional", "precio": 16500},
        {"titulo": "Giran", "artista": "Giran", "año_lanzamiento": 1985, "genero": "Rock Nacional", "precio": 16000},
        {"titulo": "Hermética", "artista": "Hermética", "año_lanzamiento": 1989, "genero": "Heavy Metal", "precio": 16000},

 
        {"titulo": "Dopádromo", "artista": "Babasónicos", "año_lanzamiento": 1997, "genero": "Rock Alternativo", "precio": 16500},
        {"titulo": "Flema", "artista": "Flema", "año_lanzamiento": 1995, "genero": "Punk Rock", "precio": 16000},
        {"titulo": "2 Minutos", "artista": "2 Minutos", "año_lanzamiento": 1994, "genero": "Punk Rock", "precio": 16000},
        {"titulo": "Ataque 77", "artista": "Ataque 77", "año_lanzamiento": 1995, "genero": "Punk Rock", "precio": 16000},
        {"titulo": "Los Brujos", "artista": "Los Brujos", "año_lanzamiento": 1991, "genero": "Rock Alternativo", "precio": 16000},
        {"titulo": "Juana La Loca", "artista": "Juana La Loca", "año_lanzamiento": 1992, "genero": "Rock Alternativo", "precio": 16000},
        {"titulo": "Rex Mix", "artista": "Soda Stereo", "año_lanzamiento": 1992, "genero": "Rock Nacional", "precio": 16500},
        {"titulo": "Animal", "artista": "Los Pericos", "año_lanzamiento": 1993, "genero": "Rock Nacional", "precio": 16000},
        {"titulo": "Almafuerte", "artista": "Almafuerte", "año_lanzamiento": 1998, "genero": "Heavy Metal", "precio": 16000},
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

    print("Discos de ROCK NACIONAL cargados correctamente")
