class Movie:
    name = ""
    yearLaunch = 0
    includedPlan = False
    note = 0
    durationMinutes = 0

# Primeiro Filme

movie = Movie()
movie.name = "Super Mario Bros"
movie.yearLaunch = 2023
movie.includedPlan = False
movie.note = 5.0
movie.durationMinutes = 130

print("## Dados do Filme ##")
print(f"Nome do filme: {movie.name}\nAno de lançamento: {movie.yearLaunch}")
