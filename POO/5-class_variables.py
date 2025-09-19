class Movie:
    platform = "OneBitsFilmes"
    def __init__(self, name, yearLaunch, includePlan, note, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan = includePlan
        self.note = note
        self.duratioMinutes = durationMinutes
    def __str__(self):
        return f"Filme: {self.name}"
    
    def techinal_sheet(self):
        print("*** Dados do Filme ***\n")
        print(f"Plataforma: {Movie.platform}")
        print(f"Nome do filme: {self.name}")
        print(f"Ano de lançamento: {self.yearLaunch}")
        print(f"Está no plano? {self.includedPlan}")
        print(f"Qual a nota do filme? {self.note}")
        print(f"Duração do filme: {self.duratioMinutes}\n")

mario = Movie("Super Mario Bross", 2023, False, 5.0, 130)
# Modificando a plataforma
Movie.platform = "Netflix"
deadpool = Movie("Deadpool e Wolverine", 2024, True, 9.9, 140)

mario.techinal_sheet()
deadpool.techinal_sheet()