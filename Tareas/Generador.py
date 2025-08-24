import random
from datetime import datetime, timedelta

# ---------------- INVENTARIO ---------------- #
peliculas = [
    ("Inception", 2010, "Ciencia ficción", 148, "+13"),
    ("Titanic", 1997, "Romance", 195, "+13"),
    ("Avengers", 2012, "Acción", 143, "ATP"),
    ("Parasite", 2019, "Drama", 132, "+16"),
    ("Toy Story", 1995, "Comedia", 81, "ATP"),
    ("La La Land", 2016, "Musical", 128, "+13"),
    ("La Gran Muralla", 2016, "Acción", 103, "+13"),
    ("Drive", 2011, "Thriller", 100, "+16"),
    ("El Rey León", 1994, "Animación", 88, "ATP"),    
    ("Como Entrenar a tu Dragón", 2010, "Animación", 98, "TP")
]

series = [
    ("Breaking Bad", "Drama", "+16", 5, [7, 13, 13, 13, 16]),
    ("Stranger Things", "Ciencia ficción", "+13", 4, [8, 9, 8, 9]),
    ("The Office", "Comedia", "ATP", 9, [6, 22, 23, 14, 26, 24, 24, 24, 25]),
    ("Better Call Saul", "Drama", "+16", 6, [10, 10, 10, 10, 10, 13]),
    ("One Piece", "Aventura", "ATP", 10, [61, 16, 14, 30, 13, 29, 33, 35, 73, 45]),
]





# Asignamos duraciones de capítulos (aleatorias)
def generar_duraciones(num_temporadas, caps_por_temp):
    return [
        [random.randint(20, 60) for _ in range(caps)]
        for caps in caps_por_temp
    ]

series_duraciones = {
    titulo: generar_duraciones(n_temp, caps_por_temp)
    for titulo, _, _, n_temp, caps_por_temp in series
}

# ---------------- USUARIOS ---------------- #
usuarios = [
    ("Luffy", "2002-05-14", 22, "F", ["Ciencia ficción", "Drama", "Aventura", "Comedia"]),
    ("Eleven", "2000-11-02", 24, "M", ["Acción", "Thriller", "Animación"]),
    ("Walter White", "1998-08-21", 26, "M", ["Drama", "Romance", "Comedia"]),
    ("Timón", "2005-01-30", 19, "F", ["Animación"]),
    ("Rose", "2003-06-17", 21, "M", ["Aventura", "Comedia"]),
]

# ---------------- HISTORIAL ---------------- #
def generar_historial(usuarios, peliculas, series):
    historial = []
    for user, _, _, _, _ in usuarios:
        # Vieron entre 3 y 6 contenidos
        vistos = random.randint(3, 6)
        for _ in range(vistos):
            if random.choice([True, False]):  # Película
                peli = random.choice(peliculas)
                titulo = peli[0]
                fecha = datetime(2024, 1, 1) + timedelta(days=random.randint(0, 200))
                duracion = random.randint(30, peli[3])
                historial.append((user, "Pelicula", titulo, fecha.strftime("%Y-%m-%d"), duracion))
            else:  # Serie
                serie = random.choice(series)
                titulo, _, _, _, caps_por_temp = serie
                temp = random.randint(1, len(caps_por_temp))
                cap = random.randint(1, caps_por_temp[temp-1])
                duracion = random.randint(15, 50)
                fecha = datetime(2024, 1, 1) + timedelta(days=random.randint(0, 200))
                historial.append((user, "Serie", f"{titulo} T{temp}C{cap}", fecha.strftime("%Y-%m-%d"), duracion))
    return historial

historial = generar_historial(usuarios, peliculas, series)

# ---------------- GUARDAR ARCHIVOS ---------------- #
with open("inventario.txt", "w", encoding="utf-8") as f:
    f.write("=== Peliculas ===\n")
    for titulo, anio, genero, duracion, clasificacion in peliculas:
        f.write(f"{titulo};{anio};{genero};{duracion};{clasificacion}\n")

    f.write("\n=== Series ===\n")
    for titulo, genero, clasificacion, n_temp, caps_por_temp in series:
        f.write(f"{titulo};{genero};{clasificacion};{n_temp};{caps_por_temp}\n")
        for t, duraciones in enumerate(series_duraciones[titulo], 1):
            f.write(f"  Temporada {t}: {duraciones}\n")

with open("infousuarios.txt", "w", encoding="utf-8") as f:
    for nombre, fnac, edad, genero, favs in usuarios:
        f.write(f"{nombre};{fnac};{edad};{genero};{','.join(favs)}\n")

with open("historial.txt", "w", encoding="utf-8") as f:
    for usuario, tipo, titulo, fecha, duracion in historial:
        f.write(f"{usuario};{tipo};{titulo};{fecha};{duracion}\n")

print("✅ Archivos inventario.txt, infousuarios.txt e historial.txt creados.")
