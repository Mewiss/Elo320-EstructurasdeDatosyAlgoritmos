import random
import datetime
import csv

# --- Datos base ---
GENEROS = ["Acción", "Comedia", "Drama", "Ciencia ficción", "Romance", "Terror", "Documental", "Animación"]
CLASIFICACIONES = ["ATP", "+7", "+13", "+16", "+18"]
NOMBRES = ["Ana", "Luis", "Carla", "Pedro", "Marta", "Juan", "Sofía", "Diego", "Camila", "Andrés"]

# --- Funciones auxiliares ---
def generar_peliculas(n=10):
    peliculas = []
    for i in range(n):
        titulo = f"Pelicula_{i+1}"
        año = random.randint(1980, 2024)
        genero = random.choice(GENEROS)
        duracion = random.randint(60, 180)
        clasif = random.choice(CLASIFICACIONES)
        peliculas.append((titulo, año, genero, duracion, clasif))
    return peliculas

def generar_series(n=5):
    series = []
    for i in range(n):
        titulo = f"Serie_{i+1}"
        genero = random.choice(GENEROS)
        clasif = random.choice(CLASIFICACIONES)
        temporadas = random.randint(1, 10)
        caps = random.randint(6, 24)
        duracion_cap = random.randint(20, 60)
        series.append((titulo, genero, clasif, temporadas, caps, duracion_cap))
    return series

def generar_usuarios(n=5):
    usuarios = []
    for i in range(n):
        nombre = NOMBRES[i % len(NOMBRES)] + f"_{i}"
        fecha = f"{random.randint(1970,2015)}-{random.randint(1,12):02}-{random.randint(1,28):02}"
        genero = random.choice(["M", "F"])
        categorias = random.sample(GENEROS, 2)
        usuarios.append((nombre, fecha, genero, categorias))
    return usuarios

def generar_historial(usuarios, peliculas, series, n=50):
    historial = []
    for i in range(n):
        usuario = random.choice(usuarios)[0]
        if random.random() < 0.6:
            titulo, año, genero, duracion, clasif = random.choice(peliculas)
            visto = random.randint(int(duracion*0.5), duracion)
        else:
            titulo, genero, clasif, temporadas, caps, duracion_cap = random.choice(series)
            visto = random.randint(int(duracion_cap*0.5), duracion_cap)
        fecha = datetime.date.today() - datetime.timedelta(days=random.randint(0, 365))
        historial.append((usuario, titulo, fecha.isoformat(), visto))
    return historial

def guardar_csv(nombre, encabezados, filas):
    with open(nombre, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(encabezados)
        writer.writerows(filas)

# --- Generar datos pequeños (ejemplo) ---
peliculas_small = [
    ("Inception", 2010, "Ciencia ficción", 148, "+13"),
    ("Titanic", 1997, "Romance", 195, "+13"),
    ("Avengers", 2012, "Acción", 143, "ATP"),
    ("Parasite", 2019, "Drama", 132, "+16"),
    ("Toy Story", 1995, "Comedia", 81, "ATP"),
]
series_small = [
    ("Breaking Bad", "Drama", "+16", 5, 13, 47),
    ("Stranger Things", "Ciencia ficción", "+13", 4, 8, 50),
    ("The Office", "Comedia", "ATP", 9, 24, 22),
]
usuarios_small = [
    ("Ana", "2000-05-15", "F", ["Romance", "Comedia"]),
    ("Luis", "1998-11-03", "M", ["Acción", "Ciencia ficción"]),
    ("Carla", "2010-08-21", "F", ["Comedia", "Animación"]),
    ("Pedro", "1985-03-12", "M", ["Drama", "Documental"]),
]
historial_small = generar_historial(usuarios_small, peliculas_small, series_small, 20)

guardar_csv("inventario_small.csv",
    ["tipo", "titulo", "año", "genero", "duracion", "clasificacion", "temporadas", "caps_por_temp", "duracion_cap"],
    [["pelicula", *p, "", "", ""] for p in peliculas_small] +
    [["serie", s[0], "", s[1], "", s[2], s[3], s[4], s[5]] for s in series_small]
)
guardar_csv("usuarios_small.csv",
    ["nombre", "fecha_nacimiento", "genero", "categorias_favoritas"],
    [[u[0], u[1], u[2], "|".join(u[3])] for u in usuarios_small]
)
guardar_csv("historial_small.csv",
    ["usuario", "titulo", "fecha_visualizacion", "duracion"],
    historial_small
)

print("Archivos pequeños generados ✅")

# --- Generar datos grandes (1000+ registros) ---
peliculas_big = generar_peliculas(500)
series_big = generar_series(200)
usuarios_big = generar_usuarios(100)
historial_big = generar_historial(usuarios_big, peliculas_big, series_big, 2000)

guardar_csv("inventario_big.csv",
    ["tipo", "titulo", "año", "genero", "duracion", "clasificacion", "temporadas", "caps_por_temp", "duracion_cap"],
    [["pelicula", *p, "", "", ""] for p in peliculas_big] +
    [["serie", s[0], "", s[1], "", s[2], s[3], s[4], s[5]] for s in series_big]
)
guardar_csv("usuarios_big.csv",
    ["nombre", "fecha_nacimiento", "genero", "categorias_favoritas"],
    [[u[0], u[1], u[2], "|".join(u[3])] for u in usuarios_big]
)
guardar_csv("historial_big.csv",
    ["usuario", "titulo", "fecha_visualizacion", "duracion"],
    historial_big
)

print("Archivos grandes (1000+ registros) generados ✅")
