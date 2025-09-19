class Movie:
    def __init__(self, name, yearLaunch, includePlan, note, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan = includePlan
        self.note = note
        self.duratioMinutes = durationMinutes
    def __str__(self):
        return f"Filme: {self.name}"

movie = Movie("Super Mario Bros", 2023, False, 5.0, 130)
movie2 = Movie("Deadpool e Wolverine", 2024, True, 10.0, 145)

print(movie.name)
print(movie2.name)
print(movie)
print(movie2)